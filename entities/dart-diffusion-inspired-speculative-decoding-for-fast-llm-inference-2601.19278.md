---
title: "DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [inference-efficiency, speculative-decoding, diffusion-llm, parallel-generation]
sources: ["https://arxiv.org/abs/2601.19278"]
---

# DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference

## Overview
Replaces the autoregressive draft stage of speculative decoding with **parallel logit prediction over multiple future positions in a single forward pass**, inspired by diffusion-LLMs (dLLMs). Predicts logits for masked future positions from hidden states of the target model, eliminating autoregressive rollouts in the draft model while preserving a lightweight design. Combined with an N-gram-enforced tree-pruning algorithm, achieves 2.03x–3.44x wall-clock speedups and outperforms EAGLE3 by 30% on average.

## Key Facts
- **Authors**: Liu, Fuliang; Li, Xue; Zhao, Ketai; Gao, Yinxi; Zhou, Ziyan; Zhang, Zhonghui; Wang, Zhibin; Dou, Wanchun; Zhong, Sheng; Tian, Chen
- **Year**: 2026
- **arXiv**: [2601.19278](https://arxiv.org/abs/2601.19278)
- **Online date**: 2026-01-27
- **Code**: https://github.com/fvliang/DART

## Key Contributions
- **Non-autoregressive-parallel-drafting primitive**: DART predicts logits for *multiple future positions in parallel* in a single forward pass — the draft stage is no longer autoregressive. The drafting-stage bottleneck that motivated every prior model-based draft design (EAGLE3, Medusa, etc.) is structurally eliminated
- **dLLM-inspired-from-target-hidden-states primitive**: instead of training a separate draft model, DART derives draft logits directly from the *target model's hidden states* — reuses compute already done, makes the "draft model" effectively free at training time
- **N-gram-enforced-semantic-continuity tree pruning primitive**: constructs high-quality draft token trees that respect N-gram constraints during parallel decoding — addresses the failure mode where parallel prediction produces locally incoherent token sequences
- **Draft-stage-overhead-as-binding-constraint primitive**: identifies that prior speculative decoding was draft-bound (not verify-bound), and demonstrates that eliminating draft-stage autoregression is the load-bearing optimization — 30% over EAGLE3 with no model retraining
- **Lightweight design preservation**: no auxiliary draft model, no retraining of target model — DART is a drop-in replacement for the draft stage, addressing inference-eff deployment constraints

## Related Papers
- [[efficientrollout-system-aware-self-speculative-decoding-for-rl-rollouts-2606.18967]] — System-aware speculation for non-stationary RL rollouts; sibling inference-eff primitive
- [[jetspec-breaking-the-scaling-ceiling-of-speculative-decoding-with-parallel-tree-2606.18394]] — Parallel tree drafting for scaling-ceiling; this paper goes further by *eliminating autoregression* in the draft
- [[vericache-turning-lossy-kv-cache-into-lossless-llm-inference-2605.17613]] — Lossless recovery from lossy KV caches; sibling inference-eff primitive addressing a different inference cost dimension
- [[improved-large-language-diffusion-models-2606.25331]] — Large LDM improvements; this paper applies dLLM's parallel-generation insight to *speculative decoding*, the first direct cross-pollination between the two lines