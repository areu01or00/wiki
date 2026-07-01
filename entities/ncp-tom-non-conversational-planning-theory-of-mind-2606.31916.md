---
title: "Theory of Mind and Persuasion Beyond Conversation: Assessing the Capacity of LLMs to Induce Belief States via Planning and Action"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, evaluation, llm, theory-of-mind, agentic-ai, alignment]
sources: ["https://arxiv.org/abs/2606.31916"]
---

# Theory of Mind and Persuasion Beyond Conversation: Assessing the Capacity of LLMs to Induce Belief States via Planning and Action

## Overview
Introduces Non-Conversational Planning ToM (NCP-ToM), a framework evaluating whether LLMs can induce specific belief states in other agents through actions rather than dialogue. Surfaces a critical gap in ToM evaluation: prior benchmarks use passive Q&A, but agentic deployments require active belief-state induction via physical/action planning. GPT-5 achieves ~80% on agentic tasks, outperforming humans, but all models show true-belief > false-belief asymmetry.

## Key Facts
- **arXiv**: [2606.31916](https://arxiv.org/abs/2606.31916)
- **Year**: 2026

## Key Contributions
- First framework for evaluating LLM belief-state induction via non-conversational planning (NCP-ToM)
- Novel task structure: agents move objects or direct characters into rooms to achieve belief-state goals
- Benchmark of 600 task instances across 6 frontier models + human cohort
- First evidence that frontier LLMs (GPT-5) can outperform humans on agentic social-reasoning tasks
- Documents true-belief > false-belief asymmetry across all models — alignment-relevant signal
- Identifies manipulation/misinformation risk from non-conversational belief induction capabilities

## Related Papers
- [[decompose-tom-enhancing-theory-mind-reasoning-through-simulation-and-task-decomposition-2501.09056]] — Prior ToM decomposition approach (shares task-decomposition sub-problem)
- [[persuasivetom-benchmark-evaluating-machine-theory-mind-in-persuasive-dialogues-2502.21017]] — Persuasive ToM via dialogue (conversational counterpart to NCP-ToM's non-conversational setting)
