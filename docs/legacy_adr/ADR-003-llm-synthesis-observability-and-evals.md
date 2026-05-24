# ADR-003: LLM Synthesis Observability and Evals

**Status:** Proposed
**Date:** 2026-05-23
**Decision Makers:** Lead Architect, High-Performance Implementer

## Context

The Knowledge bounded context utilizes a local large language model (Ollama with `qwen2.5:7b`) to synthesize raw transcripts into structured second brain wiki articles. Because LLM outputs are inherently non-deterministic, we face two main risks:
1. **Silent Drift/Regression:** Updates to prompt templates, local model versions, or source context could degrade synthesis quality without crashing the pipeline.
2. **Telemetry Blindness:** The lack of distributed tracing makes debugging synthesis latency, prompt effectiveness, and system errors difficult in production.

Under the Doctor Stangler Method, any generative AI workflow requires a strict **Langfuse Ingestion Strategy** and a pre-designed **Eval Matrix** before deployment.

## Decision

We will integrate Langfuse tracing and evaluate synthesis quality using a structured Eval Matrix.
- All synthesis runs will emit telemetry traces to Langfuse using a defined trace taxonomy and span hierarchy.
- Synthesized output schemas will be validated against a golden dataset using LLM-as-judge evaluations, preventing regressions.

## Langfuse Ingestion Strategy

We will initialize the Langfuse client inside `OllamaLLMAdapter` and wrap generative calls inside trace spans.

### 1. Trace Taxonomy
- **Trace Name:** `WikiSynthesis`
- **Trace ID:** Map directly to the unique internal `ContentId` (UUIDv4) associated with the media episode.
- **Session ID:** Map directly to the `ContentId` to group all processing stages (Ingestion -> Transcription -> Synthesis) under the same session.
- **User ID:** Map to the `channel_name` or `creator` from metadata as the business context tenant.
- **Tags:** Tag each run with `['isb-synthesis', settings.ENV, settings.OLLAMA_MODEL]`.

### 2. Span Hierarchy
- **Parent Trace:** `WikiSynthesis`
  - **Generation Span:** `OllamaSynthesisGeneration`
    - Wraps the raw Ollama HTTP API post request.
    - Captures the exact prompt string input, response output, model settings, temperature, and tokens/latency statistics.

### 3. Prompt Version Tracking
- **Prompt Name:** `wiki_synthesis_v1`
- **Prompt Version:** `1.0`
- **Governance:** The prompt layout will be registered in Langfuse Prompt Registry. In local offline modes, the version string will be sent along with the metadata block to track template changes.

### 4. Score Schema
We will calculate scores in Langfuse using automated evaluation judges:
- `faithfulness`: Matches facts present in the raw transcript note [0.0 to 1.0].
- `relevance`: Measures alignment with metadata classification [0.0 to 1.0].
- `hallucination`: Checks if claims not present in source note exist [0.0 to 1.0].

---

## Eval Matrix

To guarantee prompt and model updates do not introduce silent regression, we establish the following evaluation rules:

| Output Dimension | Evaluation Method | Threshold Score | Dataset Source | Blocking Policy |
|------------------|-------------------|-----------------|----------------|-----------------|
| **Faithfulness** | LLM-as-judge (comparison prompt) | `faithfulness >= 0.85` | `tests/resources/golden_dataset.json` | Pipeline breaks (fails build in CI) |
| **Relevance** | Embedding similarity / LLM-as-judge | `relevance >= 0.80` | `tests/resources/golden_dataset.json` | Log warning |
| **Hallucination** | Rule-based entity matching & LLM | `hallucination <= 0.10` | `tests/resources/golden_dataset.json` | Pipeline breaks (fails build in CI) |

---

## Consequences

### Positive
- **Deep Visibility:** Allows monitoring token usage, latencies, and generation quality trends on the Langfuse Dashboard.
- **Continuous Guardrails:** Regression tests in the CI pipeline fail automatically if model edits reduce faithfulness or introduce hallucinations.

### Negative
- **Network Overhead:** Generation calls require reporting spans to the Langfuse HTTP host, introducing slight network logging overhead (handled asynchronously by Langfuse client daemon threads).

### Neutral
- Offline local development can bypass Langfuse reporting when API credentials are omitted in `.env`, falling back to standard console logging.

## Alternatives Considered

### Alternative A: Custom SQLite Logging Database
- **Pros:** Completely offline, no third-party cloud service dependency.
- **Cons:** Missing GUI for visualization, session tracing, prompt version comparisons, and LLM-as-judge score evaluations.
- **Why rejected:** Building custom evaluation pipelines and GUIs replicates features already provided by Langfuse, violating the KISS principle.

## Compliance

- [x] Hexagonal Architecture layers respected
- [x] No framework dependencies in Domain layer (Pydantic model validation only)
- [x] Tests strategy defined (Eval Matrix checking golden dataset outputs)
- [x] Observability plan included (Langfuse generation spans)
- [x] LGPD/Security implications assessed (Redaction of potential PII in transcripts before sending to external endpoints)

## References

- DevOps & DDD Specification: `references/37-DevOps, DDD, TDD, ADRs, Code.md`
- Project layout guideline: `references/project_layout.md`
