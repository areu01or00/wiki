---
title: "Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [architecture, llm]
sources: ["https://arxiv.org/abs/2606.06448"]
---

# Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads

## Overview

LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. Realizing this at scale requires agents to persistently store, retrieve, and update their own memory across sessions. A rich ecosystem of agent memory systems has emerged spanning flat retrieval, LLM-mediated extraction, consolidating fact stores, and agentic control flows. Yet, their system-level behavior remains uncharacterized. We present the first systems characterization of agent memory. First, we introduce a system-oriented taxonomy classifying agent memory systems along four axes: storage substrate, extraction mechanism, consolidation strategy, and control flow. Second, we run controlled experiments measuring end-to-end behavior across long-horizon workloads, characterizing cost, latency, recall, and revision under realistic session lengths.

## Key Facts
- **Authors**: Omri, Yasmine and Gan, Ziyu and Broveak, Zachary et al.
- **Year**: 2026
- **arXiv**: [2606.06448](https://arxiv.org/abs/2606.06448)

## Key Contributions
- First **systems-level** characterization of agent memory (vs prior surveys like Are-We-Ready which are framework-level) — measures cost/latency/recall/revision under realistic session lengths
- 4-axis taxonomy: storage substrate, extraction mechanism, consolidation strategy, control flow — discriminates systems that prior 1-axis taxonomies (e.g., extraction-only) lumped together
- Controlled experiments across long-horizon workloads expose system-level behavior (error compounding, retrieval staleness) that end-to-end QA benchmarks miss
- Reframes agent memory evaluation from 'does it work?' to 'what does it cost?' — load-bearing question for production deployment where inference cost dominates

## Related Papers
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]]
- [[worldlines-benchmarking-and-modeling-long-horizon-stateful-2606.18847]]
- [[memgui-agent-end-to-end-long-horizon-mobile-gui-agent-proactive-context-2606.19926]]
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]]
