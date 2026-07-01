---
title: "Context-Aware RL for Agentic and Multimodal LLMs"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [reinforcement-learning, llm, multimodal, agentic, context]
sources: ["https://arxiv.org/abs/2606.17053"]
---

# Context-Aware RL for Agentic and Multimodal LLMs

## Overview
LLMs often fail when the answer requires identifying a small but decisive piece of evidence within a long or complex context. ContextRL introduces an indirect auxiliary objective: contrastive context selection — given a query, answer, and two similar contexts, reward the model for choosing the context that correctly supports the query-answer pair. This encourages fine-grained grounding without directly supervising the final answer.

## Key Facts
- **Authors**: (from arxiv 2606.17053)
- **Year**: 2026
- **arXiv**: [2606.17053](https://arxiv.org/abs/2606.17053)

## Key Contributions
- Contrastive context selection as RL auxiliary objective for long-horizon reasoning and multimodal understanding
- ContextRL outperforms GRPO by +2.2% on 5 long-horizon benchmarks and +1.8% on 12 VQA benchmarks
- Ablation confirms gains come from the context-selection objective, not the contrastive data alone
- Two data construction domains: coding agent trajectories (1K pairs) and multimodal images (7K pairs via generative editing)

## Related Papers
- [[osworld20-benchmarking-computer-use-agents-on-long-horizon-real-world-tasks-2606.29537]] — Long-horizon agent benchmarking
- [[agent-world-scaling-real-world-environment-synthesis-for-evolving-general-agent-intelligence-2604.18292]] — Agent environment scaling
- [[qwen-agentworld-language-world-models-for-general-agents-2606.24597]] — World models for agents
