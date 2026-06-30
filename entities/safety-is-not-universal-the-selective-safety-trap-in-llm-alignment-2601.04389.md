---
title: "Safety Is Not Universal: The Selective Safety Trap in LLM Alignment"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [safety, alignment, evaluation, fairness]
sources: ["https://arxiv.org/abs/2601.04389"]
---

# Safety Is Not Universal: The Selective Safety Trap in LLM Alignment

## Overview
Safety Is Not Universal exposes a critical blind spot in LLM safety evaluation: aggregating harms under generic categories (e.g., "Identity Hate") creates an illusion of broad protection while masking population-specific vulnerabilities. The paper demonstrates that safety-aligned LLMs can exhibit selective, targeted failure modes that generic benchmarks miss entirely.

## Key Facts
- **Authors**: Iago Alves Brito, Walcy Santos Rezende Rios, Julia Soares Dollis, Diogo Fernandes Costa Silva
- **Year**: 2026
- **arXiv**: [2601.04389](https://arxiv.org/abs/2601.04389)

## Key Contributions
- Defines the "Selective Safety Trap": safety aggregate scores hide population-specific vulnerabilities
- Introduces evaluation methodology that disaggregates safety benchmarks by demographic/contextual axes
- Demonstrates that current safety alignment generalizes insufficiently across specific populations

## Related Papers
- [[be-your-own-red-teamer-safety-alignment-via-self-play-and-reflective-experience-replay-2601.10589]] — self-play red-teaming approach
- [[do-thinking-tokens-help-with-safety-2606.25013]] — reasoning tokens and safety generalization
- [[cross-generational-transfer-adversarial-attacks-reveals-non-monotonic-safety-2606.00813]] — non-monotonic safety transfer across model generations
