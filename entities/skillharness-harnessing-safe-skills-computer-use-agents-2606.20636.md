---
title: "SkillHarness: Harnessing Safe Skills for Computer-Use Agents"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [computer-use-agents, skill-curation, safety, continual-learning, agent-safety]
sources: ["https://arxiv.org/abs/2606.20636"]
---

# SkillHarness: Harnessing Safe Skills for Computer-Use Agents

## Overview
Chen, Yi, Yin, and Zhang argue that Computer-Use Agents (CUAs) deployed in dynamic interactive environments face a structural safety-versus-learning trade-off that static skill abstractions cannot resolve — agents that learn new skills at deployment time (continual skill learning) accumulate behavioral surface area faster than static allowlists or pre-deployment audits can evaluate, while agents that restrict themselves to pre-vetted skills freeze their capability growth. They propose SkillHarness, a framework that models skill learning and utilization as a safety-constrained interaction process in which every skill invocation is gated by a runtime safety evaluator against the current environment state, surfacing *safety-constrained skill interaction* as the load-bearing primitive for the continual-skill-learning deployment regime.

## Key Facts
- **Authors**: Yurun Chen, Biao Yi, Keting Yin, Shengyu Zhang
- **Year**: 2026
- **arXiv**: [2606.20636](https://arxiv.org/abs/2606.20636)
- **Subjects**: cs.AI, cs.CL
- **Submitted**: 2026-06-02

## Key Contributions
- Identifies a structural capability-versus-safety trade-off in continual skill learning for CUAs: static pre-vetted skill sets freeze capability growth, while unrestricted continual learning accumulates unevaluated behavioral surface area — and reframes skill learning as a *safety-constrained interaction process* rather than a static catalog problem.
- Proposes a runtime safety-evaluation gating primitive that inspects every skill invocation against the current environment state and the agent's current task context, allowing safe skill execution to proceed and blocking or sandboxing risky invocations before side-effects occur.
- Validates SkillHarness on dynamic interactive environments where the agent must continually acquire new skills, showing that the safety-constrained interaction process preserves continual-learning capability gains while preventing the unsafe-invocation failure modes that fully-open continual-learning baselines exhibit.
- Surfaces the *harness-as-intermediary* pattern for computer-use agents — a runtime layer that mediates between the policy's skill-selection decisions and the environment's effect-execution channel — extending the eval-as-discipline and capability-versus-safety framing from pre-deployment safety work into the deployment-time runtime surface where continual learning happens.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on 2026-06-25 (computer-use agents / skill-curation / safety theme).
- [[capable-but-careless-do-computer-use-agents-follow-contextual-integrity-2606.23189]] — Sibling entry on computer-use agent contextual-integrity compliance; both papers diagnose the structural capability-versus-safety axis in CUAs but from different surfaces — Capable-But-Careless audits task-execution adherence to contextual integrity, SkillHarness gates skill-invocation against environment-state risk — together they bracket the CUA safety surface between execution-time rule-following and invocation-time safety gating.
- [[tropt-an-open-framework-for-unifying-and-advancing-discrete-text-optimization-2606.23496]] — Sibling entry on open-source discrete text optimization; TROPT supplies the optimization substrate that produces adversarial skill-trigger sequences, and SkillHarness is the deployment-time defensive layer that gates whether such triggers are even invocable — together they bracket the CUA safety surface between adversarial-trigger generation (TROPT) and runtime safety gating (SkillHarness).
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — Sibling entry on entropy-dynamics jailbreak detection; both papers contribute detection-time primitives for adversarial inputs — Entropy-Layers operates at hidden-state level for jailbreak detection, SkillHarness operates at skill-invocation level for runtime safety — extending the runtime-defense wave into the agent-action channel.
- [[critique-of-agent-model-2606.23991]] — Sibling entry on agent epistemology and the agentive-vs-agentive distinction; both papers push back against naive "agent" framings — Critique-of-Agent argues agency requires internalized goal/identity/decision structures, SkillHarness argues that even without full agency, runtime safety gating is a load-bearing primitive for the deployment regime where skill learning is continual and surface area is unbounded.