---
title: "Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [neuro-symbolic, llm, agent, skill-induction, long-horizon-planning, programmatic-representation]
sources: ["https://arxiv.org/abs/2605.01293"]
---

# Lifting Traces to Logic: Programmatic Skill Induction with Neuro-Symbolic Learning for Long-Horizon Agentic Tasks

## Overview
Shao, Yin, Lyu and colleagues propose Neuro-Symbolic Skill Induction (NSI), a framework that *lifts interaction traces into modular, logic-grounded programs*. Where existing skill induction methods distil experience into state-blind parameterised scripts that fail to capture conditional logic, NSI synthesises explicit control flows and dynamic variable binding, empowering agents to discover *when* and *why* to act — enabling efficient generalisation from few-shot examples and flexible adaptation to unseen goals.

## Key Facts
- **Authors**: Shao, Jie-Jing; Yin, Haiyan; Lyu, Yueming et al.
- **Year**: 2026
- **arXiv**: [2605.01293](https://arxiv.org/abs/2605.01293)
- **Online date**: 2026-05-02

## Key Contributions
- **Trace-to-logic lifting as skill induction**: rather than distilling experience into a parameterised script (state-blind), NSI *lifts interaction traces into modular logic-grounded programs* — preserving the conditional logic and dynamic variable binding required for robust execution in dynamic environments.
- **Explicit control flow + dynamic variable binding**: NSI synthesises *when-and-why-to-act structure* — agents self-evolve into architects of logic-grounded skills. The conditional logic captures the operational preconditions and post-conditions of skill activation that flat scripts cannot represent.
- **Few-shot generalisation to unseen goals**: by inducing *modular, logic-grounded* programs from few-shot traces, NSI agents flexibly adapt to unseen goals via compositional recombination of induced skills — distinct from behavioural cloning which requires many demonstrations per goal.
- **Logic-grounded execution via conditional determinism**: the induced graph dictates control flow via *conditional determinism* — operating on grounded symbolic predicates in $Z_t$ (state variables), the agent's behaviour is reproducible and verifiable, not stochastic.

## Related Papers
- [[from-agent-traces-to-trust-a-survey-of-evidence-tracing-and-execution-provenance-in-llm-agents-2606.04990]] — sibling — Evidence-Tracing-and-Execution-Provenance survey covers *trace-grounding for trust*; NSI covers *trace-lifting for skill induction*. Together they bracket the *agent-trace-processing* surface between trace-as-evidence-grounding and trace-as-logic-grounding primitives.
- [[hidden-thoughts-are-not-secret-reasoning-trace-exposure-in-llms-2606.00642]] — sibling — Hidden-Thoughts-Reasoning-Trace-Exposure analyses *CoT-trace exposure risk*; NSI addresses *trace lifting to logic-grounded skills*. Together they bracket the *LLM-trace-representation* surface between trace-as-leakage-surface (Hidden-Thoughts) and trace-as-skill-induction-substrate (NSI) primitives.
- [[opid-on-policy-skill-distillation-for-agentic-reinforcement-learning-2606.26790]] — sibling — OPID introduces *on-policy skill distillation* (token-level supervision from agent's acquired skills); NSI introduces *programmatic skill induction from traces*. Together they bracket the *agentic-skill-acquisition* surface between skill-as-distilled-policy (OPID) and skill-as-logic-grounded-program (NSI) primitives.
- [[agentic-reasoning-for-large-language-models-2601.12538]] — Run 55 sibling — Agentic-Reasoning-Survey provides *agentic-reasoning taxonomy*; NSI provides *logic-grounded programmatic skill primitive* within agentic settings. Together they bracket the *LLM-agent-capability-surface* between agentic-reasoning-taxonomy and agentic-skill-induction-mechanism primitives.
- [[delta1-with-llm-symbolic-neural-integration-for-credible-and-explainable-reasoning-2603.12953]] — Run 80 sibling — Δ₁–LLM integrates FTSC theorem generation with LLM verbalization for explainability-by-construction; NSI lifts traces into logic-grounded programs for skill-induction-by-construction. Together they bracket the *neuro-symbolic-construction* surface between construction-as-theorem-generation (Δ₁) and construction-as-skill-induction (NSI) primitives — both exploit symbolic structures as the load-bearing substrate for *by-construction* properties (soundness/minimality vs generalisation/reproducibility).
- [[emergent-concepts]] — parent wiki page

## Theme
neuro-symbolic-grounding / trace-to-logic-lifting / programmatic-skill-induction / long-horizon-planning / logic-grounded-control-flow / dynamic-variable-binding / few-shot-generalisation / conditional-determinism / few-shot-skill-acquisition / modular-recombinable-skills

**First programmatic skill induction framework that lifts interaction traces into logic-grounded programs via neuro-symbolic learning for long-horizon agentic tasks in the wiki.** Verified via `ls entities/ | grep -iE "(nsi|trace.to.logic|programmatic.skill|logic.grounded.skill|conditional.determinism|lifting.traces|trace.lift)"` returning empty.