---
title: "ODAR: Principled Adaptive Routing for LLM Reasoning via Active Inference"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [test-time-compute, active-inference, free-energy, adaptive-routing, llm-reasoning, primitive]
sources: ["https://arxiv.org/abs/2602.23681"]
---

# ODAR: Principled Adaptive Routing for LLM Reasoning via Active Inference

## Overview
Proposes **ODAR-Expert**, an adaptive routing framework that replaces uniform brute-force test-time compute (fixed Best-of-N, self-consistency) with difficulty-aware routing between a heuristic Fast Agent and a deliberative Slow Agent. The difficulty estimator is grounded in **amortized active inference** and the answer-fusion mechanism is derived from the **variational free energy principle**, balancing log-likelihood with epistemic uncertainty (varentropy) as a principled alternative to ad hoc voting. Achieves 98.2% on MATH and 54.8% on Humanity's Last Exam while reducing compute by 82% on a fully open-source stack (Llama 4 + DeepSeek).

## Key Facts
- **Authors**: Ma, Siyuan; Gao, Bo; Jia, Xiaojun; Qin, Simeng; Li, Tianlin; Ma, Ke; Jia, Xiaoshuang; Ren, Wenqi; Liu, Yang
- **Year**: 2026
- **arXiv**: [2602.23681](https://arxiv.org/abs/2602.23681)
- **Citation date**: 2026-02-27 (online 2026-02-27)

## Key Contributions
- **Active-inference-grounded difficulty estimator**: estimates per-query difficulty via amortized active inference (a principled Bayesian framework), routing easy queries to a Fast Agent and hard queries to a Slow Agent — replacing uniform brute-force sampling.
- **Free-energy-principled fusion**: replaces ad hoc voting over heterogeneous samples with minimization of a variational free energy objective that explicitly balances log-likelihood with epistemic uncertainty (varentropy).
- **Risk-sensitive answer selection**: varentropy term provides principled risk-aversion, addressing the overthinking-with-diminishing-returns pathology of fixed-budget sampling.
- **Compute-accuracy frontier improvement**: 98.2% MATH / 54.8% HLE while reducing computational cost by 82% on Llama 4 + DeepSeek open-source stack; validated across 23 benchmarks.

## Related Papers
- [[taro-token-level-adaptive-routing-llm-test-time-alignment-2603.18411]] — Sibling token-level adaptive routing primitive for LLM test-time alignment
- [[adaptive-test-time-compute-allocation-for-reasoning-llms-via-constrained-policy-optimization-2604.14853]] — Sibling run-mate: constrained-policy-optimization test-time-compute allocation (complementary: budget-constrained vs. difficulty-routed)
- [[thinkbooster-a-unified-framework-for-seamless-test-time-scaling-2606.06915]] — Sibling unified test-time-scaling framework integrating sequential and parallel modes