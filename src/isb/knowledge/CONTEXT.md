# Knowledge Bounded Context Glossary

This glossary contains the Ubiquitous Language terms for the Knowledge Bounded Context.

## Terms

### RawNote
* **Definition**: An Obsidian note containing the verbatim `Transcript` and associated metadata frontmatter. Matches the **Raw Layer** of the LLM Wiki architecture.
* **Rules**: Written in the `00-Raw/` directory inside the vault.

### WikiArticle
* **Definition**: An LLM-synthesized, cross-referenced Obsidian article compiling intelligence from one or more `RawNote` instances. Matches the **Wiki Layer** of the LLM Wiki architecture.
* **Rules**: Written in the `10-Wiki/` directory inside the vault.

### SchemaRule
* **Definition**: Structural constraint declarations (using Pydantic V2 models) defining formatting, metadata, and cross-linking rules for `WikiArticle` generation. Matches the **Schema Layer** of the LLM Wiki architecture.
* **Rules**: Code-enforced during synthesis, and written as markdown template definitions under `02-Schema/`.

### KnowledgeStatus (Local Lifecycle)
* **Definition**: The status tracked by Knowledge locally to manage its synthesis tasks:
  * `PENDING`: Verbatim transcript has been received but synthesis hasn't started.
  * `SYNTHESIZING`: LLM is running note synthesis and Obsidian note/wiki compilation is active.
  * `COMPLETED`: Note and wiki article have been successfully committed to Obsidian.
  * `FAILED`: Synthesis, Obsidian file writing, or LLM schema validation failed.

