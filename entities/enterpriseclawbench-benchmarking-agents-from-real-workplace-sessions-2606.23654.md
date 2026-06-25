---
title: "EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [benchmark, agents, enterprise, evaluation, tool-use]
sources: ["https://arxiv.org/abs/2606.23654"]
---

# EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions

## Overview
EnterpriseClawBench is an enterprise agent benchmark built from proprietary, real-world agent sessions: starting from a large archive of workplace traces, the authors distill 852 reproducible tasks each paired with recovered fixtures, rewritten prompts, role classes, skill subclasses, hard rules, and semantic rubrics. Because the underlying sessions contain internal enterprise content, the benchmark data is not released; instead, the work ships the reproducible harness, evaluation rubrics, and an analysis of agent failure modes on tool-heavy enterprise workflows. It complements earlier agent benchmarks by anchoring tasks to *real* workplace artifact outputs rather than synthetic test cases.

## Key Facts
- **Authors**: Zhong, Jincheng; Wang, Weizhi; Jiang, Che; Tian, Kai; Yuan, Zhenzhao
- **Year**: 2026 (2026-06-22)
- **arXiv**: [2606.23654](https://arxiv.org/abs/2606.23654)
- **Subjects**: cs.CL

## Key Contributions
- Mines real-world enterprise agent sessions to construct 852 reproducible tasks with semantic rubrics, hard rules, and recovered fixtures — moving beyond synthetic agent benchmarks.
- Categorizes tasks along role class and skill subclass axes, enabling structured per-capability evaluation of enterprise agents.
- Provides a non-data-releasing benchmark protocol: the evaluation harness and rubrics are public while sensitive session content stays internal, addressing enterprise confidentiality concerns.
- Surfaces a taxonomy of agent failure modes specific to enterprise workflows (heterogeneous file formats, tool orchestration across internal systems, business artifact correctness).

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on the agent-evaluation/enterprise-tool-use theme cluster.
