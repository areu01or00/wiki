---
title: "ToolTree: Efficient LLM Agent Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent-planning, llm, tool-use, mcts]
sources: ["https://arxiv.org/abs/2603.12740"]
---

# ToolTree: Efficient LLM Agent Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning

## Overview
ToolTree addresses the challenge of LLM agent planning across diverse external tools by combining Monte Carlo Tree Search with dual-feedback mechanisms (upper confidence bound + value gradient) and bidirectional pruning. The approach significantly reduces the planning search space while maintaining solution quality for multi-step tool-use tasks.

## Key Facts
- **Authors**: Yang, Shuo; Han, Soyeon Caren; Ding, Yihao + 2
- **Year**: 2026
- **arXiv**: [2603.12740](https://arxiv.org/abs/2603.12740)

## Key Contributions
- Dual-feedback MCTS framework combining UCB and value gradient signals
- Bidirectional pruning for efficient tool planning search
- First systematic MCTS-based approach specifically for tool-use planning in LLM agents

## Related Papers
- [[constraint-tax-in-open-weight-llms-an-empirical-study-of-tool-calling-suppression-under-structured-output-constraints-2606.25605]] — Constraint Tax: prior tool-calling structured output work
