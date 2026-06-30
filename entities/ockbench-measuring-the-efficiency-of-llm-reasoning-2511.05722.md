---
title: "OckBench: Measuring the Efficiency of LLM Reasoning"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [evaluation, efficiency, llm, benchmarking]
sources: ["https://arxiv.org/abs/2511.05722"]
---

# OckBench: Measuring the Efficiency of LLM Reasoning

## Overview
OckBench is the first benchmark that jointly measures accuracy AND token efficiency across reasoning and coding tasks. It addresses a critical gap in LLM evaluation: current benchmarks emphasize accuracy while ignoring the 5.0× token-length variance between models solving the same problem at similar accuracy. OckBench establishes token-per-correct-output as a standardized evaluation dimension.

## Key Facts
- **Authors**: Zheng Du, Hao Kang, Song Han, Tushar Krishna, Ligeng Zhu
- **Year**: 2025
- **arXiv**: [2511.05722](https://arxiv.org/abs/2511.05722)

## Key Contributions
- First joint accuracy + token-efficiency benchmark for LLMs
- Reveals up to 5.0× token-length variance between models at similar accuracy
- Shows token efficiency remains largely unoptimized across current models
- Proposes evaluation paradigm shift: tokens must not be multiplied beyond necessity
- Provides concrete roadmap for optimizing latent reasoning ability alongside token efficiency

## Related Papers
- [[wisparse-boosting-inference-efficiency-weight-aware-mixed-2602.14452]] — Weight-aware mixed-precision inference efficiency; orthogonal axis (Wisparse targets weight-compression efficiency, OckBench targets token-length efficiency)
- [[rope-aware-bit-allocation-for-kv-cache-quantization-2606.24033]] — KV-cache compression; orthogonal axis (rope-aware targets memory-bandwidth efficiency, OckBench targets per-token efficiency)
- [[counsel-a-meta-evaluation-dataset-for-agentic-tasks-2606.21627]] — Meta-evaluation of agentic task performance; orthogonal axis (Counsel evaluates agent trajectory quality, OckBench evaluates token efficiency as a standalone evaluation dimension)
