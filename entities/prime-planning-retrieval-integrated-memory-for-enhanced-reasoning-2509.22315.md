---
title: "PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reasoning"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [dual-process, memory, reasoning, multi-agent]
sources: ["https://arxiv.org/abs/2509.22315"]
---

# PRIME: Planning and Retrieval-Integrated Memory for Enhanced Reasoning

## Overview
PRIME operationalizes dual-process theory (Thinking, Fast and Slow) as a multi-agent reasoning framework. A Quick Thinking Agent (System 1) generates rapid answers; if uncertainty is detected, it triggers a System 2 pipeline of specialized agents for planning, hypothesis generation, retrieval, information integration, and decision-making. This architecture enables open-source LLMs to match closed-source GPT-4/4o on multi-hop and knowledge-intensive reasoning benchmarks.

## Key Facts
- **Authors**: Hieu Tran, Zonghai Yao, Nguyen Luong Tran, Zhichao Yang, Feiyun Ouyang, Shuo Han, Razieh Rah
- **Year**: 2025
- **arXiv**: [2509.22315](https://arxiv.org/abs/2509.22315)

## Key Contributions
- First dual-process System 1/System 2 architecture as multi-agent pipeline in the wiki
- Uncertainty-triggered switching between fast (System 1) and deliberate (System 2) reasoning
- Specialized agents for planning, hypothesis generation, retrieval, integration, and decision-making
- Enables open-source LLaMA 3 models to match GPT-4/4o on multi-hop reasoning benchmarks
- First dual-process theory operationalization as agent pipeline

## Related Papers
- [[think2-grounded-metacognitive-reasoning-in-large-language-models-2602.18806]] — Metacognitive regulatory cycle for adaptive effort allocation (different mechanism: single-agent prompting vs. multi-agent pipeline)
- [[spiral-symbolic-llm-planning-via-grounded-and-reflective-search-2512.23167]] — Symbolic planning via MCTS with specialized LLM agents (complementary: Spiral focuses on search-based planning, PRIME on dual-process memory integration)
- [[decompose-tom-enhancing-theory-mind-reasoning-through-simulation-and-task-decomposition-2501.09056]] — ToM via simulation+decomposition (PRIME's System 2 integrates planning/retrieval, broader than ToM-specific decomposition)
