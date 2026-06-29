---
title: "LLM-as-Code: Agentic Programming for Agent Harness"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agent, programming, llm, framework]
sources: ["https://arxiv.org/abs/2606.15874"]
---

# LLM-as-Code: Agentic Programming for Agent Harness

## Overview
Challenges the dominant "LLM-as-orchestrator" paradigm where the model controls all control flow. Proposes Agentic Programming where the program governs control flow and the LLM is invoked only where reasoning or generation is needed — an "LLM-as-Code" adaptive component. Within each call the model keeps full flexibility but cannot alter the execution path. The LLM's context is built from the call tree DAG of execution history.

## Key Facts
- **Authors**: Junjia Qi, Zichuan Fu, Jingtong Gao, Wenlin Zhang, Hanyu Yan, Xian Wu, Xiangyu Zhao
- **Year**: 2026
- **arXiv**: [2606.15874](https://arxiv.org/abs/2606.15874)

## Key Contributions
- **LLM-as-Code**: LLM as an adaptive component invoked by program control flow, not the orchestrator
- **Program governs control flow**: DAG-structured call tree from execution history provides LLM context
- **Full flexibility within calls**: model retains reasoning/generation autonomy within each call boundary
- **Structural context**: LLM context = execution history call tree (DAG), not flat scratchpad

## Related Papers
- [[agent-orchestration]] — General agent orchestration frameworks
- [[skilldag-self-evolving-typed-skill-graphs-for-llm-skill-selection-at-scale-2606.03056]] — Skill graph reasoning for LLM agents (orthogonal axis: skill-graph-DAG vs execution-history-DAG)
