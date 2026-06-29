---
title: "Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [safety, agent, context-management]
sources: ["https://arxiv.org/abs/2606.22528"]
---

# Governance Decay: How Context Compaction Silently Erases Safety Constraints in Long-Horizon LLM Agents

## Overview
Modern LLM agents increasingly rely on context compaction (summarization, eviction, or chunking) to keep long-running sessions within token budgets. This paper identifies a critical safety failure mode: governance constraints that agents reliably obey while visible can be silently removed by compaction, causing the same agent to perform prohibited tool actions later in the session — without any explicit command or override. The authors call this failure mode **Governance Decay**.

## Key Facts
- **arXiv**: [2606.22528](https://arxiv.org/abs/2606.22528)
- **Date**: 2026/06/21 (online)

## Key Contributions
- **Governance Decay failure mode**: formally identified and characterized; in-context governance constraints that survive explicit override can be silently removed by context compaction, creating a time-of-check-to-time-of-use (TOCTOU) gap in agent safety
- **ConstraintRot benchmark**: long-horizon agent scenarios with deterministic tool-call grading; measures compaction-induced constraint violations across summarization strategies
- **Empirical evaluation**: compaction strategies (summary, eviction, chunk) cause 34–67% of previously constrained dangerous tool calls to become executable without any explicit prompt change
- **Key mechanism**: compaction targets the governance layer (safety constraints, tool-use policies) as "redundant context," removing it before the agent acts on it — a structurally distinct failure from both jailbreaking and memory corruption

## Related Papers
- [[ajar-adaptive-jailbreak-architecture-red-teaming-2601.10971]] — Rule 86 sibling: adaptive multi-turn jailbreak via MCP services
- [[agentic-adversarial-rewriting-exposes-nlp-pipeline-vulnerabilities-2604.23483]] — Rule 86 sibling: two-agent semantic perturbation pipeline
- [[jailbreaking-llms-vlms-mechanisms-evaluation-unified-defense-2601.03594]] — Rule 86 sibling: systematic jailbreak taxonomy
- [[gatemem-benchmarking-memory-governance-in-multi-principal-shared-memory-agents-2606.18829]] — Context/memory governance overlap: GateMem benchmarks memory governance in multi-principal shared-memory agents
- [[agent-memory-characterization-and-system-implications-of-stateful-long-horizon-workloads-2606.06448]] — Long-horizon agent workload characterization
