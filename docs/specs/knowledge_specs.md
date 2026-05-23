# Knowledge Bounded Context Specifications

This document defines the formal behavioral specifications, boundaries, and invariants for the Knowledge Bounded Context.

---

## 1. Value Object Invariants

### NoteTitle
- **Description:** A sanitized, filesystem-safe note title.
- **Constraints:**
  - Must be a string.
  - Characters `\`, `/`, `:`, `*`, `?`, `"`, `<`, `>`, `|` must be replaced by space.
  - Resulting string must not contain consecutive spaces or consist solely of whitespace.
- **Test Scenarios:**
  - `Note: Title *Test*` is sanitized to `Note Title Test`.
  - Empty string raises `ValueError`.

### ArticleContent
- **Description:** The synthesized Markdown body content.
- **Constraints:**
  - Must be a string.
  - Length must be at least 10 characters (excluding padding).

### ArticleTag
- **Description:** A normalized taxonomy tag.
- **Constraints:**
  - Must contain only lowercase alphanumeric characters.
  - Whitespaces and special characters are stripped.
- **Test Scenarios:**
  - `AI-Deep_Learning!` is normalized to `aideeplearning`.

### ArticleBacklink
- **Description:** An Obsidian-style double bracketed wiki cross-link.
- **Constraints:**
  - Must start with `[[` and end with `]]`.
  - Content inside brackets must not be empty or whitespace.
- **Test Scenarios:**
  - `[[Neural Networks]]` is valid.
  - `[Neural Networks]` or `[[]]` raises `ValueError`.

---

## 2. Entity Invariants

### RawNote
- **Rules:**
  - `content_id` is a valid ContentId.
  - `title` is a valid NoteTitle.
  - `transcript_text` is a valid TranscriptText.
  - `metadata` is a valid NoteMetadata Pydantic model.
  - `to_obsidian_markdown()` generates valid Markdown file starting with YAML frontmatter bounded by triple hyphens (`---`).

### WikiArticle
- **Rules:**
  - `article_id` is a valid ContentId.
  - `title` is a valid NoteTitle.
  - `content` is a valid ArticleContent.
  - `tags` is a list of ArticleTag.
  - `backlinks` is a list of ArticleBacklink.
  - `source_notes` is a list of ContentId.
  - `to_obsidian_markdown()` outputs frontmatter containing string lists for `tags` and `backlinks`.

---

## 3. Obsidian Vault Layout

To maintain organization, the Obsidian Vault must be laid out in structured subdirectories:
- `00-Raw/`: Contains raw source transcript captures. Filename is `{NoteTitle}.md`.
- `10-Wiki/`: Contains synthesized wiki articles. Filename is `{NoteTitle}.md`.

---

## 4. LLM Eval Matrix

Non-deterministic outputs from the LLM adapter are checked against a golden evaluation dataset (`tests/resources/golden_dataset.json`) containing reference inputs and expected answers.

| Evaluation Metric | Target Threshold | Method | Blocking Policy |
|--------------------|------------------|--------|-----------------|
| **Faithfulness** | `score >= 0.85` | LLM-as-judge comparing facts to raw transcript | Fails CI pipeline |
| **Relevance** | `score >= 0.80` | Embedding similarity / LLM-as-judge | Logs Warning |
| **Hallucination** | `score <= 0.10` | LLM-as-judge verifying no unsupported claims | Fails CI pipeline |
