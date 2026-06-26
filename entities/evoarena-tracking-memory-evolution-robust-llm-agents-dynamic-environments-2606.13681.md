---
title: "EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [agent-benchmark, dynamic-environment, memory-evolution, persistent-state, llm-agent, evaluation]
sources: ["https://arxiv.org/abs/2606.13681"]
---

# EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments

## Overview
EvoArena introduces a benchmark suite for evaluating LLM agents under *persistent environment evolution* — agents must continually align their knowledge, skills, and behavior with changing environments over extended interaction. The work addresses a structural gap in agent evaluation: most existing benchmarks assume static environments, but real-world deployment is inherently dynamic (tools change APIs, documents update, user preferences drift), and agents that perform well on static benchmarks routinely fail under persistent change because their memory representations become stale. EvoArena's central contribution is *memory evolution tracking* — measuring how an agent's internal representations and external memory artifacts adapt to environment change as a first-class evaluation axis.

## Key Facts
- **Authors**: Xu, Jundong; Li, Qingchuan; Wu, Jiaying; Lan, Yihuai; Li, Shuyue Stella; + 9 more (14 total)
- **Year**: 2026
- **arXiv**: [2606.13681](https://arxiv.org/abs/2606.13681)
- **Submitted**: 2026-06-11
- **Discovered via**: emergent-concept search on 2026-06-26 (dynamic-environment-benchmark / memory-evolution / persistent-state / version-aware-agents theme)
- **First-in-wiki surface**: Persistent-environment-evolution benchmark for LLM agents (verified via `ls entities/ | grep -iE "(arena|persistent|dynamic.env|memory.evol)"` returning empty)

## Key Contributions
- Identifies a structural under-evaluation gap: most LLM agent benchmarks assume static environments, leaving the deployment regime where environments evolve over time structurally un-assessed despite being the common case
- Introduces EvoArena as a benchmark suite where the environment *persists and evolves* across episodes — tools, APIs, documents, and task definitions change between rounds, and agents must adapt their memory representations to maintain performance
- Surfaces *memory evolution tracking* as a load-bearing evaluation primitive: agent capability is not just accuracy-at-time-T but the rate at which memory representations converge to the new environment state and the graceful degradation curve under sustained drift
- Demonstrates that frontier agents exhibit characteristic failure patterns under persistent evolution — over-reliance on outdated cached knowledge, delayed update of tool-use policies, and loss of cross-session consistency — none of which are visible in static benchmarks
- Surfaces *version-awareness* as a structurally distinct axis from raw capability: agents that score well on static benchmarks can still fail under persistent environment change because their representations do not track version drift

## Related Papers
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — sibling agent-memory-survey (Are-Ready surveys agent-memory architecture choices including update policies; EvoArena isolates the *evaluation* axis — under persistent evolution, the question is not which memory design is best but how to *measure* memory evolution)
- [[gatemem-benchmarking-memory-governance-in-multi-principal-shared-memory-agents-2606.18829]] — sibling memory-governance benchmark (GateMem benchmarks multi-principal shared-memory governance; EvoArena benchmarks *unipersonal* memory evolution under persistent environment change — together they bracket the agent-memory-evaluation surface)
- [[worldlines-benchmarking-and-modeling-long-horizon-stateful-2606.18847]] — sibling long-horizon-memory benchmark (WorldLines benchmarks long-horizon memory in embodied agents; EvoArena extends the long-horizon principle to non-embodied software environments with persistent API/version drift)
- [[beyond-static-leaderboards-predictive-validity-evaluation-llm-agents-2606.19704]] — sibling agent-evaluation-methodology (Beyond-Static-Leaderboards critiques aggregate-leaderboard scoring; EvoArena's version-aware scoring is a concrete instantiation of that critique — score one version vs another is structurally different from scoring one task vs another)
- [[emergent-concepts]] — parent meta-page for this discovery
