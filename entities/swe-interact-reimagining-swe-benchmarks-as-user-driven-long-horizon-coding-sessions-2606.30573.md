---
title: "SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [coding-agents, benchmark, software-engineering, interactive-planning]
sources: ["https://arxiv.org/abs/2606.30573"]
---

# SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions

## Overview
SWE-INTERACT introduces a new testbed for evaluating coding agents on multi-turn, interactive, user-driven software engineering tasks. Unlike existing SWE benchmarks that provide complete requirements upfront and evaluate agents on autonomous implementation, SWE-INTERACT simulates real-world software development where requirements emerge through user dialogue, clarification requests, and iterative feedback. The benchmark exposes a critical gap: current frontier models achieve only 23-31% success on interactive sessions versus 67-78% on static SWE-bench.

## Key Facts
- **Authors**: Raghavendra, Mohit; Gunjal, Anisha; Sabharwal, Aakash + 1
- **Year**: 2026
- **arXiv**: [2606.30573](https://arxiv.org/abs/2606.30573)

## Key Contributions
- Introduced 1,247 curated user interaction traces covering requirements gathering, specification refinement, implementation negotiation, and bug reporting
- Demonstrated that interactive software engineering exposes fundamentally different capabilities than autonomous implementation
- Revealed 40-50 percentage point gap between frontier models on static vs interactive coding tasks
- Established collaborative coding as a distinct evaluation axis orthogonal to autonomous agent capability
- Provides interaction taxonomy: dialogue-based requirements, iterative feedback, specification negotiation, bug reporting

## Related Papers
- [[a-multi-dataset-benchmark-for-evaluating-llm-agents-in-microservice-failure-diagnosis-2606.29193]] — Multi-dataset benchmark for LLM agents in failure diagnosis
- [[benchmarking-open-ended-multi-agent-coordination-in-language-agents-2606.08340]] — Multi-agent coordination benchmarking
- [[agent-skill-evaluation-and-evolution-frameworks-benchmarks-2606.11435]] — Agent skill evaluation frameworks
