---
title: "BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [inference-efficiency, llm, speculative-decoding]
sources: ["https://arxiv.org/abs/2606.31315"]
---

# BlockPilot: Instance-Adaptive Policy Learning for Diffusion-based Speculative Decoding

## Overview
BlockPilot addresses a fundamental limitation of diffusion-based speculative decoding: the use of a fixed block size across all inputs, ignoring that optimal block size varies per sample. The method learns a lightweight policy that predicts the optimal block size from prefilling representations, formulated as a single-shot decision after the prefilling stage. Achieves 5.92 average acceptance length and 4.20× speedup on Qwen3-4B at temperature T=1, with minimal overhead and seamless integration.

## Key Facts
- **Authors**: Anonymous (arXiv:2606.31315)
- **Year**: 2026
- **arXiv**: [2606.31315](https://arxiv.org/abs/2606.31315)

## Key Contributions
- **Instance-adaptive block size**: first method to predict optimal diffusion-based speculative decoding block size per input sample from prefilling representation, instead of using a fixed global block size
- **Low-dimensional structured decision space**: block size values exhibit local structure around the training block size, reducing the problem to a low-dimensional and structured decision space
- **Single-shot prediction**: block size predicted once after prefilling, introducing no additional per-token overhead — seamlessly integrable into existing systems
- **Plug-and-play**: evaluated on Qwen3-4B, achieves 5.92 acceptance length and 4.20× speedup at T=1 without architectural changes
- **First learned block-size policy for diffusion-based speculative decoding**: prior work assumed uniform optimal strategy; BlockPilot proves sample-adaptive policies outperform fixed strategies

## Related Papers
- [[specgen-accelerating-agentic-kernel-optimization-with-speculative-generation-2606.17518]] — SpecGen applies speculative generation to agentic kernel optimization; BlockPilot advances the inference efficiency substrate that enables such agents
- [[jetspec-breaking-the-scaling-ceiling-of-speculative-decoding-with-parallel-tree-2606.18394]] — JetSpec explores speculative decoding scaling ceilings via parallel tree structures; BlockPilot complements by learning instance-adaptive block sizes within the diffusion-based paradigm
