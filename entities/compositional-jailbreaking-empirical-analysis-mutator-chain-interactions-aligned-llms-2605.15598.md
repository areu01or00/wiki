---
title: "Compositional Jailbreaking: An Empirical Analysis of Mutator Chain Interactions in Aligned LLMs"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [safety, adversarial, jailbreak, alignment, llm]
sources: ["https://arxiv.org/abs/2605.15598"]
---

# Compositional Jailbreaking: An Empirical Analysis of Mutator Chain Interactions in Aligned LLMs

## Overview
Jailbreaking attacks on large language models pose a significant threat to AI safety by enabling the generation of harmful or restricted content. This paper presents a systematic study of mutator chaining, in which weak jailbreak transformations are applied sequentially to characterize how they interact: whether they reinforce one another, interfere destructively, or produce no meaningful change. Twelve baseline mutators are implemented and all ordered pairs evaluated on a benchmark of harmful prompts against three popular LLM models. Findings reveal that while most combinations fail to outperform individual mutators (destructive interference or structural incompatibility), a small fraction produce synergistic effects that improve attack success rates.

## Key Facts
- **Authors**: Unknown (arXiv 2605.15598)
- **Year**: 2025
- **arXiv**: [2605.15598](https://arxiv.org/abs/2605.15598)

## Key Contributions
- **Mutator chaining framework**: Systematic study of sequential compositional jailbreak transformations applied to aligned LLMs
- **12 baseline mutators + all ordered pairs**: Comprehensive evaluation matrix across three popular LLM models
- **Completeness and validity metrics**: Capture both transformation persistence and attack effectiveness
- **Non-uniform interaction landscape**: Most combinations fail (destructive interference), but a small fraction yield synergistic attack success rate improvements
- **First-in-wiki**: First systematic study of compositional mutator chaining for jailbreak attack analysis in the wiki
- **Orthogonal to**: Prior jailbreak papers (single-strategy evaluations); this focuses on emergent interactions between sequential transformations

## Related Papers
- [[jailbreaking-llms-vlms-mechanisms-evaluation-unified-defense-2601.03594]] — Foundational jailbreak mechanisms and defense paper
- [[ajar-adaptive-jailbreak-architecture-red-teaming-2601.10971]] — Adaptive red-teaming architecture for jailbreaking
