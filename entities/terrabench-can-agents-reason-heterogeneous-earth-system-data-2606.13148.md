---
title: "TerraBench: Can Agents Reason Over Heterogeneous Earth-System Data?"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [agent, benchmark, scientific-reasoning, tool-use, earth-system, llm]
sources: ["https://arxiv.org/abs/2606.13148"]
---

# TerraBench: Can Agents Reason Over Heterogeneous Earth-System Data?

## Overview
TerraBench is a benchmark for grounded Earth-science reasoning built on TerraAgent, a ReAct-style executable framework that couples LLM planning with scientific tools for environmental retrieval, geospatial processing, simulation, and artifact-backed computation. The benchmark unifies analysis of Earth observation imagery, gridded data, GIS reasoning and simulation in a single executable interface, pairing process-level tool-use metrics with tolerance-aware numeric scoring across 403 extensive agentic tasks.

## Key Facts
- **Authors**: Dat Tien Nguyen, Thao Nguyen, Fadillah Adamsyah Maani, Huy M. Le, Muhammad Umer Sheikh, Numa
- **Year**: 2026
- **arXiv**: [2606.13148](https://arxiv.org/abs/2606.13148)

## Key Contributions
- TerraAgent framework: ReAct-style coupling of LLM planning with scientific tools for heterogeneous data (satellite imagery, gridded physical data, geospatial context, simulator outputs)
- First benchmark to unify process-level tool-use metrics with tolerance-aware numeric scoring
- 403 extensive agentic tasks across Fundamentals, Simulator-Grounded, and Document-Grounded Verification tracks
- 24,500 verified execution steps
- Finding: reliable Earth-science agents must coordinate heterogeneous workflows, parameterize tools precisely, and preserve artifact provenance

## Related Papers
- [[agora-an-archive-grounded-benchmark-for-agentic-workplace-document-reasoning-2606.24526]] — Archive-grounded agentic reasoning benchmark
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — Long-horizon planning in large tool ecosystems
- [[calibration-is-not-control-llm-agent-oversight-needs-intervention-2606.21399]] — Agent oversight and tool-use reliability
