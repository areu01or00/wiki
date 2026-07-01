---
title: "Embodied CAD: Solver-Grounded LLM Agents for Parametric B-Rep Assembly Modeling"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [llm-agents, cad-reasoning, geometric-solver, agentic-planning, llm]
sources: ["https://arxiv.org/abs/2606.31252"]
---

# Embodied CAD: Solver-Grounded LLM Agents for Parametric B-Rep Assembly Modeling

## Overview
Embodied CAD grounds LLM agents in geometric constraint solvers for reliable parametric B-Rep CAD assembly modeling. While LLMs can write syntactically valid CAD scripts, reliable industrial CAD requires every feature, placement, and assembly relation to be accepted by an exact geometric kernel. Embodied CAD bridges this gap by integrating solver-grounded agents that verify geometric validity before code generation.

## Key Facts
- **arXiv**: [2606.31252](https://arxiv.org/abs/2606.31252)

## Key Contributions
- Solver-grounded LLM agents that verify CAD feature validity against exact geometric kernels
- Addresses the gap between syntactically valid and geometrically correct CAD code generation
- Parametric B-Rep assembly modeling beyond toy examples to industrially relevant geometry

## Related Papers
- [[specgen-accelerating-agentic-kernel-optimization-with-speculative-generation-2606.17518]] — Agentic kernel optimization; relevant to Embodied CAD's agent planning over constrained search spaces
- [[think-twice-before-you-act-protecting-llm-agents-against-tool-description-poisoning-via-isolated-planning-2606.20922]] — Isolated planning for agent safety; relevant to Embodied CAD's geometric validation
- [[why-reasoning-fails-to-plan-a-planning-centric-analysis-of-long-horizon-decision-making-in-llm-agents-2601.22311]] — Planning-centric analysis of LLM agent failures; relevant to Embodied CAD's geometric reasoning constraints
