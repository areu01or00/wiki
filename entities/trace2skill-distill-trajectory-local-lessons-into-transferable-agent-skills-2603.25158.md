---
title: "Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [llm, alignment, safety, jailbreak, knowledge-editing, agent, skill-distillation]
sources: ["https://arxiv.org/abs/2603.25158"]
---

# Trace2Skill: Distill Trajectory-Local Lessons into Transferable Agent Skills

## Overview
Trace2Skill addresses the skill acquisition bottleneck in LLM agents by distilling broad execution trajectories into compact, transferable skill modules. Rather than requiring manual skill authoring or relying on parametric knowledge, it performs inductive reasoning over agent execution traces to identify reusable operational patterns. The framework consolidates trajectory-level lessons into a structured skill directory, enabling agents to rapidly acquire domain-specific skills that transfer across tasks.

## Key Facts
- **arXiv**: [2603.25158](https://arxiv.org/abs/2603.25158)
- **Submitted**: 2026-05-DD (from arxiv ID prefix)
- **Theme**: LLM agents / skill distillation / trajectory learning

## Key Contributions
- First trajectory-to-skill distillation framework via inductive reasoning over execution traces
- Unified skill directory enabling cross-task transfer for LLM agents
- Handles operational pitfalls that purely parametric skill generation misses
- Empirically validates skill transfer on 12 diverse agent domains


## Related Papers
- [[emergent-concepts]] — Emergent Concepts parent page
