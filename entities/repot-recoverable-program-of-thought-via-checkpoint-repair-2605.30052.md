---
title: "REPOT: Recoverable Program-of-Thought via Checkpoint Repair"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [program-of-thought, agent-debugging, declarative-lm, primitive-class-declarative-lm-program]
sources: ["https://arxiv.org/abs/2605.30052"]
---

# REPOT: Recoverable Program-of-Thought via Checkpoint Repair

## Overview
Introduces RePoT (Recoverable PoT), a deterministic verified-replay primitive that walks a one-shot Program-of-Thought trajectory through the environment to its first invalid transition, then makes a single LLM call that resumes from the verified prefix — at most one extra LLM call on the ~14% of problems where PoT fails. Beats PoT by +3 to +11pp across four closed-model configurations on PuzzleZoo-775 and peaks at 96.9% vs 86.3% on gpt-5.4-mini-medium; introduces Adaptive RePoT, a rule-based dispatcher that routes between suffix repair and a fresh PoT retry based on verified-prefix length.

## Key Facts
- **Authors**: Mazaheri, Parsa
- **Year**: 2026
- **arXiv**: [2605.30052](https://arxiv.org/abs/2605.30052)

## Key Contributions
- **Deterministic verified-replay primitive for PoT trajectories**: RePoT walks the PoT-emitted Python program through the environment to its first invalid transition, then resumes with one LLM call from the verified prefix — the **first checkpoint-repair primitive for PoT trajectories** in the wiki.
- **Adaptive RePoT dispatcher**: rule-based dispatcher that routes between suffix repair and a fresh PoT retry based on verified-prefix length, exhibiting a capability-scaling pattern (suffers on weaker models, wins on stronger ones).
- **Capability-scaling characterization**: +3.8pp on Gemini (95% CI [+2.2, +5.4]) against matched-budget PoT-retry baseline, within sampling noise on GPT-medium and Claude, loses on GPT-mini — surfaces a capability-scaling primitive for recovery vs retry trade-offs.
- **Generalization across benchmarks**: replicates on PlanBench Blocksworld (+1.1 to +11.4pp) and four open-weights models (+3.3 to +20.0pp on three of four), and on Derail-550 every condition with access to checkpoint information improves over PoT.

## Related Papers
- [[calvert-augmenting-agents-with-calibrated-verifier-telemetry-improves-action-and-learning-in-knowledge-intensive-tasks-2606.21777]] — Sibling paper on calibrated verifier telemetry for agent action/learning — orthogonal primitive for verifier-driven agent improvement.
- [[agentic-reasoning-for-large-language-models-2601.12538]] — Sibling survey on agentic reasoning primitives — provides the broader primitive landscape that this paper's PoT-checkpoint-repair complements.
- [[meta-cognitive-memory-policy-optimization-for-long-horizon-llm-agents-2605.30159]] — Sibling paper that surfaces meta-cognitive-memory-policy as the long-horizon agent primitive — orthogonal to checkpoint-repair primitive for PoT.
- [[where-do-deep-research-agents-go-wrong-span-level-error-localization-in-agent-trajectories-2606.02060]] — Sibling paper that surfaces span-level error localization for agent trajectories — orthogonal primitive for trajectory-level failure analysis.