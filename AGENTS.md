# Doctor Stangler Method

> Default-active coding methodology for this workspace, executed by a committee of specialized agents.

## Activation

The orchestrator skill `doctor-stangler` ([SKILL.md](/.agents/skills/stangler/SKILL.md)) coordinates the committee and activates on **every coding task** by default — architecture, implementation, debugging, refactoring, testing, deployment, and any technical decision-making. The only exception is when the user explicitly asks to skip it.

Individual agent skills route specific tasks depending on the phase of the development lifecycle:
- **Phase 0: Angiography** ([SKILL.md](/.agents/skills/stangler-angiography/SKILL.md)) — Code archaeology and legacy reverse-engineering.
- **Phase 1: Stereoscopy** ([SKILL.md](/.agents/skills/stangler-stereoscopy/SKILL.md)) — Strategic vision and ADR drafting.
- **Phase 2: Refractometry** ([SKILL.md](/.agents/skills/stangler-refractometry/SKILL.md)) — Precision test specifications.
- **Phase 3: Surgery** ([SKILL.md](/.agents/skills/stangler-surgery/SKILL.md)) — High-performance TDD execution.
- **Phase 4: Treatment** ([SKILL.md](/.agents/skills/stangler-treatment/SKILL.md)) — Mutation testing and quality post-op treatment.

## Core Protocol

**ADR-First.** Every implementation begins with an Architectural Decision Record. Specs are consequences of the ADR. Implementation plans are consequences of specs. No implementation plan without specs. No specs without ADR.

The Five-Phase Execution Cycle: **Angiography (Phase 0) → Stereoscopy (Phase 1) → Refractometry (Phase 2) → Surgery (Phase 3) → Treatment (Phase 4)**. No functional code without architect approval at each gate.
