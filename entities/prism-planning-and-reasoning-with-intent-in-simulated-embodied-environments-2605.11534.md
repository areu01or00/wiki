---
title: "PRISM: Planning and Reasoning with Intent in Simulated Embodied Environments"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [embodied-agent, benchmarking, planning, reasoning, llm]
sources: ["https://arxiv.org/abs/2605.11534"]
---

# PRISM: Planning and Reasoning with Intent in Simulated Embodied Environments

## Overview
PRISM introduces a diagnostic framework for embodied LLM agents that decomposes failure at household tasks into three distinct cognitive modules: object identification, sub-goal tracking, and action sequencing. Existing benchmarks report only a single success/failure binary, making it impossible to determine which cognitive module is responsible for failure. PRISM provides fine-grained module-level diagnostics, enabling targeted improvement of specific agent capabilities rather than end-to-end black-box optimization.

## Key Facts
- **Authors**: Lim, Yunn Kang; Sun, Pengzhan; Bai, Ziyi + 4
- **Year**: 2026
- **arXiv**: [2605.11534](https://arxiv.org/abs/2605.11534)

## Key Contributions
- First module-level diagnostic benchmark for embodied LLM agents (object ID / sub-goal / action sequencing)
- Demonstrates that single success-rate metrics mask which cognitive module is failing — a fundamental measurement problem
- Provides structured evaluation protocol replicable across different embodied agent architectures
- Enables targeted capability improvement by isolating specific module failures rather than treating the whole agent as a black box

## Related Papers
- [[holoagent-0-a-unified-embodied-agent-framework-with-3d-spatial-memory-2606.23565]] — Unified embodied agent with spatial memory; the 3D memory module corresponds to PRISM's object-identification diagnostic dimension
- [[envscaler-scaling-tool-interactive-environments-for-llm-agent-via-programmatic-synthesis-2601.05808]] — Environment scaling for tool-interactive agents; PRISM's diagnostic framework applies directly to environments at different scale regimes
- [[evoarena-tracking-memory-evolution-robust-llm-agents-dynamic-environments-2606.13681]] — Dynamic environment memory tracking; extends PRISM's module diagnostics to temporal dimension where sub-goal drift occurs
