---
title: "Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [memory, agent, rl, credit-assignment, grpo, long-horizon]
sources: ["https://arxiv.org/abs/2605.21768"]
---

# Memory-R2: Fair Credit Assignment for Long-Horizon Memory-Augmented LLM Agents

## Overview
Memory-R2 introduces a training framework for long-horizon memory-augmented LLM agents that fixes a structural unfairness in trajectory-level reward signals: once different rollouts write, update, or delete different memories, they no longer share the same intermediate memory state, so trajectory-level comparisons under group-relative methods like GRPO become fundamentally unfair. The core algorithm LoGo-GRPO combines local rerollouts (same memory state, different memory-operation outcomes) with global trajectory-level optimization, and a co-learning design jointly optimizes memory formation and evolution via shared-parameter fact extractor + memory manager.

## Key Facts
- **Authors**: Yan, Sikuan; Bahloul, Ahmed; Nie, Ercong; Schwarzmann, Susanna; Trivisonno, Riccardo; Tresp, Volker
- **Year**: 2026
- **arXiv**: [2605.21768](https://arxiv.org/abs/2605.21768)
- **Date**: 2026-05-20

## Key Contributions
- **Diagnosis**: When memory becomes part of the agent's environment, trajectory-level group-relative methods (GRPO, PPO) violate a foundational fairness assumption — different rollouts no longer sample from the same effective environment because their memory states diverge, so trajectory-level rewards provide noisy/biased credit signals for memory operations.
- **LoGo-GRPO (Local + Global Group-Relative Optimization)**: Preserves end-to-end learning from long-horizon trajectory-level rewards via a global objective, while local rerollouts compare different memory-operation outcomes from the same intermediate memory state — yielding fairer group comparisons and more precise supervision for memory construction.
- **Co-learning design**: Joint optimization of memory formation (fact extractor) and memory evolution (memory manager) with shared parameters, rather than treating them as decoupled components.
- **Empirical validation**: Outperforms outcome-RL baselines on multi-session long-horizon environments where memory trajectories diverge across rollouts — the exact regime where trajectory-level credit assignment becomes structurally unfair.

## Key Insights
- The "verifying is easier than producing" intuition (cf. [[the-verification-horizon-no-silver-bullet-for-coding-agent-rewards-2606.26300]]) inverts for memory agents: *producing memory states that allow fair comparison* is harder than producing answers, because memory state divergence makes group comparisons structurally unfair.
- Local rerollouts from a shared memory state are the algorithmic primitive that restores the GRPO fairness assumption without abandoning end-to-end trajectory-level learning.
- Joint co-training of formation+evolution (rather than decoupled pipelines) is the structurally correct primitive because memory state drift couples the two objectives — improving one without the other caps overall memory quality.

## Related Papers
- [[meta-cognitive-memory-policy-optimization-for-long-horizon-llm-agents-2605.30159]] — Sibling Run 55 memory-policy paper (MMPO). MMPO provides a *belief-entropy self-supervised proxy* for memory quality; Memory-R2 provides *fair credit assignment* for memory operations. Together they bracket the memory-agent training surface between uncertainty-aware supervision and trajectory-level credit allocation.
- [[agentic-reasoning-for-large-language-models-2601.12538]] — Run 55 agentic-reasoning survey. Memory-R2 is the load-bearing *training-algorithm primitive* for the survey's memory layer of self-evolving agentic reasoning.
- [[agent-memory-characterization-and-system-implications-of-stateful-long-horizon-workloads-2606.06448]] — Sibling memory-system characterization. Memory-R2 complements with the training-side fairness primitive.
- [[emergent-concepts]] — Parent wiki page.