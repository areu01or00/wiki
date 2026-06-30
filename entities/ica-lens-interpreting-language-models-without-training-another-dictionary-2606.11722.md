---
title: "ICA Lens: Interpreting Language Models Without Training Another Dictionary"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [interpretability, representation-geometry, llm]
sources: ["https://arxiv.org/abs/2606.11722"]
---

# ICA Lens: Interpreting Language Models Without Training Another Dictionary

## Overview
Sparse autoencoders (SAEs) are the standard tool for finding interpretable directions in LLM activations but require training large overcomplete dictionaries. This paper shows that much interpretable structure is already visible from activation geometry alone before training any dictionary — enabling faster, cheaper interpretability without the SAE bottleneck.

## Key Facts
- **Authors**: Sida Liu, Feijiang Han
- **Year**: 2026
- **arXiv**: [2606.11722](https://arxiv.org/abs/2606.11722)

## Key Contributions
- Introduced ICA Lens: activation geometry before dictionary learning as a first-pass interpretability lens
- Showed many interpretable directions are already selective in raw activations
- Reduced the computational overhead of SAE-based interpretability by eliminating dictionary training when geometry suffices
- Theoretical and empirical analysis of what structure is vs isn't visible pre-training

## Related Papers
- [[emergent-causal-geometric-dynamics-across-depth-in-large-language-models-2602.04931]] — Geometric representation analysis in LLM depth layers (prior work this extends)
