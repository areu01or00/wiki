---
title: "Can LLM Agents Infer World Models? Evidence from Agentic Automata Learning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [world-model, llm-agents, planning, automata-learning, agentic-ai]
sources: ["https://arxiv.org/abs/2606.16576"]
---

# Can LLM Agents Infer World Models? Evidence from Agentic Automata Learning

## Overview
This paper proposes Agentic Automata Learning (AAL) to evaluate whether tool-calling LLM agents can uncover hidden environments through interaction. The agent must identify a hidden deterministic finite automaton (DFA) via two query types: membership queries ("Does this string belong to the target language?") and equivalence queries ("Is my current hypothesis correct?"). Results reveal the conditions under which LLMs can and cannot learn world models from interaction — providing a principled benchmark for testing emergent world-model acquisition in agentic systems.

## Key Facts
- **Authors**: (from arxiv 2606.16576)
- **Year**: 2026
- **arXiv**: [2606.16576](https://arxiv.org/abs/2606.16576)

## Key Contributions
- Formal framework (Agentic Automata Learning) for evaluating world-model inference in LLM agents via active learning
- Membership and equivalence query protocol for systematically testing hidden DFA identification
- Establishes empirical conditions under which LLM agents can vs cannot acquire world models from interaction
- Contrasts with passive world-model construction (WorldEvolver, Internalizing the Future) — tests active inference capability
- Orthogonal to world-model-as-planning-substrate papers: focuses on world-model acquisition mechanism rather than planning application

## Related Papers
- [[worldevolver-self-evolving-world-models-for-llm-agent-planning-2606.30639]] — WorldEvolver: Self-Evolving World Models for LLM Agent Planning (world models for planning — application vs this paper's acquisition mechanism)
- [[internalizing-the-future-a-unified-agentic-training-paradigm-for-world-model-planning-2606.27483]] — Internalizing the Future: World Model Planning (planning with world models — application axis, orthogonal to acquisition mechanism)
- [[agentic-world-modeling-foundations-capabilities-laws-and-beyond-2604.22748]] — Agentic World Modeling: Foundations, Capabilities, Laws and Beyond (survey of world-modeling for agents — broader framing)
