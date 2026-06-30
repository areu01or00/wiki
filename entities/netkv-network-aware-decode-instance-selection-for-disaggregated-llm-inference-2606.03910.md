---
title: "NetKV: Network-Aware Decode Instance Selection for Disaggregated LLM Inference"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [llm-inference, kv-cache, disaggregated-serving, memory-efficiency]
sources: ["https://arxiv.org/abs/2606.03910"]
---

# NetKV: Network-Aware Decode Instance Selection for Disaggregated LLM Inference

## Overview
NetKV addresses the KV cache network transfer bottleneck in disaggregated LLM inference. Current schedulers route based on compute load and prefix-cache locality, ignoring topological distance and congestion between prefill and decode instances. NetKV closes this gap with a thin operator that accounts for network topology.

## Key Facts
- **Authors**: NetKV Team
- **Year**: 2026
- **arXiv**: [2606.03910](https://arxiv.org/abs/2606.03910)

## Key Contributions
- Network-topology-aware decode instance selection for disaggregated LLM inference
- Addresses KV cache transfer time entering Time to First Token (TTFT) budget
- Complements HMA-Serve (2606.29986) disaggregated serving work — NetKV focuses on network routing, HMA-Serve on memory heterogeneity
- Thin operator design that integrates with existing disaggregated inference frameworks

## Related Papers
- [[emergent-concepts]] — Parent emergent concepts chain
