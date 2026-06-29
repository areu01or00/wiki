---
title: "ZenBrain: A Neuroscience-Inspired 7-Layer Memory Architecture for Autonomous AI Systems"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [memory, neuroscience, long-context, agent, llm, cross-discipline, architecture]
sources: ["https://arxiv.org/abs/2604.23878"]
---

# ZenBrain: A Neuroscience-Inspired 7-Layer Memory Architecture for Autonomous AI Systems

## Overview
First paper in the wiki to systematically map **7 neuroscience memory subsystems** (sensory, working, episodic, semantic, procedural, prospective, consolidation) onto a unified LLM-agent memory architecture. Achieves 91.3% of a long-context oracle's accuracy on LongMemEval-500 at 1/106th of the per-query token cost, providing a neuroscience-grounded primitive-class for memory-efficient long-horizon agents.

## Key Facts
- **Authors**: Bering, Alexander et al.
- **Year**: 2026
- **arXiv**: [2604.23878](https://arxiv.org/abs/2604.23878)
- **Online Date**: 2026-05-02 (citation_date 2026-04-26)
- **Domain**: neuroscience × LLM-memory-architecture × agent-system-design

## Key Contributions
- **Neuroscience-grounded 7-layer memory taxonomy**: maps biological memory subsystems (sensory buffer, working memory, episodic memory, semantic memory, procedural memory, prospective memory, consolidation) onto LLM-agent memory primitives, providing a principled cross-discipline frame for organizing memory functions
- **Cost-vs-accuracy frontier shift**: matches long-context oracle's binary-judge accuracy (47.7% vs 52.2%) on LongMemEval-500 at 1/106th the per-query token cost — a 100x+ efficiency gain from principled memory organization rather than long-context scaling
- **All 12 head-to-head answer-quality cells won** against 4 baseline systems × 3 LLM judges — establishes neuroscience-mapping as a competitive primitive for memory-intensive agent workloads
- **Cross-discipline primitive**: bridges neuroscience × LLM-architecture — provides a vocabulary for memory-subsystem reasoning that is structurally different from existing vector-RAG, hierarchical-RAG, or graph-memory approaches (which don't map to biology)
- **Resolves the long-context-vs-memory trade-off**: rather than scaling context window, organises memory by neuroscience-inspired subsystems — making it a structural alternative to context-extension primitives like EndPrompt (Run 68) and context-RL approaches (Run 64)

## Related Papers
- [[memory-r2-fair-credit-assignment-for-long-horizon-memory-augmented-llm-agents-2605.21768]] — Sibling from Run 55 that addresses long-horizon memory credit assignment; complements ZenBrain's neuroscience-grounded organization
- [[agent-memory-characterization-and-system-implications-of-stateful-long-horizon-workloads-2606.06448]] — Cross-discipline primitive on stateful agent memory workloads; ZenBrain provides neuroscience-grounded architecture for this workload
- [[memory-is-reconstructed-not-retrieved-graph-memory-llm-agents-2606.06036]] — Sibling that frames memory as graph-reconstruction; orthogonal to ZenBrain's neuroscience-layers approach
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Cross-discipline primitive evaluating agent-native memory system readiness
- [[endprompt-efficient-long-context-extension-via-terminal-anchoring-2605.14589]] — Run 68 axis-inversion primitive on long-context extension; ZenBrain inverts the long-context-extension axis with neuroscience-grounded memory organization