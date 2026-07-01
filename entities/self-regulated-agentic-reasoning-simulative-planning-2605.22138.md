---
title: "Efficient Agentic Reasoning Through Self-Regulated Simulative Planning"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [agentic-reasoning, planning, inference-efficiency]
sources: ["https://arxiv.org/abs/2605.22138"]
---

# Efficient Agentic Reasoning Through Self-Regulated Simulative Planning

## Overview
SR²AM (Self-Regulated Simulative Planning) decomposes efficient agentic reasoning into three systems: simulative reasoning (System II deep search), self-regulation (deciding when/how to plan), and reactive execution (fast System I responses). This controlled planning reduces token usage while maintaining accuracy, addressing the core inefficiency of end-to-end reactive agents that over-generate chain-of-thought without reliable accuracy gains.

## Key Facts
- **Authors**: Mingkai Deng, Jinyu Hou, Lara Sá Neves, Varad Pimpalkhute, Taylor W. Killian, Zhengzhong Liu, Eric P. Xing
- **Year**: 2026
- **arXiv**: [2605.22138](https://arxiv.org/abs/2605.22138)

## Key Contributions
- Three-system decomposition: simulative reasoning + self-regulation + reactive execution
- Self-regulation module learns when to invoke planning vs reactive execution — avoids wasteful chain-of-thought on easy queries
- Token-efficient: reduces reasoning length on simple tasks while maintaining accuracy on hard tasks
- First explicit planning-horizon control for agentic LLMs — the agent decides the depth of its own search

## Related Papers
- [[polaris-typed-planning-governed-execution-agentic-ai-2601.11816]] — POLARIS: Typed DAG Planning — structural plan verification complements SR²AM's planning-horizon control
- [[crystal-kv-efficient-kv-cache-management-chain-thought-2601.16986]] — Crystal-KV: KV cache efficiency for long CoT sequences
