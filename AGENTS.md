# Stangler Method

> Default-active coding methodology skill for this workspace.

## Activation

The `stangler` skill (`.agents/skills/stangler/SKILL.md`) activates on **every coding task** by default — architecture, implementation, debugging, refactoring, testing, deployment, and any technical decision-making. The only exception is when the user explicitly asks to skip it.

## Core Protocol

**ADR-First.** Every implementation begins with an Architectural Decision Record. Specs are consequences of the ADR. Implementation plans are consequences of specs. No implementation plan without specs. No specs without ADR.

The Four-Phase Execution Cycle: **ADR → Specs → Red (failing tests) → Green + Refactor (implementation)**. No functional code without architect approval at each gate.
