---
title: "Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents"
created: "2026-06-30"
updated: "2026-06-30"
type: entity
tags: [agent-memory, unified-memory, LTM, STM, reinforcement-learning]
sources: ["https://arxiv.org/abs/2601.01885"]
---

# Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents

## Overview
AgeMem is a unified framework that integrates long-term memory (LTM) and short-term memory (STM) management directly into the LLM agent's policy, treating memory operations as tool-based actions the agent autonomously decides when to invoke. Unlike prior work that separates LTM/STM into independent subsystems with heuristic controllers, AgeMem enables end-to-end optimization of the full memory lifecycle — store, retrieve, update, summarize, and discard — via a three-stage progressive reinforcement learning strategy with step-wise GRPO addressing sparse/discontinuous rewards from memory operations.

## Key Facts
- **Authors**: Yi Yu, Liuyi Yao, Yuexiang Xie, Qingquan Tan, Jiaqi Feng, Yaliang Li, Libing Wu
- **Year**: 2026 (submitted Jan 5, 2026; last revised Apr 30, 2026)
- **arXiv**: [2601.01885](https://arxiv.org/abs/2601.01885)
- **Subjects**: Computation and Language (cs.CL)

## Key Contributions
- Unified LTM+STM management as policy-learned tool actions (store, retrieve, update, summarize, discard) rather than heuristic sub-systems
- Three-stage progressive RL strategy with step-wise GRPO addressing sparse/discontinuous reward signals inherent to memory operations
- Experiments on 5 long-horizon benchmarks (ALFWorld, WebShop, MiniWob++, etc.) show AgeMem consistently outperforms strong memory-augmented baselines across multiple LLM backbones
- Higher-quality long-term memory and more efficient context usage vs. separate-LTM/STM approaches
- First unified LTM+STM joint optimization via learned memory-as-tool policy in the wiki

## Related Papers
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — EvoEmbedding: evolvable agentic memory representations via representation surgery; orthogonal to AgeMem's learned memory-operation policy (EvoEmbedding = fixed-representation adaptation, AgeMem = learned when/what memory operations to perform)
- [[memprobe-probing-longterm-agent-memory-via-hidden-userstate-recovery-2606.24595]] — MEMPROBE: probing long-term agent memory via hidden user-state recovery; orthogonal to AgeMem (MEMPROBE = memory evaluation benchmark, AgeMem = memory management methodology)
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Plans Don't Persist: context management as load-bearing for LLM agents; complementary framing (Plans-Dont-Persist identifies the problem, AgeMem provides the learned solution architecture)
