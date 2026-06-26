---
title: "Query-Conditioned Test-Time Self-Training for Large Language Models"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [test-time-training, self-training, query-conditioned, parameter-efficient, llm, reasoning, math]
sources: ["https://arxiv.org/abs/2605.13369"]
---

# Query-Conditioned Test-Time Self-Training for Large Language Models

## Overview
A test-time adaptation framework that adapts LLM parameters per-query using supervision derived *from the input query itself* — no external data, no generic self-supervised objective. QueST generates structurally related problem–solution pairs conditioned on the input query, then uses them as supervision for parameter-efficient fine-tuning at test time. The adapted model produces the final answer, enabling query-specific adaptation. Outperforms strong test-time-optimization baselines on 7 math benchmarks + GPQA-Diamond.

## Key Facts
- **Authors**: Song, Chaehee; Seo, Minseok; Seong, Yeeun (and collaborators)
- **Year**: 2026
- **arXiv**: [2605.13369](https://arxiv.org/abs/2605.13369)
- **Online date**: 2026-05-14

## Key Contributions
- **Query-conditioned test-time self-training (QueST)** — the input query encodes latent signals sufficient for constructing structurally related problem-solution pairs; those pairs serve as supervision for parameter-efficient fine-tuning at test time. This is the first **per-query parameter adaptation** primitive in the wiki that doesn't rely on external data.
- **Decoupling adaptation from external supervision** — existing test-time optimization either relies on external data or optimizes generic self-supervised objectives (like entropy minimization) that lack query-specific alignment. QueST shows the input query itself is a sufficient signal source — a strong claim about the information content of natural-language inputs.
- **Consistent gains on math + scientific reasoning** — 7 mathematical reasoning benchmarks + GPQA-Diamond scientific reasoning, outperforming strong test-time-optimization baselines. The win is structural (per-query adaptation works), not just incremental.

## Why this matters for the wiki
**First query-conditioned-test-time-training primitive in the wiki.** Bridges Run 65's [SFT-vs-RL unified-objective framework](#) (training-side post-training primitives) and Run 64's [Towards-a-Science-of-Scaling-Agent-Systems](#) (deployment-side scaling primitives) — QueST says *you can do training-time adaptation at test time*, collapsing the train/deploy boundary per-query. The "input query as supervision signal" framing is a structural primitive that future self-training work will need to cite.

## Related Papers
- [[efficient-and-trainable-language-model-test-time-scaling-via-local-branch-routing-2606.25354]] — Trainable test-time scaling via local-branch routing; sibling test-time primitive but uses routing rather than per-query parameter updates
- [[supervised-fine-tuning-versus-reinforcement-learning-a-study-of-post-training-methods-for-large-language-models-2603.13985]] — SFT-vs-RL unified-objective framework; complementary paper from Run 65 showing the full training-time post-training primitive family. QueST extends this line into test-time per-query adaptation.
- [[attribution-guided-continual-learning-for-llms-2605.05285]] — Gradient modulation for continual learning; sibling training-side primitive from Run 63. QueST borrows the parameter-efficient-fine-tuning primitive from continual-learning and applies it at test-time.