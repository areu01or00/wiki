---
title: "QMFOL: Benchmarking Large Language Model Reasoning via Quantifiable Monadic First-Order Logic Test Case Generation"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [reasoning, evaluation, benchmark, logic, formal]
sources: ["https://arxiv.org/abs/2606.20227"]
---

# QMFOL: Benchmarking Large Language Model Reasoning via Quantifiable Monadic First-Order Logic Test Case Generation

## Overview
Existing LLM reasoning benchmarks lack fine-grained control over logical complexity and struggle to balance semantic diversity with logical consistency. QMFOL introduces an automated framework for generating monadic first-order logic reasoning tasks with quantifiable and controllable complexity, enabling systematic evaluation of LLM deductive reasoning under precisely characterized conditions.

## Key Facts
- **Authors**: Zheng, Xinyi; Shi, Ling; Yu, Tianlong + 3
- **Year**: 2026
- **arXiv**: [2606.20227](https://arxiv.org/abs/2606.20227)

## Key Contributions
- First automated framework for generating FOL reasoning tasks with *quantifiable* complexity control (by varying quantifier nesting depth, predicate arity, and domain size)
- Separates logical complexity from semantic complexity — enables isolating which dimension causes reasoning failures
- Proposes automated test case generation from formal logical specifications, ensuring consistency that manual benchmark construction cannot guarantee
- Establishes new state-of-the-art on logical reasoning evaluation for high-stakes decision-making contexts (medical, legal)

## Related Papers
- [[the-periodic-table-of-llm-reasoning-a-structured-survey-of-reasoning-paradigms-abstractions-building-blocks-and-open-challenges-2606.11470]] — Taxonomy of reasoning paradigms; QMFOL provides the missing fine-grained evaluation methodology for formal logic reasoning
