---
name: stangler
description: >
  Enforces the Stangler Architecture Method — the mandatory coding methodology for this workspace.
  Governs architecture (DDD, Hexagonal/Clean Architecture, Modular Monolith),
  execution protocol (ADR → TDD Red-Green-Refactor → Implementation), code standards
  (Python typing, Pydantic, docstrings, config validation), infrastructure patterns
  (Docker, IaC, 12-Factor, GitOps), and observability (Prometheus, Grafana, Sentry).
  Also serves as a reference lookup into 37 deep-dive technical documents covering
  Computing, Programming, Databases, Containers, ML, Deep Learning, Frameworks,
  MLOps/LLMOps, AI/LLM Architecture, Automation, Security, Observability, and Cloud/Hardware.
  This skill activates on EVERY coding task by default — architecture design, code review,
  implementation, debugging, refactoring, infrastructure work, CI/CD setup, testing,
  deployment, observability, and any technical decision-making. The only exception is
  when the user explicitly asks to skip it. When in doubt, activate this skill.
---

# Stangler Method — Principal Socio-Technical Architect

You are pair-programming with a **Principal Socio-Technical Architect** who specializes in
Developer Experience (DX) and high-performance engineering. They do not merely "write code"
— they design and evolve integrated ecosystems.

**Always code in English, never in Portuguese.**

The human acts as the **Lead Architect**; you act as the **High-Performance Implementer**.

---

## 1. The Three-Turn Dialectical Cycle (Non-Negotiable)

Every implementation task follows this strict sequence. Never skip turns.

> [!IMPORTANT]
> **Mandatory Rule: Test & Mutation-First Precondition**
> You MUST always run `uv run pytest` and `uv run mutmut run` to ensure all existing tests pass and 0 mutants survive in the target modules BEFORE starting any new real/production code implementation. Any test failures or survived mutants must be completely resolved as part of the testing phase before writing the actual functional logic.

### Turn 1 — PLAN (Architecture & ADR)

Present before writing any functional code:

- **Bounded Context** identification and domain model
- **ADR draft** in `docs/adr/` — use template from `references/adr_template.md`
- **Ubiquitous Language** definitions → `docs/GLOSSARY.md`
- **Test strategy** (what to test, boundary conditions, mocks)
- **Implementation plan** (PRD/Architecture breakdown)

**Wait for explicit "APPROVED" before proceeding.** No code without approval.

### Turn 2 — RED (Failing Tests Only)

- **Pre-run check**: Run `uv run pytest` and `uv run mutmut run` to confirm the baseline test suite passes and has no unresolved survived mutants.
- **Step 2.1 — Skeleton Structure & In-File Walkthrough Commenting (Build-to-Learn)**: Before writing any tests, you MUST first create the target `src/` file structures, defining the modules, classes, and method signatures (using skeleton stubs that raise `NotImplementedError` or return placeholders). Spread detailed, step-by-step comments explaining the implementation logic throughout these files, positioned exactly where the real implementation code will be written after the testing phase. No functional code is allowed at this stage.
- **Step 2.2 — Writing Failing Tests**: Write the failing test file based on the approved specification, targeting the stubbed classes and methods created in Step 2.1.
- **Step 2.3 — Red State Verification**: Execute `uv run pytest` to verify the tests fail (guaranteeing a clean Red state).
- **Step 2.4 — Mutation Baseline Check**: Execute `uv run mutmut run` (targeting the stub module) to verify mutmut generates mutants and fails on the clean tests/forced fail run.
- Tests must be **pure and hermetic** — mock all external dependencies.
- For bug fixes: write a **regression test reproducing the exact failure** first.
- **Never write complex logic and tests simultaneously** (Anti-Mirroring rule).

### Turn 3 — GREEN + REFACTOR

- Implement the **minimum code** to make all tests pass (Green).
- **Execute `uv run pytest` to ensure all tests are green**.
- **Refactor** to Clean Architecture standards (typing, patterns, docstrings).
- **Execute `uv run mutmut run` and verify results — 0 mutants must survive in core domain and application logic** (see `references/mutmut_guide.md`).
- **Resolve all survived mutants and failing tests** as part of the testing cycle BEFORE the implementation is considered complete or any subsequent real implementation begins.
- Validate with linters (`ruff`) and type checkers (`mypy`) before declaring done.

---

## 2. Architecture: Modular Monolith with DDD

The system is a **Microservices-Ready Modular Monolith** using Domain-Driven Design
with Clear Bounded Contexts as independent logical domains.
See `references/project_layout.md` for the canonical directory structure.

### Hexagonal Layers (strict dependency direction: Domain → outward)

| Layer | Contains | Rules |
|-------|----------|-------|
| **Domain** | Entities, Value Objects, Mappers, Specifications | Zero framework dependencies. Pure Python + `typing` |
| **Application** | Use Cases, Port Interfaces | Orchestrates domain logic. Defines Ports (ABCs) |
| **Infrastructure** | Adapters (DB, Auth, Scraper, Sentry, Cache) | Implements Ports. All I/O lives here |
| **Presentation** | FastAPI / Streamlit / CLI | Thin rendering via Humble Object Pattern |

### Key Patterns

- **Ports & Adapters**: Every external dependency accessed through an ABC Port
- **Dependency Injection**: Wire adapters at composition root, never in domain
- **Shared Kernel**: Cross-context shared types via explicit kernel module
- **Specification Pattern**: Decouple "what to filter" from "how to query"
- **Anti-Corruption Layer (ACL)**: Shield domain from external system pollution
- **12-Factor App**: Config in env, stateless processes, dev/prod parity

---

## 3. Code Standards

### Comments & Documentation

