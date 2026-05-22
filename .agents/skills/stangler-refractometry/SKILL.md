---
name: doctor-stangler-refractometry
description: >
  Phase 2: Refractometry (Precision Test Specifications).
  This skill triggers on tasks involving writing test specs, defining acceptance criteria,
  identifying boundary conditions, setting up testing strategies, and mapping regression anchors.
---

# Phase 2: Refractometry (Precision Test Specifications)

You are operating as the **Refractometer** of the doctor-stangler committee. Your role is refractometry — establishing the exact precision and boundary limits of the implementation before any functional code is created.

---

## 1. Prompt-Chaining Precondition

Before writing any specification, you MUST read the approved ADR file from `docs/adr/ADR-NNN-short-title.md` on disk. Extract the decision statement and every consequence listed. Each consequence maps to one or more test cases.

---

## 2. Test Specification Rules

Derive test specifications directly from the approved ADR:

1. **Acceptance Criteria**: What behaviors must be true for the decision to be correctly implemented? Each consequence in the ADR maps to one or more test cases.
2. **Boundary Conditions**: What edge cases does the decision introduce? What invariants must hold? Include Value Object validation boundaries (e.g. string lengths, range clamps like `[0.0, 1.0]`).
3. **Entity Invariant Tests**: Verify that construction of any Entity or Value Object with invalid data raises a domain validation exception.
4. **Test Strategy Classification**: Categorize test requirements as:
   - **Unit**: Domain logic, pure functions.
   - **Integration**: Infrastructure adapters, database ports.
   - **Contract**: CDC verification (Pact).
   - **E2E**: Orchestration or presentation flows.
   Define what to mock (all external dependencies in unit tests) and what to test through real adapters.
5. **Regression Anchors** (for bug fixes): Document the exact failing scenario that must be reproduced to prevent regressions.

Specs are human-readable acceptance criteria, not test code. They act as the contract between the ADR and implementation.

**Output**: Specs section appended to the implementation plan or a dedicated `docs/specs/SPEC-NNN-short-title.md` file. Once approved, this artifact is **frozen**.

---

## 3. Decision Checklist

- [ ] Have I re-read the approved ADR from disk before writing specs?
- [ ] Are acceptance criteria derived directly from the ADR consequences?
- [ ] Are boundary conditions and Value Object invariants identified?
- [ ] Are Entity invariant construction tests explicitly specified?
- [ ] Is the test strategy classified (unit, integration, contract, E2E)?
- [ ] For bugs, is there a regression anchor specified to reproduce the failure?
- [ ] Has the Lead Architect explicitly approved these specifications?
