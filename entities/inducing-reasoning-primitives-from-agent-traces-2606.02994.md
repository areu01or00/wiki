---
title: "Inducing Reasoning Primitives from Agent Traces"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, agent, primitive-extraction, trace-mining]
sources: ["https://arxiv.org/abs/2606.02994"]
---

# Inducing Reasoning Primitives from Agent Traces

## Overview
ReAct-style LLM agents frequently rediscover the same reasoning routines across diverse problems, yet these routines remain locked in transient scratchpad state and are never externalized. This paper introduces Reasoning Primitive Induction — a single-pass method that mines successful ReAct traces, clusters recurrent reasoning moves, and converts them into reusable, composable primitives that can be injected into future agent prompts.

## Key Facts
- **Authors**: Lei, Zhihan; Yan, Jiarui; Momo, Joshua + 1
- **Year**: 2026
- **arXiv**: [2606.02994](https://arxiv.org/abs/2606.02994)

## Key Contributions
- First method to extract reusable reasoning primitives from agent execution traces (single-pass mining + clustering)
- Compositional primitive library that boosts downstream agent performance on held-out tasks
- Empirical evidence that primitive repertoire size correlates with cross-domain generalization
- **First trace-mined reasoning primitive library in the wiki** — distinct from prior agent skill extraction approaches

## Related Papers
- [[compositional-skill-routing-for-llm-agents-decompose-retrieve-and-compose-2606.18051]] — Both surface compositional structure in agent behavior; RPI extracts primitives from execution while CSR decomposes at the skill level
- [[agent-skill-evaluation-and-evolution-frameworks-benchmarks-2606.11435]] — Both concern agent skill primitives; RPI is about inducing them from traces rather than designing them manually
- [[agents-last-exam-2606.05405]] — Both evaluate agents on reasoning tasks; RPI provides the primitive library that enables better reasoning performance
