---
title: "Improved Large Language Diffusion Models"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [architecture, llm, diffusion, non-autoregressive, llm-research]
sources: ["https://arxiv.org/abs/2606.25331"]
---

# Improved Large Language Diffusion Models

## Overview
iLLaDA is an 8B masked diffusion language model trained from scratch, demonstrating that the masked-diffusion objective can match or exceed strong autoregressive baselines on standard language modeling and downstream reasoning benchmarks when scaled carefully. The paper introduces a curriculum-style noising schedule and a parallel-decoding inference strategy that make 8B-scale masked diffusion competitive with autoregressive LLMs at the same compute budget.

## Key Facts
- **Authors**: Nie, Shen, Min, Qiyang, Xu, Shaoxuan
- **Year**: 2026
- **Date**: 2026-06-24
- **arXiv**: [2606.25331](https://arxiv.org/abs/2606.25331)
- **Subjects**: Computation and Language (cs.CL)

## Key Contributions
- 8B masked diffusion language model (iLLaDA) trained from scratch that competes with autoregressive LLMs at matched compute
- Curriculum-style noising schedule that progressively widens the mask span during training
- Parallel-decoding inference strategy with no quality regression at long context
- Empirical evidence that the masked-diffusion vs autoregressive gap closes at the 8B scale with the right training recipe

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
