---
title: "JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [inference-efficiency, speculative-decoding, llm, serving]
sources: ["https://arxiv.org/abs/2606.18394"]
---

# JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting

## Overview
JetSpec proposes a head-based speculative decoding framework that combines one-forward drafting efficiency with branch-wise causal conditioning, breaking the scaling ceiling where prior SD methods plateau because of a causality-efficiency dilemma. The approach trains a causal parallel draft head over fused hidden states from the frozen target model, producing candidate trees whose scores align with the target model's autoregressive factorization and converting larger draft budgets into longer accepted prefixes and higher end-to-end speedup. Across dense and MoE Qwen3 models on math, coding, and chat workloads, JetSpec achieves up to 9.64x speedup on MATH-500 and 4.58x on conversational serving, with additional gains demonstrated via vLLM integration.

## Key Facts
- **Authors**: Hu, Lanxiang; Feng, Zhaoxiang; Wu, Yulun; Yuan, Haoran; Zhao, Yujie; Qian, Yu-Yang; Wang, Bojun; Zhao, Peng; Jiang, Daxin; Zhu, Yibo
- **Year**: 2026
- **arXiv**: [2606.18394](https://arxiv.org/abs/2606.18394)

## Key Contributions
- Diagnoses a causality-efficiency dilemma in head-based speculative decoding: autoregressive drafters produce path-conditioned candidates with effective tree behavior but drafting cost grows with tree depth, while bidirectional block-diffusion drafters produce branch-agnostic marginals that form individually plausible yet mutually inconsistent trees, wasting budget and reducing acceptance.
- Proposes a head-based SD framework that combines one-forward drafting efficiency with branch-wise causal conditioning by training a causal parallel draft head over fused hidden states from the frozen target model.
- Demonstrates that the resulting candidate-tree scores align with the target model's autoregressive factorization, converting larger draft budgets into longer accepted prefixes and higher end-to-end speedup.
- Achieves up to 9.64x speedup on MATH-500 and 4.58x on open-ended conversational workloads on H100 GPUs, with further latency gains via vLLM integration under realistic serving loads.

## Related Papers
- [[emergent-concepts]] — Parent emergent-concept run that surfaced this paper