---
title: "Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [serving, inference, energy-efficiency, gpu-scheduling, serverless, cluster-scheduling]
sources: ["https://arxiv.org/abs/2606.30391"]
---

# Energy-Aware Scheduling for Serverless LLM Serving on Shared GPUs

## Overview
Festina is a profiling-guided, power-aware control plane for minimizing cluster-wide energy in serverless LLM serving on shared GPUs. Unlike common global-local schedulers that optimize throughput or tail latency, Festina makes energy-first decisions by jointly coordinating request placement, SM partitioning, and GPU operating points under TTFT/TBT SLOs. Reduces energy consumption by up to 56% while maintaining SLO attainment within a 2% margin of throughput-optimized baselines.

## Key Facts
- **Authors**: Tianyu Wang, Gourav Rattihalli, Aditya Dhakal, Longfei Shangguan, Dejan Milojicic
- **Year**: 2026
- **arXiv**: [2606.30391](https://arxiv.org/abs/2606.30391)

## Key Contributions
- **Energy-first scheduling under SLO constraints** — jointly optimizes request placement, SM partitioning, and GPU operating points for energy minimization while meeting TTFT/TBT SLOs; first energy-centric scheduling for serverless LLM serving
- **Lightweight global constant-time placement** — fast SLO-safe energy-aware placement via offline profiles and GPU state summaries (no online optimization)
- **Phase-aware local GPU scheduler** — continuously adapts task batching and compute resources per GPU to minimize power consumption based on execution phase
- **SLO-aware workload consolidation** — reduces static power via migration to consolidate workloads; achieves 56% energy reduction vs throughput-optimized baselines with 2% SLO margin

## Related Papers
- [[cluster-route-escalate-cascaded-framework-for-cost-aware-llm-serving-2606.27457]] — related cost-aware LLM serving (Festina focuses on energy vs Cluster Route's cost-efficiency via quality routing)
- [[hbm-is-not-all-you-need-efficient-disaggregated-llm-serving-across-memory-heterogeneous-accelerators-2606.29986]] — related LLM serving efficiency
- [[flexserve-fast-secure-llm-serving-mobile-devices-flexible-resource-isolation-2606.23370]] — related serving infrastructure optimization
