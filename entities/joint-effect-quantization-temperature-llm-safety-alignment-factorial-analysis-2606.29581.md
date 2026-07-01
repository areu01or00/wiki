---
title: "The Joint Effect of Quantization and Sampling Temperature on LLM Safety Alignment: A Factorial Analysis"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [safety, quantization, alignment, deployment]
sources: ["https://arxiv.org/abs/2606.29581"]
---

# The Joint Effect of Quantization and Sampling Temperature on LLM Safety Alignment: A Factorial Analysis

## Overview
This paper investigates whether safety guarantees that hold under ideal deployment conditions (FP16, greedy decoding) remain intact when models are quantized and operated at non-zero sampling temperatures — two ubiquitous deployment optimizations that are rarely studied in combination for safety.

## Key Facts
- **Authors**: Prasad, Hari; Pal, Ritam
- **Year**: 2026
- **arXiv**: [2606.29581](https://arxiv.org/abs/2606.29581)

## Key Contributions
- First factorial evaluation of 9 instruction-tuned models × 3 precisions (FP16, GPTQ INT8, AWQ INT4) × 6 temperatures (T=0 to T=1.0)
- Reveals that quantization and temperature interact non-additively: some model families become *more* safe under quantization+stochastic sampling, while others become significantly less safe
- Quantified safety degradation thresholds across six model families; demonstrates that a model safe at FP16+greedy can become unsafe after INT4+moderate-temperature sampling
- Introduces practical guidance for deployment configurations that preserve safety alignment under realistic serving conditions

## Related Papers
- [[alignment-floor-persona-customization-breaks-safety-2605.27382]] — Alignment floor quantitative analysis; both papers probe safety degradation surfaces under deployment conditions
- [[multi-bitwidth-quantization-llms-additive-codebooks-2606.12876]] — Quantization methodology for LLMs; complementary on the compression axis
