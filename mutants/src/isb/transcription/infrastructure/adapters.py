import json
import whisper
from pathlib import Path
from isb.shared_kernel.types import ContentId
from isb.transcription.domain.entities import Transcript
from isb.transcription.domain.value_objects import Segment
from isb.transcription.application.ports import TranscriberPort
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

class WhisperTranscriberAdapter(TranscriberPort):
    """Infrastructure adapter implementing the TranscriberPort using openai-whisper.

    This adapter manages the transition from raw audio data to structured text representation,
    interacting with the neural network model to generate transcripts and caching the output.

    Attributes:
        cache_dir: The directory path where transcription results are cached on disk.
        model_name: The Whisper model size identifier to load (e.g., "base", "tiny").
    """

    def __init__(self, cache_dir: str | Path, model_name: str = "base") -> None:
        args = [cache_dir, model_name]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁWhisperTranscriberAdapterǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁWhisperTranscriberAdapterǁ__init____mutmut_mutants'), args, kwargs, self)

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_orig(self, cache_dir: str | Path, model_name: str = "base") -> None:
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

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_1(self, cache_dir: str | Path, model_name: str = "XXbaseXX") -> None:
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

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_2(self, cache_dir: str | Path, model_name: str = "BASE") -> None:
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

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_3(self, cache_dir: str | Path, model_name: str = "base") -> None:
        """Initializes the Whisper transcriber adapter.

        Args:
            cache_dir: Directory path on the local filesystem to store transcription cache files.
            model_name: Size/name of the Whisper model to load. Defaults to "base".
        """
        # Infrastructure limit: Local storage caching prevents redundant compute, saving CPU/GPU cycles
        # on subsequent reads of the same media content.
        self.cache_dir = None
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.model_name = model_name
        
        # Infrastructure limit: Lazy-load the neural network model to avoid excessive memory consumption
        # during application bootstrap when the transcription context may not be active.
        self._model = None

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_4(self, cache_dir: str | Path, model_name: str = "base") -> None:
        """Initializes the Whisper transcriber adapter.

        Args:
            cache_dir: Directory path on the local filesystem to store transcription cache files.
            model_name: Size/name of the Whisper model to load. Defaults to "base".
        """
        # Infrastructure limit: Local storage caching prevents redundant compute, saving CPU/GPU cycles
        # on subsequent reads of the same media content.
        self.cache_dir = Path(None)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.model_name = model_name
        
        # Infrastructure limit: Lazy-load the neural network model to avoid excessive memory consumption
        # during application bootstrap when the transcription context may not be active.
        self._model = None

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_5(self, cache_dir: str | Path, model_name: str = "base") -> None:
        """Initializes the Whisper transcriber adapter.

        Args:
            cache_dir: Directory path on the local filesystem to store transcription cache files.
            model_name: Size/name of the Whisper model to load. Defaults to "base".
        """
        # Infrastructure limit: Local storage caching prevents redundant compute, saving CPU/GPU cycles
        # on subsequent reads of the same media content.
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=None, exist_ok=True)
        self.model_name = model_name
        
        # Infrastructure limit: Lazy-load the neural network model to avoid excessive memory consumption
        # during application bootstrap when the transcription context may not be active.
        self._model = None

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_6(self, cache_dir: str | Path, model_name: str = "base") -> None:
        """Initializes the Whisper transcriber adapter.

        Args:
            cache_dir: Directory path on the local filesystem to store transcription cache files.
            model_name: Size/name of the Whisper model to load. Defaults to "base".
        """
        # Infrastructure limit: Local storage caching prevents redundant compute, saving CPU/GPU cycles
        # on subsequent reads of the same media content.
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=None)
        self.model_name = model_name
        
        # Infrastructure limit: Lazy-load the neural network model to avoid excessive memory consumption
        # during application bootstrap when the transcription context may not be active.
        self._model = None

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_7(self, cache_dir: str | Path, model_name: str = "base") -> None:
        """Initializes the Whisper transcriber adapter.

        Args:
            cache_dir: Directory path on the local filesystem to store transcription cache files.
            model_name: Size/name of the Whisper model to load. Defaults to "base".
        """
        # Infrastructure limit: Local storage caching prevents redundant compute, saving CPU/GPU cycles
        # on subsequent reads of the same media content.
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)
        self.model_name = model_name
        
        # Infrastructure limit: Lazy-load the neural network model to avoid excessive memory consumption
        # during application bootstrap when the transcription context may not be active.
        self._model = None

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_8(self, cache_dir: str | Path, model_name: str = "base") -> None:
        """Initializes the Whisper transcriber adapter.

        Args:
            cache_dir: Directory path on the local filesystem to store transcription cache files.
            model_name: Size/name of the Whisper model to load. Defaults to "base".
        """
        # Infrastructure limit: Local storage caching prevents redundant compute, saving CPU/GPU cycles
        # on subsequent reads of the same media content.
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, )
        self.model_name = model_name
        
        # Infrastructure limit: Lazy-load the neural network model to avoid excessive memory consumption
        # during application bootstrap when the transcription context may not be active.
        self._model = None

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_9(self, cache_dir: str | Path, model_name: str = "base") -> None:
        """Initializes the Whisper transcriber adapter.

        Args:
            cache_dir: Directory path on the local filesystem to store transcription cache files.
            model_name: Size/name of the Whisper model to load. Defaults to "base".
        """
        # Infrastructure limit: Local storage caching prevents redundant compute, saving CPU/GPU cycles
        # on subsequent reads of the same media content.
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=False, exist_ok=True)
        self.model_name = model_name
        
        # Infrastructure limit: Lazy-load the neural network model to avoid excessive memory consumption
        # during application bootstrap when the transcription context may not be active.
        self._model = None

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_10(self, cache_dir: str | Path, model_name: str = "base") -> None:
        """Initializes the Whisper transcriber adapter.

        Args:
            cache_dir: Directory path on the local filesystem to store transcription cache files.
            model_name: Size/name of the Whisper model to load. Defaults to "base".
        """
        # Infrastructure limit: Local storage caching prevents redundant compute, saving CPU/GPU cycles
        # on subsequent reads of the same media content.
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=False)
        self.model_name = model_name
        
        # Infrastructure limit: Lazy-load the neural network model to avoid excessive memory consumption
        # during application bootstrap when the transcription context may not be active.
        self._model = None

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_11(self, cache_dir: str | Path, model_name: str = "base") -> None:
        """Initializes the Whisper transcriber adapter.

        Args:
            cache_dir: Directory path on the local filesystem to store transcription cache files.
            model_name: Size/name of the Whisper model to load. Defaults to "base".
        """
        # Infrastructure limit: Local storage caching prevents redundant compute, saving CPU/GPU cycles
        # on subsequent reads of the same media content.
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.model_name = None
        
        # Infrastructure limit: Lazy-load the neural network model to avoid excessive memory consumption
        # during application bootstrap when the transcription context may not be active.
        self._model = None

    def xǁWhisperTranscriberAdapterǁ__init____mutmut_12(self, cache_dir: str | Path, model_name: str = "base") -> None:
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
        self._model = ""
    
    xǁWhisperTranscriberAdapterǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁWhisperTranscriberAdapterǁ__init____mutmut_1': xǁWhisperTranscriberAdapterǁ__init____mutmut_1, 
        'xǁWhisperTranscriberAdapterǁ__init____mutmut_2': xǁWhisperTranscriberAdapterǁ__init____mutmut_2, 
        'xǁWhisperTranscriberAdapterǁ__init____mutmut_3': xǁWhisperTranscriberAdapterǁ__init____mutmut_3, 
        'xǁWhisperTranscriberAdapterǁ__init____mutmut_4': xǁWhisperTranscriberAdapterǁ__init____mutmut_4, 
        'xǁWhisperTranscriberAdapterǁ__init____mutmut_5': xǁWhisperTranscriberAdapterǁ__init____mutmut_5, 
        'xǁWhisperTranscriberAdapterǁ__init____mutmut_6': xǁWhisperTranscriberAdapterǁ__init____mutmut_6, 
        'xǁWhisperTranscriberAdapterǁ__init____mutmut_7': xǁWhisperTranscriberAdapterǁ__init____mutmut_7, 
        'xǁWhisperTranscriberAdapterǁ__init____mutmut_8': xǁWhisperTranscriberAdapterǁ__init____mutmut_8, 
        'xǁWhisperTranscriberAdapterǁ__init____mutmut_9': xǁWhisperTranscriberAdapterǁ__init____mutmut_9, 
        'xǁWhisperTranscriberAdapterǁ__init____mutmut_10': xǁWhisperTranscriberAdapterǁ__init____mutmut_10, 
        'xǁWhisperTranscriberAdapterǁ__init____mutmut_11': xǁWhisperTranscriberAdapterǁ__init____mutmut_11, 
        'xǁWhisperTranscriberAdapterǁ__init____mutmut_12': xǁWhisperTranscriberAdapterǁ__init____mutmut_12
    }
    xǁWhisperTranscriberAdapterǁ__init____mutmut_orig.__name__ = 'xǁWhisperTranscriberAdapterǁ__init__'

    def transcribe(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
        args = [content_id, audio_path, language_hint]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_orig'), object.__getattribute__(self, 'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_mutants'), args, kwargs, self)

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_orig(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_1(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        if audio_path.exists():
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_2(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            raise FileNotFoundError(None)
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_3(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        if self._model is not None:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_4(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            self._model = None
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_5(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            self._model = whisper.load_model(None)
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_6(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        options = None
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_7(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            options["language"] = None
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_8(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            options["XXlanguageXX"] = language_hint
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_9(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            options["LANGUAGE"] = language_hint
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_10(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        result = None
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_11(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        result = self._model.transcribe(None, **options)
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_12(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        result = self._model.transcribe(**options)
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_13(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        result = self._model.transcribe(str(audio_path), )
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_14(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        result = self._model.transcribe(str(None), **options)
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_15(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        full_text = None
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_16(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        full_text = result.get(None, "")
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_17(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        full_text = result.get("text", None)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_18(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        full_text = result.get("")
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_19(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        full_text = result.get("text", )
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_20(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        full_text = result.get("XXtextXX", "")
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_21(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        full_text = result.get("TEXT", "")
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_22(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        full_text = result.get("text", "XXXX")
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_23(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        detected_language = None
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_24(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        detected_language = result.get(None, "pt")
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_25(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        detected_language = result.get("language", None)
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_26(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        detected_language = result.get("pt")
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_27(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        detected_language = result.get("language", )
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_28(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        detected_language = result.get("XXlanguageXX", "pt")
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_29(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        detected_language = result.get("LANGUAGE", "pt")
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_30(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        detected_language = result.get("language", "XXptXX")
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_31(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        detected_language = result.get("language", "PT")
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_32(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        segments: list[Segment] = None
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_33(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        raw_segments = None
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_34(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        raw_segments = result.get("segments") and []
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_35(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        raw_segments = result.get(None) or []
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_36(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        raw_segments = result.get("XXsegmentsXX") or []
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_37(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        raw_segments = result.get("SEGMENTS") or []
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_38(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        max_end_time = None
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_39(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        max_end_time = 1.0
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_40(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            start = None
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_41(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            start = float(None)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_42(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            start = float(raw_seg.get(None, 0.0))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_43(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            start = float(raw_seg.get("start", None))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_44(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            start = float(raw_seg.get(0.0))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_45(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            start = float(raw_seg.get("start", ))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_46(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            start = float(raw_seg.get("XXstartXX", 0.0))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_47(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            start = float(raw_seg.get("START", 0.0))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_48(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            start = float(raw_seg.get("start", 1.0))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_49(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            end = None
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_50(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            end = float(None)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_51(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            end = float(raw_seg.get(None, 0.0))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_52(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            end = float(raw_seg.get("end", None))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_53(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            end = float(raw_seg.get(0.0))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_54(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            end = float(raw_seg.get("end", ))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_55(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            end = float(raw_seg.get("XXendXX", 0.0))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_56(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            end = float(raw_seg.get("END", 0.0))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_57(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            end = float(raw_seg.get("end", 1.0))
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_58(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            text = None
            
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_59(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            text = raw_seg.get(None, "").strip()
            
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_60(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            text = raw_seg.get("text", None).strip()
            
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_61(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            text = raw_seg.get("").strip()
            
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_62(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            text = raw_seg.get("text", ).strip()
            
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_63(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            text = raw_seg.get("XXtextXX", "").strip()
            
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_64(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            text = raw_seg.get("TEXT", "").strip()
            
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_65(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            text = raw_seg.get("text", "XXXX").strip()
            
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_66(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            
            if end >= max_end_time:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_67(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                max_end_time = None
            
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_68(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            avg_logprob = None
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_69(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            avg_logprob = raw_seg.get(None)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_70(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            avg_logprob = raw_seg.get("XXavg_logprobXX")
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_71(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            avg_logprob = raw_seg.get("AVG_LOGPROB")
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_72(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            if avg_logprob is None:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_73(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = None
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_74(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(None, 1.0)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_75(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(max(1.0 + float(avg_logprob), 0.0), None)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_76(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(1.0)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_77(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(max(1.0 + float(avg_logprob), 0.0), )
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_78(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(max(None, 0.0), 1.0)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_79(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(max(1.0 + float(avg_logprob), None), 1.0)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_80(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(max(0.0), 1.0)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_81(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(max(1.0 + float(avg_logprob), ), 1.0)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_82(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(max(1.0 - float(avg_logprob), 0.0), 1.0)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_83(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(max(2.0 + float(avg_logprob), 0.0), 1.0)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_84(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(max(1.0 + float(None), 0.0), 1.0)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_85(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(max(1.0 + float(avg_logprob), 1.0), 1.0)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_86(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = min(max(1.0 + float(avg_logprob), 0.0), 2.0)
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_87(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = None
            
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_88(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                confidence = 2.0
            
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_89(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                None
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_90(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                    start_seconds=None,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_91(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                    end_seconds=None,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_92(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                    text=None,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_93(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                    confidence=None
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_94(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_95(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_96(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_97(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_98(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        
        transcript = None
        
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_99(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            content_id=None,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_100(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            full_text=None,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_101(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            segments=None,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_102(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            language=None,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_103(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            model=None,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_104(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            duration_seconds=None
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_105(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_106(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_107(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_108(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_109(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_110(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_111(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path = None
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_112(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path = self.cache_dir * f"{content_id}.json"
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_113(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_payload = None
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_114(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "XXcontent_idXX": str(content_id),
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_115(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "CONTENT_ID": str(content_id),
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_116(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "content_id": str(None),
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_117(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "XXfull_textXX": transcript.full_text,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_118(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "FULL_TEXT": transcript.full_text,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_119(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "XXlanguageXX": transcript.language,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_120(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "LANGUAGE": transcript.language,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_121(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "XXmodelXX": transcript.model,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_122(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "MODEL": transcript.model,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_123(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "XXduration_secondsXX": transcript.duration_seconds,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_124(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "DURATION_SECONDS": transcript.duration_seconds,
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_125(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "XXsegmentsXX": [
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_126(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
            "SEGMENTS": [
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

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_127(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                    "XXstart_secondsXX": s.start_seconds,
                    "end_seconds": s.end_seconds,
                    "text": s.text,
                    "confidence": s.confidence
                }
                for s in transcript.segments
            ]
        }
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_128(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                    "START_SECONDS": s.start_seconds,
                    "end_seconds": s.end_seconds,
                    "text": s.text,
                    "confidence": s.confidence
                }
                for s in transcript.segments
            ]
        }
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_129(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                    "XXend_secondsXX": s.end_seconds,
                    "text": s.text,
                    "confidence": s.confidence
                }
                for s in transcript.segments
            ]
        }
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_130(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                    "END_SECONDS": s.end_seconds,
                    "text": s.text,
                    "confidence": s.confidence
                }
                for s in transcript.segments
            ]
        }
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_131(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                    "XXtextXX": s.text,
                    "confidence": s.confidence
                }
                for s in transcript.segments
            ]
        }
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_132(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                    "TEXT": s.text,
                    "confidence": s.confidence
                }
                for s in transcript.segments
            ]
        }
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_133(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                    "XXconfidenceXX": s.confidence
                }
                for s in transcript.segments
            ]
        }
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_134(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
                    "CONFIDENCE": s.confidence
                }
                for s in transcript.segments
            ]
        }
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_135(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(None, encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_136(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding=None)
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_137(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_138(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), )
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_139(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(json.dumps(None, indent=2, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_140(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(json.dumps(cache_payload, indent=None, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_141(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=None), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_142(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(json.dumps(indent=2, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_143(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(json.dumps(cache_payload, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_144(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_145(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(json.dumps(cache_payload, indent=3, ensure_ascii=False), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_146(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=True), encoding="utf-8")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_147(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding="XXutf-8XX")
        
        return transcript

    def xǁWhisperTranscriberAdapterǁtranscribe__mutmut_148(self, content_id: ContentId, audio_path: Path, language_hint: str | None = None) -> Transcript:
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
        cache_file_path.write_text(json.dumps(cache_payload, indent=2, ensure_ascii=False), encoding="UTF-8")
        
        return transcript
    
    xǁWhisperTranscriberAdapterǁtranscribe__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_1': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_1, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_2': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_2, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_3': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_3, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_4': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_4, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_5': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_5, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_6': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_6, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_7': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_7, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_8': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_8, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_9': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_9, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_10': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_10, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_11': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_11, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_12': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_12, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_13': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_13, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_14': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_14, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_15': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_15, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_16': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_16, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_17': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_17, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_18': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_18, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_19': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_19, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_20': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_20, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_21': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_21, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_22': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_22, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_23': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_23, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_24': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_24, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_25': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_25, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_26': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_26, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_27': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_27, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_28': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_28, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_29': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_29, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_30': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_30, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_31': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_31, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_32': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_32, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_33': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_33, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_34': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_34, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_35': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_35, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_36': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_36, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_37': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_37, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_38': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_38, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_39': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_39, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_40': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_40, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_41': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_41, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_42': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_42, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_43': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_43, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_44': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_44, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_45': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_45, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_46': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_46, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_47': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_47, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_48': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_48, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_49': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_49, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_50': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_50, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_51': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_51, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_52': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_52, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_53': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_53, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_54': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_54, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_55': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_55, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_56': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_56, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_57': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_57, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_58': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_58, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_59': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_59, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_60': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_60, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_61': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_61, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_62': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_62, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_63': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_63, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_64': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_64, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_65': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_65, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_66': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_66, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_67': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_67, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_68': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_68, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_69': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_69, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_70': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_70, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_71': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_71, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_72': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_72, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_73': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_73, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_74': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_74, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_75': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_75, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_76': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_76, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_77': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_77, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_78': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_78, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_79': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_79, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_80': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_80, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_81': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_81, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_82': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_82, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_83': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_83, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_84': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_84, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_85': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_85, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_86': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_86, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_87': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_87, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_88': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_88, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_89': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_89, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_90': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_90, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_91': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_91, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_92': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_92, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_93': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_93, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_94': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_94, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_95': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_95, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_96': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_96, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_97': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_97, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_98': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_98, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_99': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_99, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_100': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_100, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_101': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_101, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_102': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_102, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_103': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_103, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_104': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_104, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_105': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_105, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_106': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_106, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_107': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_107, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_108': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_108, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_109': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_109, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_110': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_110, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_111': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_111, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_112': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_112, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_113': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_113, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_114': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_114, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_115': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_115, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_116': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_116, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_117': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_117, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_118': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_118, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_119': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_119, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_120': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_120, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_121': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_121, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_122': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_122, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_123': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_123, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_124': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_124, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_125': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_125, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_126': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_126, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_127': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_127, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_128': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_128, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_129': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_129, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_130': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_130, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_131': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_131, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_132': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_132, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_133': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_133, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_134': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_134, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_135': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_135, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_136': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_136, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_137': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_137, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_138': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_138, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_139': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_139, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_140': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_140, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_141': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_141, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_142': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_142, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_143': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_143, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_144': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_144, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_145': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_145, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_146': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_146, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_147': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_147, 
        'xǁWhisperTranscriberAdapterǁtranscribe__mutmut_148': xǁWhisperTranscriberAdapterǁtranscribe__mutmut_148
    }
    xǁWhisperTranscriberAdapterǁtranscribe__mutmut_orig.__name__ = 'xǁWhisperTranscriberAdapterǁtranscribe'
