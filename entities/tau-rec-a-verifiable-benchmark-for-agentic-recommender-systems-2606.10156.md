---
title: "τ-Rec: A Verifiable Benchmark for Agentic Recommender Systems"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [agentic-ai, benchmark, evaluation, recommender-systems]
sources: ["https://arxiv.org/abs/2606.10156"]
---

# τ-Rec: A Verifiable Benchmark for Agentic Recommender Systems

## Overview
τ-Rec addresses evaluation subjectivity in agentic recommender systems that use multi-turn conversational interfaces. Current benchmarks rely on LLM-as-a-judge, introducing subjectivity, high costs, and inconsistency. τ-Rec replaces subjective evaluation with verifiable rewards and a Reveal-Tagged Elicitation (RTE) mechanism controlling how task constraints surface during dialogue. Uses structured catalog predicates and a pass^k reliability metric to provide systematic testing for consistent reasoning across 9 configurations spanning 5 model families.

## Key Facts
- **Authors**: Bharath Sivaram Narasimhan, Karthik R Narasimhan
- **Year**: 2026
- **arXiv**: [2606.10156](https://arxiv.org/abs/2606.10156)

## Key Contributions
- **Verifiable rewards** replacing subjective LLM-as-judge evaluation for agentic recommenders
- **Reveal-Tagged Elicitation (RTE)** mechanism controlling constraint disclosure during dialogue
- **pass^k reliability metric** for systematic reasoning consistency testing
- Evaluates 9 configurations across 5 model families (GPT-5.4, Claude Sonnet 4.6, Gemini 2.5 Flash, DeepSeek V...)

## Related Papers
- [[taco-tool-augmented-credit-optimization-for-agentic-tool-use-2606.30251]] — TACO: tool-augmented credit optimization for agentic tool use
- [[scaling-the-horizon-not-the-parameters-reaching-trillion-parameter-performance-with-a-35b-agent-2606.30616]] — Agents-A1: agent-horizon scaling
- [[memobench-benchmarking-world-modeling-in-dynamically-changing-environments-2606.27537]] — MemoBench: world model benchmark