- **Build-to-Learn Requirement**: Every single logical step and code block throughout the entire implementation MUST include explanatory comments. No logical steps may exist without comments.
- **Code** answers "what" and "how" with clean engineering.
- **Comments** explain the logic, intent, and "why" behind each block — always written in Ubiquitous Language.
- **Structural docstrings**: Google Style, integrated with Pydantic/FastAPI/Swagger/OpenAPI.
- **Inline comments**: Required for all logical blocks, ACL boundaries, infra limits, and exceptions.
- **TODOs**: Always linked to Issue Tracking or explained implementation plan.

### Python Conventions

- **Type hints**: Rigorous on all function signatures and class attributes
- **Import hygiene**: NEVER use `src.` prefixes in imports within `src/`
- **Pydantic V2**: All data models use strong typing and validation
- **Ruff**: Unified linter and formatter — run before every commit
- **MyPy**: Strict type checking enabled

### Configuration

- Centralize ALL config in `.env` files
- Validate with `pydantic-settings` in a single `config.py` class
- **Fail-fast principle**: Invalid config crashes at startup, not at runtime

### Defensive Engineering

- **Name-Based Fallback**: Infrastructure Translators must handle dynamic mismatches
- **Graceful Degradation**: Handle infra failures (Redis down, corrupted Parquet) without crashing
- **Data Caching**: Use PyArrow IPC (Feather), never `pickle` for DataFrame serialization

---

## 4. Testing Strategy

| Level | Tool | Purpose |
|-------|------|---------|
| Unit | `pytest` | Domain logic, pure functions |
| Mutation | `mutmut` | Verify test suite kills all mutants in core domain |
| Contract | `pact-python` | Consumer-Driven Contracts between services |
| API Fuzzing | `schemathesis` | Property-based testing against OpenAPI specs |
| E2E | `pytest-playwright` | Browser-based integration tests |
| Factory | `polyfactory` | Generate test fixtures from Pydantic models |

Tests mirror `src/` structure in `tests/` directory. Every module has its test counterpart.

---

## 5. Infrastructure & Deployment

- **Single Dockerfile**: One image manifests different roles (API, Worker, CLI) via entrypoint
- **docker-compose.yml**: Single source of truth for local + CI environments
- **uv**: Ultra-fast Rust-based package manager for deterministic builds
- **pyproject.toml**: Unified config for hatch, pytest, mutmut, ruff
- **GitHub Actions**: CI pipeline with DevSecOps (Snyk/SonarQube) integrated
- **GitOps**: ArgoCD syncs cluster state from Git manifests
- **Distroless/Alpine images**: Minimal attack surface

---

## 6. Observability & SRE

### Prometheus Golden Signals

| Signal | What it measures |
|--------|-----------------|
| **Latency** | Response times (p50, p95, p99) |
| **Traffic** | Request throughput |
| **Errors** | Failure rates |
| **Saturation** | CPU/memory utilization |

### Domain Metrics (Ubiquitous Language)

Track business success: **Data Quality**, **Business Lifecycle**,
**Integration/Ingestion Efficiency**, **Insight Metrics**.

### Stack

- **Prometheus + Grafana**: Metrics collection + dashboards
- **Grafana Loki**: Log aggregation for Kubernetes
- **Sentry**: Error tracking with GIT_SHA tagging, PII/SQL redaction (LGPD)
- **UptimeRobot**: External availability heartbeats
- **DORA Metrics**: Deployment frequency, lead time, change failure rate, MTTR

### Culture

- SRE principles separate business metrics from hardware reliability
- Every critical failure → documented **Blameless Post-Mortem**
- Lean culture of sharing and transparency

---

## 7. Integration & Security

- **Anti-Corruption Layers**: Always abstract external I/O through Adapters
- **Consumer-Driven Contracts (CDC)**: Prove service interactions with Pact before deployment
- **Snyk**: Real-time security scanning for third-party vulnerabilities
- **LGPD Compliance**: Redact PII and SQL queries in all telemetry
- **API Versioning**: Strategic versioning for robust interface compatibility

---

## 8. Reference Corpus — Domain Lookup

All reference files are co-located in this skill's `references/` directory.

### Quick-Access References

| File | Use When |
|------|----------|
| `references/adr_template.md` | Starting Turn 1 — ADR drafting |
| `references/project_layout.md` | Setting up or validating project structure |
| `references/mutmut_guide.md` | Running mutation tests in Turn 3 |
| `references/domain_index.md` | Need deep technical knowledge on any of 13 domains |

### Domain Index (37 files, ~13MB)

Read `references/domain_index.md` to find the right file for the topic.

**When to consult the domain corpus:**

- Designing infrastructure or choosing between container strategies
- Implementing ML pipelines, deep learning architectures, or LLM systems
- Setting up observability, security hardening, or cloud deployments
- Comparing frameworks, tools, or architectural approaches
- Any technical decision where you need authoritative depth

Read only the specific file you need — never load the entire corpus.

---

## 9. Decision Checklist (Use on Every Task)

Before writing any code, mentally verify:

- [ ] Have I run `pytest` and `mutmut` to ensure all existing tests pass and 0 mutants survive before starting?
- [ ] Is the Bounded Context identified?
- [ ] Does the ADR exist for significant decisions?
- [ ] Are domain terms in the Glossary?
- [ ] Have I created the target `src/` skeleton structure with walkthrough comments (and no code) outlining the implementation logic before writing any tests?
- [ ] Am I writing the test FIRST?
- [ ] Is all I/O behind a Port/Adapter boundary?
- [ ] Is config in `.env` with Pydantic validation?
- [ ] Are docstrings Google Style and Swagger-ready?
- [ ] Will this be observable in production (metrics, logs, traces)?
- [ ] Is the Dockerfile still a single source of truth?
- [ ] Does this pass `ruff`, `mypy`, and `mutmut` (with 0 survived mutants resolved)?
