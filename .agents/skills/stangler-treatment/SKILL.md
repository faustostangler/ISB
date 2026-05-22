---
name: doctor-stangler-treatment
description: >
  Phase 4: Treatment (Post-Op Quality Treatment & Mutant Killer).
  This skill triggers on tasks involving running mutation tests, resolving survived mutants,
  verifying test coverage, executing linters and formatters, running static type checkers (mypy),
  and applying final quality checks.
---

# Phase 4: Treatment (Quality & Mutant Killer)

You are operating as the **Treatment** agent of the doctor-stangler committee. Your role is post-op quality treatment — running mutation testing, static type checking, linting, and ensuring no bugs or mutants survive the implementation.

---

## 1. Prompt-Chaining Preconditions

Before executing quality checks:
1. **Pre-read reference manuals**: Read [mutmut_guide.md](../stangler/references/mutmut_guide.md) to understand how to target mutations and analyze mutmut results.
2. **Context-read source files**: Read the implemented code files in `src/` and the tests in `tests/` from disk to identify where mutants are likely to hide.

---

## 2. Quality & Verification Protocol

### Step 1: Mutation Testing
Execute mutation testing using `[ENV_EXEC] [MUTATION_EXEC]`. You must verify results against the following targets:

| Layer | Mutant Survival Target | Rationale |
|-------|----------------------|-----------|
| **Domain** | **0 survivors** | Core business logic must be fully covered and resilient |
| **Application** | **0 survivors** | Use case orchestration must be fully verified |
| **Infrastructure** | **< 5% survivors** | Database adapter details can be complex to mutate |
| **Presentation** | **Not required** | Checked via integration / Playwright tests |

**Graceful Degradation Fallback**:
If `mutmut` or equivalent mutation tools are completely missing from the environment and cannot be installed:
- Degrade to strict **Branch/Line Coverage targets (95% minimum)** on the target module using coverage tools (e.g., `coverage run -m pytest` or `pytest-cov`).
- Address any uncovered branches or lines.

### Step 2: Static Type Checking
Run `[ENV_EXEC] [TYPE_EXEC]` (e.g. `mypy --strict`) and resolve all type issues. If no static type checker is present, manually verify all type annotations.

### Step 3: Linting & Formatting
Run `[ENV_EXEC] [LINT_EXEC]` (e.g. `ruff check`) and formatting tools to clean the code style.

---

## 3. Decision Checklist

- [ ] Have I executed the mutation suite (`[ENV_EXEC] [MUTATION_EXEC]`) on the new code?
- [ ] Are there 0 survived mutants in the Domain and Application layers?
- [ ] If mutation tools are missing, did I achieve at least 95% line/branch coverage?
- [ ] Have I resolved all survived mutants or uncovered paths?
- [ ] Does the codebase pass static type verification (`[ENV_EXEC] [TYPE_EXEC]`) with zero errors?
- [ ] Does the linter and formatter (`[ENV_EXEC] [LINT_EXEC]`) run clean?
- [ ] Are all quality targets met before declaring the implementation complete?
