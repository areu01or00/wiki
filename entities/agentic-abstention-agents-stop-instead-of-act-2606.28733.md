---
title: "Agentic Abstention: Do Agents Know When to Stop Instead of Act?"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [llm-agents, abstention, sequential-decision-making, tool-use]
sources: ["https://arxiv.org/abs/2606.28733"]
---

# Agentic Abstention: Do Agents Know When to Stop Instead of Act?

## Overview
Defines Agentic Abstention — the problem of deciding when an LLM agent should stop acting under uncertainty in multi-turn tool-use environments. Unlike single-turn abstention, agentic abstention is a sequential decision problem where the need to abstain may only become clear after environment interaction. Introduces CONVOLVE, a context-engineering method that distills full interaction trajectories into reusable stopping rules.

## Key Facts
- **Year**: 2026
- **arXiv**: [2606.28733](https://arxiv.org/abs/2606.28733)

## Key Contributions
- **Agentic Abstention Problem Definition**: Formalizes agentic abstention as a sequential decision problem distinct from single-turn answer-or-abstain tasks; evaluates 13 LLM-as-agent systems across 28,000+ tasks
- **Scale Paradox in Timely Abstention**: Larger or more capable models sometimes perform worse at timely abstention — demonstrating that capability and abstention are not monotonically related
- **CONVOLVE Context Engineering**: Distills full interaction trajectories into reusable stopping rules without updating model parameters; raises Llama-3.3-70B's timely recall rate from 26.7 to 57.4 on WebShop
- **Web Shopping, Terminal, and QA Environments**: First systematic study of abstention across diverse agent scaffolds and environment types

## Related Papers
- [[taco-tool-augmented-credit-optimization-for-agentic-tool-use-2606.30251]] — Tool-augmented credit optimization for agentic tool use
- [[est-prm-stress-testing-process-reward-models-before-they-become-load-bearing-2606.00437]] — Stress testing PRMs before they become load-bearing; process reward evaluation methodology
