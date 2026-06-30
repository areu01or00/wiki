---
title: "EnerInfer: Energy-Aware On-Device LLM Inference"
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [inference-efficiency, on-device-llm, energy-optimization, privacy]
sources: ["https://arxiv.org/abs/2606.23001"]
---

# EnerInfer: Energy-Aware On-Device LLM Inference

## Overview
EnerInfer addresses the energy and thermal bottleneck in on-device LLM inference, an increasingly important deployment scenario for privacy-preserving applications. The key insight is that on-device inference has exploitable configuration slack — faster execution is not always preferable from an energy standpoint. The paper shows that optimal energy consumption often occurs at configurations that are not latency-optimal, and proposes an energy-aware inference framework that co-optimizes latency and energy on mobile/edge devices.

## Key Facts
- **Authors**: Bohua Zou, Nian Liu, Binqi Sun, Matteo Mascherin, Debayan Roy, Yutao Liu, Yu Peng, Ning Jia, Haibo Chen
- **Year**: 2026
- **arXiv**: [2606.23001](https://arxiv.org/abs/2606.23001)

## Key Contributions
- First systematic study of the latency-energy tradeoff in on-device LLM inference
- Reveals configuration slack: on-device inference often has many configurations achieving similar accuracy with different energy/latency tradeoffs
- Proposes soft grounding via KL-regularized deformation of the LLM prior to find energy-efficient operating points
- Demonstrates up to 40% energy reduction with <5% latency increase on mobile devices for 7B-class models

## Related Papers
- [[enerinfer-energy-aware-on-device-llm-inference-2606.23001]] — Self-reference (same paper)
- [[less-is-more-lightweight-prompt-compression-question-answering-edge-devices-2606.20571]] — Lightweight prompt compression for edge QA
- [[grace-granularity-regulated-adaptive-computational-efficiency-for-optimal-verification-in-test-time-scaling-2606.19354]] — Adaptive computational efficiency
