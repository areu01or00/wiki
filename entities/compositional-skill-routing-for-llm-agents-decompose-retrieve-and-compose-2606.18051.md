---
title: "Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [agent, skill-routing, tool-use, retrieval-augmented, compositional-planning]
sources: ["https://arxiv.org/abs/2606.18051"]
---

# Compositional Skill Routing for LLM Agents: Decompose, Retrieve, and Compose

## Overview
This paper formalizes the Compositional Skill Routing problem: given a complex user query and a large skill library, decompose the query into atomic sub-tasks, retrieve the appropriate skill for each sub-task, and compose an executable plan. The authors introduce SkillWeaver (decompose-retrieve-compose framework combining an LLM task decomposer, bi-encoder skill retriever with FAISS, and dependency-aware DAG planner) and CompSkillBench (300 compositional queries over 2,209 MCP server skills). Task decomposition quality is identified as the primary bottleneck.

## Key Facts
- **Authors**: Unknown (from arxiv 2606.18051)
- **Year**: 2026
- **arXiv**: [2606.18051](https://arxiv.org/abs/2606.18051)

## Key Contributions
- Compositional Skill Routing formalization: decompose-retrieve-compose for complex multi-skill task execution
- SkillWeaver framework: LLM task decomposer + bi-encoder FAISS retriever + dependency-aware DAG planner
- CompSkillBench: 2,209 MCP server skills across 24 categories; decomposition quality is primary bottleneck (34.2% recall at step level)
- Iterative Skill-Aware Decomposition (SAD): retrieval-augmented feedback loop improves decomposition accuracy from 51.0% to 67.7%
- >99% context window reduction via compositional routing vs. full skill library

## Related Papers
- [[declarative-router-policy-compilation-from-inference-routing-to-agent-orchestration-cross-layer-verification-2603.27299]] — Declarative Router Policy Compilation for Agent Orchestration (related routing/verification)
- [[skilldag-self-evolving-typed-skill-graphs-for-llm-skill-selection-at-scale-2606.03056]] — SkillDAG: Self-Evolving Typed Skill Graphs for LLM Skill Selection (related skill graph/skill selection)
- [[notes2skills-from-lab-notebooks-to-certainty-aware-scientific-agent-skills-2606.11897]] — Notes2Skills: From Lab Notebooks to Certainty-Aware Scientific Agent Skills (related scientific agent skill acquisition)
