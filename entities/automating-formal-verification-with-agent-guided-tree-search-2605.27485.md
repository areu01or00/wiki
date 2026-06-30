---
title: "Automating Formal Verification with Agent-Guided Tree Search"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [reasoning, formal-verification, llm-agent, theorem-proving, search]
sources: ["https://arxiv.org/abs/2605.27485"]
---

# Automating Formal Verification with Agent-Guided Tree Search

## Overview
This thesis evaluates LLM-driven verified-code generation ("vericoding") in Lean and develops search-based methods for improving verification performance. It introduces agentic loops with mathlib search and two agent-directed tree-search formulations: a state-based orchestrator that branches on partial-proof states, and a context-based orchestrator that branches on full subagent contexts. GPT-5.4 nearly saturates the benchmark at 95.0% on 423 specs with $K=50$ LLM calls.

## Key Facts
- **Authors**: Leo (MIT)
- **Year**: 2025
- **arXiv**: [2605.27485](https://arxiv.org/abs/2605.27485)

## Key Contributions
- Reproduces vericoding-benchmark Lean leaderboard across cross-vendor model pool
- Develops iterative agentic loop with mathlib search that greatly improves model performance
- Designs two tree-search formulations: state-based and context-based orchestrators
- Context-based design solves wider range of intermediate-difficulty specs at lower token cost; agent baseline retains advantage on hardest specs

## Related Papers
- [[seva-self-evolving-verification-agent-process-reward-fact-attribution-2606.29713]] — SEVA: Self-Evolving Verification Agent with Process Reward — orthogonal verification-agent approach with process reward gradients
- [[process-verified-reinforcement-theorem-proving-lean-2606.20068]] — Process-VR: Lean as Process-Level Reward Oracle — first use of Lean as symbolic process oracle during RL training
- [[a-verifiable-search-is-not-a-learnable-chain-of-thought-2606.21884]] — Verifiable Search: contrasts chain-of-thought with search-based verification approaches
