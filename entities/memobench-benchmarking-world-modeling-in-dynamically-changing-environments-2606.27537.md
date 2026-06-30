---
title: "MemoBench: Benchmarking World Modeling in Dynamically Changing Environments"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [world-modeling, benchmark, memory]
sources: ["https://arxiv.org/abs/2606.27537"]
---

# MemoBench: Benchmarking World Modeling in Dynamically Changing Environments

## Overview
MemoBench evaluates video generation models as world simulators by testing memory consistency across dynamically changing environments. Unlike prior benchmarks that evaluate world models on static or slowly-changing scenes, MemoBench specifically targets the failure mode where world models forget or mishandle changes to objects, scenes, or physical rules that occur mid-trajectory. The benchmark introduces structured probes for object persistence, causal intervention consistency, and temporal coherence under distribution shift.

## Key Facts
- **Authors**: Multiple (inferred from arXiv submission)
- **Year**: 2026
- **arXiv**: [2606.27537](https://arxiv.org/abs/2606.27537)

## Key Contributions
- Structured benchmark for evaluating world model memory consistency under dynamic environmental changes
- Tests object persistence, causal intervention consistency, and temporal coherence — three orthogonal failure modes of world modeling
- Reveals that current world models systematically fail when object properties or scene rules change mid-trajectory
- Provides diagnostic split of world-model failure modes to guide improvement efforts

## Related Papers
- [[einstein-world-models-2606.26969]] — physics-informed world models; MemoBench provides the diagnostic benchmark for such models' memory consistency
- [[agentic-world-modeling-foundations-capabilities-laws-and-beyond-2604.22748]] — foundational world modeling taxonomy; MemoBench operationalizes evaluation across its memory-axis
- [[causal-rcm-a-unified-teacher-forcing-and-self-forcing-open-recipe-for-autoregressive-diffusion-distillation-in-streaming-video-generation-and-interactive-world-models-2606.25473]] — world model distillation; MemoBench identifies the memory-consistency failure mode this approach must address
