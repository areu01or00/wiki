---
title: "ComplianceGate: Classifier-Gated Multi-Tier LLM Routing for Inference in Regulated Industries"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [llm-deployment, routing, compliance, regulated-industries, inference-efficiency]
sources: ["https://arxiv.org/abs/2606.31163"]
---

# ComplianceGate: Classifier-Gated Multi-Tier LLM Routing for Inference in Regulated Industries

## Overview
Large language models in regulated industries face dual constraints: compliance enforcement and cost efficiency. PII in user queries can reach model endpoints before routing decisions are made. This paper proposes a classifier-gated routing architecture where a trained encoder sits before any decoder inference, evaluating each query for complexity and data sensitivity, then routing to an appropriately sized model in the appropriate geographic location. Achieves 39% median latency reduction, 33-52% cost savings, and 99.2% PII classification accuracy at 7ms overhead.

## Key Facts
- **arXiv**: [2606.31163](https://arxiv.org/abs/2606.31163)
- **Date**: 2026-06-01

## Key Contributions
- Classifier-gated pre-inference routing architecture — PII queries route to local endpoints before any LLM computation begins
- Trained encoder classifier evaluates query complexity and data sensitivity before decoder inference
- Geographic routing to appropriate jurisdiction before computation
- 39% median latency reduction, 33-52% cost savings
- 99.2% PII classification accuracy with 7ms inference overhead
- 122-200 tokens/second throughput vs 50-64 baseline

## Related Papers
- [[grace-granularity-regulated-adaptive-computational-efficiency-for-optimal-verification-in-test-time-scaling-2606.19354]] — GRACE: Related via test-time efficiency — both address adaptive computational efficiency in LLM deployment
- [[a-theoretical-model-for-task-routing-in-mixture-of-expert-transformers-2606.14398]] — Task Routing MoE: Related via routing theory — both address routing decisions in LLM systems
- [[beyond-goodharts-law-a-dynamic-benchmark-for-evaluating-compliance-in-multi-agent-systems-2606.07805]] — Beyond Goodhart's Law: Related via compliance benchmarking — both address compliance in multi-agent LLM deployments
