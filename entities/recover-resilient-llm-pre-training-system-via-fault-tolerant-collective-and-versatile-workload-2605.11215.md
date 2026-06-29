---
title: "ReCoVer: Resilient LLM Pre-Training System via Fault-Tolerant Collective and Versatile Workload"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [training-infrastructure, fault-tolerance, distributed-systems]
sources: ["https://arxiv.org/abs/2605.11215"]
---

# ReCoVer: Resilient LLM Pre-Training System via Fault-Tolerant Collective and Versatile Workload

## Overview
Pre-training LLMs on massive GPU clusters makes hardware faults routine rather than rare, creating a need for resilient training systems. ReCoVer is a resilient LLM pre-training system that maintains a single critical invariant: each iteration recovers to a failure-free training trajectory. Unlike prior frameworks that focus on specific parallelism schemes or risk trajectory drift, ReCoVer provides fault-tolerant collective communication and versatile workload distribution across heterogeneous GPU clusters.

## Key Facts
- **Authors**: Ziyue Liu, Zhengyang Wang, Ruijie Zhang, Avinash Maurya, Hui Zhou, Paul Hovland, Sheng Di, Franck Cappello, Bogdan Nicolae
- **Year**: 2026
- **arXiv**: [2605.11215](https://arxiv.org/abs/2605.11215)

## Key Contributions
- Fault-tolerant collective communication primitives that survive GPU/node failures without losing training progress
- Single-iteration recovery invariant — each failure recovery resumes from exact failure-free state
- Versatile workload distribution handling heterogeneous GPU cluster topologies
- Scales across multiple parallelism strategies (tensor/pipeline/data) without framework lock-in
- Characterizes the failure taxonomy in large-scale LLM pre-training (checkpoint corruption, silent data corruption, network partition)

## Related Papers
- [[repot-recoverable-program-of-thought-via-checkpoint-repair-2605.30052]] — Checkpoint repair for recoverable program-of-thought (complementary checkpoint resilience)
