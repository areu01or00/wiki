---
title: "How Much Coordination Gain Is Real? A Paired Noise-Floor Protocol for Multi-Agent LLM Benchmarks"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [multi-agent, benchmark, evaluation, coordination]
sources: ["https://arxiv.org/abs/2606.20695"]
---

# How Much Coordination Gain Is Real? A Paired Noise-Floor Protocol for Multi-Agent LLM Benchmarks

## Overview
This paper reveals that most multi-agent LLM coordination architectures report benchmark deltas below the noise floor of their own evaluations. Using a paired noise-floor protocol that isolates configuration-equivalent API inputs via SHA-256 byte audit, the authors show that 7 of 10 recent coordination architectures report effects smaller than the local noise envelope, and even the largest single-seed effect (+18pp) fails to reproduce in a same-model replication. Introduces `coordination-active pass@k` as the minimum reporting protocol.

## Key Facts
- **Authors**: Alibek T Kaliyev, Artem Maryanskyy
- **Year**: 2026
- **arXiv**: [2606.20695](https://arxiv.org/abs/2606.20695)
- **Submitted**: 15 Jun 2026
- **Venue**: cs.MA (Multiagent Systems)

## Key Contributions
- Paired noise-floor protocol: isolates configuration-equivalent API inputs via SHA-256 byte audit to measure baseline trial-0 disagreement
- Coordination-active pass@k: minimum reporting protocol requiring sample-size targets and runtime hooks
- ET-MCP substrate: task-scoped negative-knowledge store conformant with MCP 2026-07-28 for isolating reader-side choices
- Demonstrates that most published multi-agent coordination gains are below the noise floor of same-model paired replications

## Related Papers
- [[taco-tool-augmented-credit-optimization-for-agentic-tool-use-2606.30251]] — TACO's self-supervised tool credit assignment as a representative architecture whose gains fall below the noise floor when evaluated with the paired protocol
- [[tau-rec-a-verifiable-benchmark-for-agentic-recommender-systems-2606.10156]] — τ-Rec's verifiable reward framework as a methodology for moving beyond subjective benchmark deltas
