---
title: "Video-MME-Logical: A Controlled Diagnostic Benchmark for Video Temporal-Logical Reasoning"
created: 2026-06-01
updated: 2026-06-01
type: entity
tags: [llm, post-training]
sources: ["https://arxiv.org/abs/2606.27828"]
---

# Video-MME-Logical: A Controlled Diagnostic Benchmark for Video Temporal-Logical Reasoning

## Overview
Video temporal-logical reasoning — maintaining, updating, and composing visual states as they evolve across frames — is a capability that existing video benchmarks conflate with scene complexity, static recognition, or uncontrolled temporal variation. Video-MME-Logical is a controlled diagnostic benchmark that isolates this specific capability by holding scene complexity constant while systematically varying temporal-logical structure, enabling precise measurement of MLLM temporal reasoning.

## Key Facts
- **arXiv**: [2606.27828](https://arxiv.org/abs/2606.27828)
- **Date**: 2026-06-01

## Key Contributions
- First controlled benchmark isolating video temporal-logical reasoning from scene complexity confounds
- Diagnostic evaluation framework: disentangles temporal-logical reasoning from static scene recognition in MLLMs
- Findings: current MLLMs (GPT-4V, Gemini, etc.) significantly underperform humans on temporal-logical tasks even when scene recognition is near-perfect
- Framework enables targeted capability diagnosis for video understanding in multimodal agents


## Related Papers
- [[emergent-concepts]] — Parent wiki page for emergent concept discoveries

## Theme Framing
**Axis**: Evaluation/benchmarking — video temporal-logical reasoning in multimodal LLMs
