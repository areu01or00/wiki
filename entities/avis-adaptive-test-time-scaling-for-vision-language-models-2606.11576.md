---
title: "AVIS: Adaptive Test-Time Scaling for Vision-Language Models"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [test-time-compute, vlm, adaptive-inference, efficiency]
sources: ["https://arxiv.org/abs/2606.11576"]
---

# AVIS: Adaptive Test-Time Scaling for Vision-Language Models

## Overview
AVIS (Adaptive Visual Inference Scaling) introduces a lightweight, sample-dependent policy for test-time compute allocation in Vision-Language Models. Given a target workload, AVIS predicts optimal per-sample inference configurations over both Visual Context Scaling (VCS) and Visual Reasoning Scaling (VRS), reducing inference cost while maintaining quality.

## Key Facts
- **Authors**: Jeddi, Ahmadreza; Le, Minh Ngoc; Kazerouni, Amirhossein + 8
- **Year**: 2026
- **arXiv**: [2606.11576](https://arxiv.org/abs/2606.11576)

## Key Contributions
- Novel framework for adaptive, per-sample test-time compute allocation in VLMs
- Joint optimization over visual context scaling and visual reasoning scaling axes
- Sample-dependent policy that predicts optimal inference configuration per input
- Significant inference cost reduction without quality degradation

## Related Papers
- [[thinkbooster-a-unified-framework-for-seamless-test-time-scaling-2606.06915]] — Unified test-time scaling framework for LLM reasoning (broader paradigm)
- [[when-more-thinking-hurts-overthinking-in-llm-test-time-compute-2604.10739]] — Overthinking phenomenon demonstrating that longer CoT doesn't always yield better results
- [[grace-granularity-regulated-adaptive-computational-efficiency-for-optimal-verification-in-test-time-scaling-2606.19354]] — Granularity-regulated adaptive compute for test-time scaling verification
