---
title: "CoAgent: Concurrency Control for Multi-Agent Systems"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [multi-agent-systems, concurrency-control, llm-agents, system-architecture]
sources: ["https://arxiv.org/abs/2606.15376"]
---

# CoAgent: Concurrency Control for Multi-Agent Systems

## Overview
CoAgent addresses a fundamental gap: when multiple LLM agents mutate shared state (git tree, Kubernetes cluster, documents) in parallel, classical concurrency control (2PL, OCC) fails because LLM transactions span minutes of inference with opaque read sets and speculative writes. The paper introduces MTPO (Monotonic Trajectory Pre-Order), which replaces blocking locks with advisory control — the runtime informs agents of conflicts, and each agent judges and repairs exactly the operations that depended on the invalidated state. At quiescence the run is serializable in a pre-decided order.

## Key Facts
- **Authors**: Lyu, Dingyan Zhang, Mingyu Wu, Xingda Wei, Haibo Chen
- **Year**: 2026
- **arXiv**: [2606.15376](https://arxiv.org/abs/2606.15376)

## Key Contributions
- **MTPO Protocol**: Monotonic Trajectory Pre-Order — pre-decides a serialization order at launch, serves each read the order-filtered value, applies writes speculatively in place; affected readers receive a one-way notification to re-judge and patch their plan
- **CoAgent middleware**: toolcall middleware whose privileged ToolSmith grows footprint-declared, undoable tools online
- **Empirical results**: on ten contended workloads, stays within 5% of serial correctness at 1.4× speedup and near-serial token cost (vs 2PL and OCC which surrender nearly all concurrency gains); on a bash-only target, grows a 25-tool library online and lifts task pass rate from 45/71 to 63/71 at 0.80× time and 0.86× cost

## Related Papers
- [[a-technical-taxonomy-of-llm-agent-communication-protocols-2606.19135]] — Communication protocol taxonomy for LLM multi-agent systems (orthogonal: CoAgent addresses concurrency control within shared-state agents; taxonomy addresses protocol interoperability)
- [[autopass-evidenceguided-llm-agents-for-compiler-performance-tuning-2606.20373]] — Multi-agent LLM system for automated tasks (orthogonal: AutoPass targets compiler optimization; CoAgent targets fundamental concurrency primitives for multi-agent shared state)
