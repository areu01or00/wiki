---
title: "Robust Reasoning Benchmark"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [reasoning, benchmark, llm-evaluation]
sources: ["https://arxiv.org/abs/2604.08571"]
---

# Robust Reasoning Benchmark

## Overview
The Robust Reasoning Benchmark (RRB) is a systematic evaluation framework exposing how frontier LLMs fail under structured textual perturbations to mathematical reasoning problems. Rather than measuring raw accuracy on clean benchmarks, RRB measures the accuracy degradation pipeline across 13 deterministic textual perturbations applied to AIME 2024 and AIME 2025 problems — revealing that frontier models lose up to 54 percentage points of accuracy under structural noise including cognitive thrashing, tokenization breakdown, and reasoning collapse.

## Key Facts
- **Authors**: Golikov, Pavel; Opryshko, Evgenii; Pekhimenko, Gennady + 1
- **Year**: 2026
- **arXiv**: [2604.08571](https://arxiv.org/abs/2604.08571)

## Key Contributions
- **13-perturbation pipeline**: Applies deterministic textual perturbations (rephrasing, irrelevant context injection, formatting changes, constraint modifications) to AIME problems to test reasoning robustness
- **Up to 54pp accuracy degradation**: Frontier models (including GPT-4 class) show catastrophic reasoning degradation under structural noise, far beyond what clean-benchmark scores predict
- **Failure mode taxonomy**: Identifies three primary failure modes — cognitive thrashing (model switches between reasoning strategies), tokenization breakdown (numerical reasoning disrupted by formatting), reasoning collapse (model abandons valid reasoning under perturbation)
- **Perturbation-robust evaluation standard**: Proposes RRB as the minimum standard for reasoning model evaluation, replacing static accuracy as the primary metric

## Related Papers
- [[large-language-model-reasoning-failures-2602.06176]] — Prior survey of LLM reasoning failures taxonomy
- [[memfail-stress-testing-failure-modes-of-llm-memory-systems-2605.26667]] — Complementary benchmark for memory system failure modes
- [[the-compliance-trap-how-structural-constraints-degrade-frontier-ai-metacognition-2605.02398]] — Metacognitive stability failures under adversarial pressure
