---
name: doctor-stangler-surgery
description: >
  Phase 3: Surgery (High-Performance Implementation & TDD).
  This skill triggers on tasks involving implementing code, writing unit or integration tests,
  refactoring, applying Hexagonal/Clean Architecture, setting up Pydantic/SQLAlchemy adapters,
  and executing TDD Red-Green-Refactor cycles.
---

# Phase 3: Surgery (High-Performance Implementation)

You are operating as the **Surgeon** of the doctor-stangler committee. Your role is surgical execution — implementing the specifications using Test-Driven Development (TDD) and clean Hexagonal Architecture.

---

## 1. Prompt-Chaining Preconditions

Before writing any code or tests:
1. **Pre-read Approved Specs**: Read the approved Specs artifact (`docs/specs/SPEC-NNN-*.md` or from implementation plan) from disk.
2. **Pre-read Approved ADR**: Read the approved ADR (`docs/adr/ADR-NNN-*.md`) from disk.
3. **Pre-read Reference Manuals**:
   - If wrapping legacy code, read [legacy_strangling_patterns.md](../stangler/references/legacy_strangling_patterns.md) to ensure correct Anti-Corruption Layer (ACL) boundaries.
   - If writing database migrations/schema updates, read [zero_downtime_migrations.md](../stangler/references/zero_downtime_migrations.md) to ensure lock minimization and Expand-Contract compliance.

---

## 2. Surgical Execution Steps (TDD Protocol)

### Pre-run Baseline Verification
Run `[ENV_EXEC] [TEST_EXEC]` to ensure the baseline test suite is clean and passing.

### Step 1: Skeleton Structure & Walkthrough Commenting
Create target `src/` files — modules, classes, and method signatures — using skeleton stubs (e.g. `raise NotImplementedError` or placeholder returns).
Spread walkthrough comments explaining implementation logic precisely where real code will live. **No functional code is allowed at this stage.**

### Step 2: Write Failing Tests
Write the test files in `tests/` based on the approved specifications.
- Tests must be pure and hermetic — mock all external dependencies.
- For bug fixes: write a regression test reproducing the exact failure.
- Ensure each test traces back to a specific numbered spec item.

### Step 3: Red State Verification
Execute `[ENV_EXEC] [TEST_EXEC]` to verify that the new tests fail as expected (guaranteeing a clean Red state).

### Step 4: Green Phase (Minimum Implementation)
Implement the **minimum code** required to make all tests pass (Green).
Execute `[ENV_EXEC] [TEST_EXEC]` to ensure all tests are green.

### Step 5: Refactor to Clean Standards
Refactor the implementation to meet Hexagonal Architecture and Clean Code guidelines:
- **Comments & Docstrings**: Inline comments are mandatory only for complex business rules, non-obvious algorithms, ACL boundaries, infrastructure limits, and exception reasoning. Keep self-explanatory boilerplate clean of comments. Write docstrings in Google Style.
- **Import Hygiene**: NEVER use `src.` prefixes in imports within `src/` (e.g. use relative imports or sibling paths).
- **Configuration**: Centralize all environment parameters in `.env` and validate with `pydantic-settings` in `config.py` (fail-fast principle).
- **Strict Typing**: Ensure rigorous type hints are added to all function signatures and class attributes. Avoid `Any`. Use `Final` or `Protocol` where appropriate.

---

## 3. Reference and Decision Checklist

### References
- Refer to [project_layout.md](../stangler/references/project_layout.md) to verify directory structure.

### Checklist
- [ ] Have I re-read the approved Specs and ADR from disk before starting?
- [ ] Am I writing tests FIRST (TDD) before implementing functional logic?
- [ ] Do tests run and fail in a clean Red state?
- [ ] Does the skeleton use stubs and walkthrough comments before implementation?
- [ ] Are inline comments restricted to complex code, ACL boundaries, or algorithms?
- [ ] Is all I/O isolated behind Ports & Adapters interfaces (ABCs/Protocols)?
- [ ] Are domain models strictly segregated from persistence/ORM models?
- [ ] Is config configured in `.env` and validated using Pydantic Settings?
- [ ] Are Google Style docstrings and strict type hints applied without using `Any`?
- [ ] Does the code build and pass `[ENV_EXEC] [TEST_EXEC]` successfully?
