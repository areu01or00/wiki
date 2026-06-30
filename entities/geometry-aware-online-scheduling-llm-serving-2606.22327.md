---
title: "Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice"
created: 2026-07-03
updated: 2026-07-03
type: entity
tags: [inference-efficiency, llm-serving, kv-cache, scheduling]
sources: ["https://arxiv.org/abs/2606.22327"]
---

# Geometry-Aware Online Scheduling for LLM Serving: From Theoretical Bound to System Practice

## Overview
This paper addresses the KV cache memory management problem in LLM inference serving systems. It reveals that time-centric scheduling heuristics (like Shortest Job First) are theoretically suboptimal for KV cache management and proposes a geometry-aware approach that explicitly accounts for the spatial structure of cache allocation. The work bridges theoretical optimality bounds with practical system design for interactive LLM serving.

## Key Facts
- **Authors**: Li Kong, Qi Qi, Yinyu Ye, Zijie Zhou
- **Year**: 2026
- **arXiv**: [2606.22327](https://arxiv.org/abs/2606.22327)

## Key Contributions
- First theoretical characterization of KV cache scheduling as a geometry problem rather than a time problem
- Shows Shortest Job First is suboptimal for KV cache because it ignores the spatial locality structure of cache allocations
- Proposes geometry-aware scheduling that exploits the 2D spatial structure of cache footprint (sequence length × batch size)
- Evaluates on production LLM serving traces showing up to 23% memory efficiency improvement over time-centric baselines

## Related Papers
- [[coverage-driven-kv-cache-eviction-kvec-2606.29563]] — KV cache eviction strategy complementary to scheduling
- [[information-aware-kv-cache-compression-for-long-reasoning-2606.26875]] — KV cache compression for long context
- [[refreekv-towards-threshold-free-kv-cache-compression-2502.16886]] — Threshold-free KV cache compression methodology
