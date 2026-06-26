---
title: "Why Reasoning Fails to Plan: A Planning-Centric Analysis of Long-Horizon Decision Making in LLM Agents"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [planning, reasoning, long-horizon, agents, decision-making, llm, lookahead]
sources: ["https://arxiv.org/abs/2601.22311"]
---

# Why Reasoning Fails to Plan: A Planning-Centric Analysis of Long-Horizon Decision Making in LLM Agents

## Overview
This paper diagnoses a fundamental mismatch in LLM-based agents: step-by-step reasoning is strong on short horizons but fails to sustain coherent behavior over long planning horizons because it induces a *step-wise greedy policy* that is adequate for short horizons but fails when early actions must account for delayed consequences. Wang, Zehong; Wu, Fang; Wang, Hongru; Tang, Xiangru; Li, Bolian; Yin, Zhenfei (et al.) study LLM agents in deterministic, fully structured environments with explicit state transitions and evaluation signals, revealing that locally optimal step-wise choices produce early myopic commitments that are systematically amplified over time and are difficult to recover from. The paper introduces **FLARE** (Future-aware Lookahead with Reward Estimation) — a minimal instantiation of future-aware planning that enforces explicit lookahead, value propagation, and limited commitment in a single model — and shows that LLaMA-8B with FLARE frequently outperforms GPT-4o with standard step-by-step reasoning, establishing a clear conceptual distinction between *reasoning* and *planning*.

## Key Facts
- **Authors**: Zehong Wang, Fang Wu, Hongru Wang, Xiangru Tang, Bolian Li, Zhenfei Yin (et al.)
- **Year**: 2026
- **arXiv**: [2601.22311](https://arxiv.org/abs/2601.22311) ([pdf](https://arxiv.org/pdf/2601.22311))
- **Date published**: 2026-01-29
- **Subjects**: cs.CL, cs.AI, cs.LG
- **Methodology**: Planning-centric analysis in deterministic fully-structured environments with explicit state transitions; FLARE architecture combining explicit lookahead + value propagation + limited commitment; multiple benchmarks + agent frameworks + LLM backbones; comparison vs step-by-step reasoning baselines including GPT-4o.

## Key Contributions
- **Surfaces *step-wise greedy policy* as the structural failure mode of reasoning for planning**: argues that the failure of LLM agents on long-horizon tasks is not a capability problem but a *policy-structural* problem — step-wise scoring induces myopic commitments that compound over time. This inverts the conventional "LLM reasoning just needs to be more capable" framing.
- **Distinguishes *reasoning* from *planning* as separate cognitive primitives**: even with strong step-by-step reasoning, long-horizon planning requires explicit lookahead and value propagation — capabilities that reasoning alone does not provide. Establishes *reasoning* and *planning* as orthogonal cognitive axes that must be reasoned about jointly.
- **FLARE as a minimal future-aware planning instantiation**: combines explicit lookahead, value propagation, and limited commitment in a single model — surfacing *future-aware-planning-as-load-bearing-primitive* rather than capability scaling. LLaMA-8B+FLARE frequently outperforming GPT-4o is the load-bearing empirical result.
- **Myopic-commitment-amplification as the failure-dynamics primitive**: locally optimal step-wise choices become globally suboptimal because they lock the agent into early commitments that compound over time — a dynamic that is invisible to single-step evaluation but visible at the trajectory level.
- **Decision-centric evaluation principles for long-horizon agents**: the analysis yields evaluation principles that focus on planning-level behavior (not just task-completion rate), moving beyond aggregate-success metrics toward commitment-recovery and value-propagation-fidelity primitives.

## Related Papers
- [[emergent-concepts]] — parent meta-page that catalogued this paper as part of the long-horizon-planning / step-wise-greedy-policy / future-aware-lookahead / FLARE theme.
- [[reasoninglens-hierarchical-visualization-and-diagnostic-auditing-for-large-reasoning-models-2606.23404]] — sibling Run 60 trace-diagnostic paper; ReasoningLens provides the *hierarchical-trace-structure primitive* (high-level strategy vs low-level execution) that surfaces the FLARE-relevant strategy-vs-execution distinction, Why-Reasoning-Fails-to-Plan is the *planning-failure-mechanism* diagnosis that ReasoningLens's hierarchy helps visualize.
- [[when-the-chain-of-thought-knows-better-failure-modes-in-multi-turn-reasoning-models-2606.10740]] — sibling Run 60 reasoning-failure paper; Why-Reasoning-Fails-to-Plan is *long-horizon-planning-failure* diagnostic, When-the-Chain-of-Thought-Knows-Better is *multi-turn-safety-failure* diagnostic — together they bracket the reasoning-failure surface between planning-strategy-failure and multi-turn-safety-locking primitives.
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — sibling long-horizon-planning evaluation work; PlanBench-XL surfaces *planning-evaluation-failure modes* in tool ecosystems at scale, Why-Reasoning-Fails-to-Plan surfaces the *step-wise-greedy-policy mechanism* in deterministic environments — together they bracket the long-horizon-planning surface between tool-ecosystem-evaluation and policy-structural-failure-mode primitives.
- [[agentic-reasoning-for-large-language-models-2601.12538]] — sibling Run 55 agentic-reasoning survey; Agentic-Reasoning provides the *three-layer-environment-dynamics-taxonomy* that includes planning as a foundational layer, Why-Reasoning-Fails-to-Plan is the *mechanistic-diagnosis* of *why* the planning layer's step-wise reasoning fails at long horizons — together they bracket the agentic-reasoning-planning surface between survey-level taxonomy and mechanism-level diagnosis primitives.
- [[in-context-world-modeling-for-robotic-control-2606.26025]] — sibling in-context world modeling for embodied agents; both address *lookahead-and-commitment* problems — In-Context-World-Modeling uses implicit world models for robotic control, Why-Reasoning-Fails-to-Plan uses explicit value-propagation lookahead for general agents — together they bracket the lookahead-planning surface between implicit-world-model and explicit-value-propagation primitives.
