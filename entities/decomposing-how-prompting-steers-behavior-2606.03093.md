---
title: "Decomposing How Prompting Steers Behavior"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [interpretability, representation-geometry, llm]
sources: ["https://arxiv.org/abs/2606.03093"]
---

# Decomposing How Prompting Steers Behavior

## Overview
Prompting steers LLM behavior without weight updates, but the mechanism by which instruction changes reshape internal representations has been unclear. This paper introduces a nested geometric decomposition framework treating prompting as a transformation of representational geometry, showing how prompt pairs reorganize activation space through stimulus-invariant maps.

## Key Facts
- **Authors**: Fan L. Cheng, Nikolaus Kriegeskorte
- **Year**: 2026
- **arXiv**: [2606.03093](https://arxiv.org/abs/2606.03093)

## Key Contributions
- Nested geometric decomposition framework for mapping prompt-induced representational changes
- Stimulus-invariant alignment protocol (translation → rigid → scaling → sequential axis scaling)
- Quantified how different prompt types reorganize geometry at each transformer layer
- First framework to decompose prompting effects into interpretable geometric components

## Related Papers
- [[emergent-causal-geometric-dynamics-across-depth-in-large-language-models-2602.04931]] — Geometric representation analysis in LLM depth layers (prior work this extends)
