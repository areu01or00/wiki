---
title: "GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [multi-agent, llm, optimization, attribution, gradient]
sources: ["https://arxiv.org/abs/2606.28187"]
---

# GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems

## Overview
GBC is a framework for fine-grained attribution and optimization of multi-agent LLM systems. It models a multi-agent system as a computational graph, introduces gradient-based connection weights to quantify each agent's token-level influence on downstream agents, and uses backward propagation of task-specific loss to identify error sources and target prompt optimization. The approach is implemented as AgentChord, a system that uses prefix-based gradient computation for efficiency, and improves multi-agent performance over strong single-agent and multi-agent baselines on MultiWOZ and τ-bench.

## Key Facts
- **Authors**: Yang, Xiaocheng; Alrabah, Abdulrahman; Hakkani-Tür, Dilek; Tur, Gokhan
- **Year**: 2026
- **arXiv**: [2606.28187](https://arxiv.org/abs/2606.28187)

## Key Contributions
- **Computational-graph model of multi-agent LLM systems**: GBC models a multi-agent system as a directed graph where nodes are agents and edges carry outputs between them, enabling systematic application of gradient-based attribution to the agent-coordination layer.
- **Token-level gradient-based connection weights**: each agent's contribution to a downstream agent's output is quantified at token-level granularity by computing gradients of the downstream loss with respect to the upstream agent's output tokens, providing fine-grained credit assignment across agents and interaction steps.
- **Backwards loss propagation for targeted prompt optimization**: the attribution graph is used to propagate task-specific loss signals backward through the multi-agent system, identifying which agents and steps are responsible for errors and providing a principled target for prompt-level optimization.
- **AgentChord efficient implementation**: prefix-based gradient computation reduces the cost of attribution, making fine-grained gradient analysis tractable for real multi-agent deployments.
- **Empirical improvement on standard multi-agent benchmarks**: GBC improves multi-agent performance over strong single-agent and multi-agent baselines on MultiWOZ and τ-bench, and the experiments show that higher attribution quality is associated with greater optimization effectiveness.

## Related Papers
- [[coordination-as-an-architectural-layer-for-llm-based-multi-agent-systems-2605.03310]] — Sibling work that treats coordination as an architectural layer for LLM-based multi-agent systems, providing architectural primitives complementary to GBC's gradient-based fine-grained attribution.
- [[when-gradients-collide-failure-modes-of-multi-objective-prompt-optimization-for-llm-judges-2605.26046]] — Sibling work identifying failure modes when gradient-based prompt optimization is applied to multiple objectives; complements GBC by characterizing the multi-objective loss geometry that GBC's gradient-based attribution must navigate in MAS prompt optimization.
- [[memory-r2-fair-credit-assignment-for-long-horizon-memory-augmented-llm-agents-2605.21768]] — Sibling work introducing fair credit assignment for long-horizon memory-augmented LLM agents; complements GBC's token-level gradient-based credit assignment with a memory-reward credit-assignment layer.
- [[emergent-concepts]] — Parent meta-page listing all emergent-concept entities in the wiki.
