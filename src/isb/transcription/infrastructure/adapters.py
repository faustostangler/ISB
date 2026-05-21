import json
import whisper
from pathlib import Path
from isb.shared_kernel.types import ContentId
from isb.transcription.domain.entities import Transcript
from isb.transcription.domain.value_objects import Segment
from isb.transcription.application.ports import TranscriberPort

class WhisperTranscriberAdapter(TranscriberPort):
    """Infrastructure adapter implementing the TranscriberPort using openai-whisper.

    This adapter manages the transition from raw audio data to structured text representation,
    interacting with the neural network model to generate transcripts and caching the output.

    Attributes:
        cache_dir: The directory path where transcription results are cached on disk.
        model_name: The Whisper model size identifier to load (e.g., "base", "tiny").
    """

    def __init__(self, cache_dir: str | Path, model_name: str = "base") -> None:
        """Initializes the Whisper transcriber adapter.

        Args:
            cache_dir: Directory path on the local filesystem to store transcription cache files.
            model_name: Size/name of the Whisper model to load. Defaults to "base".
        """
        # Infrastructure limit: Local storage caching prevents redundant compute, saving CPU/GPU cycles
        # on subsequent reads of the same media content.
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.model_name = model_name
        
        # Infrastructure limit: Lazy-load the neural network model to avoid excessive memory consumption
        # during application bootstrap when the transcription context may not be active.
        self._model = None

    def transcribe(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
        """Runs the speech-to-text inference pipeline on a local audio file.

        Loads the Whisper model on-demand, executes the inference process with optional language hints,
        normalizes confidence scores, compiles the results into a domain Transcript entity,
        and serializes a JSON audit copy to the local cache directory.

        Args:
            content_id: The ContentId domain identifier of the associated media episode.
            audio_path: Absolute filesystem path to the local audio file.
            language_hint: Optional ISO language code hint to guide the transcriber model.

        Returns:
            A Transcript domain entity containing the processed full text, timing segments,
            and model execution metadata.

        Raises:
            FileNotFoundError: If the input audio file does not exist.
        """
        # Exception handling: Stop early if the source audio has been purged or is unreachable,
        # preventing the C-level model loader from executing on non-existent targets.
        if not audio_path.exists():
            raise FileNotFoundError(f"Audio file for transcription not found at: {audio_path}")
        
        # Infrastructure limit: Load the Whisper model on-demand (lazy load) and keep it in-memory
        # to amortize heavy disk-to-RAM model-loading latency across multiple transcription runs.
        if self._model is None:
            self._model = whisper.load_model(self.model_name)
        
        options = {}
        if language_hint:
            options["language"] = language_hint
        
        result = self._model.transcribe(str(audio_path), **options)
        
        full_text = result.get("text", "")
        detected_language = result.get("language", "pt")
        
        segments: list[Segment] = []
        raw_segments = result.get("segments") or []
        max_end_time = 0.0
        
        for raw_seg in raw_segments:
            start = float(raw_seg.get("start", 0.0))
            end = float(raw_seg.get("end", 0.0))
            text = raw_seg.get("text", "").strip()
            
            if end > max_end_time:
                max_end_time = end
            
            # Infrastructure limit: Log probability ranges from negative infinity to 0.0.
            # We map this range to [0.0, 1.0] to satisfy the domain segment confidence invariants.
            avg_logprob = raw_seg.get("avg_logprob")
            if avg_logprob is not None:
                confidence = min(max(1.0 + float(avg_logprob), 0.0), 1.0)
            else:
                confidence = 1.0
            
            segments.append(
                Segment(
                    start_seconds=start,
                    end_seconds=end,
                    text=text,
                    confidence=confidence
                )
            )
        
        transcript = Transcript(
            content_id=content_id,
            full_text=full_text,
            segments=segments,
            language=detected_language,
            model=self.model_name,
            duration_seconds=max_end_time
        )
        
        # Infrastructure limit: Persist a serialized JSON representation in cache_dir as a backup.
        # This provides a disaster recovery boundary and allows auditing the raw Whisper outputs.
        cache_file_path = self.cache_dir / f"{content_id}.json"
        cache_payload = {
            "content_id": str(content_id),
            "full_text": transcript.full_text,
            "language": transcript.language,
            "model": transcript.model,
            "duration_seconds": transcript.duration_seconds,
            "segments": [
                {
                    "start_seconds": s.start_seconds,
                    "end_seconds": s.end_seconds,
                    "text": s.text,
                    "confidence": s.confidence
                }
                for s in transcript.segments
            ]
        }
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        
        return transcript
