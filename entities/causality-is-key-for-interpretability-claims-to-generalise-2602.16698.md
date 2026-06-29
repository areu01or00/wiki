---
title: "Causality is Key for Interpretability Claims to Generalise"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [causal-interpretability, mechanistic-interpretability, llm, methodology]
sources: ["https://arxiv.org/abs/2602.16698"]
---

# Causality is Key for Interpretability Claims to Generalise

## Overview
Interpretability research on LLMs has produced important insights but faces two recurring pitfalls: findings that do not generalise beyond the specific model/setting, and causal interpretations that outrun the empirical evidence. The authors argue that causal inference is the correct framework for specifying valid mappings from model activations to invariant high-level structures. The paper catalogues common failure modes and proposes causal fidelity as the methodological standard for the field.

## Key Facts
- **Authors**: Shruti Joshi, Aaron Mueller, David Klindt, Wieland Brendel, Patrik Reizinger, Dhanya Sridhar
- **Year**: 2026
- **arXiv**: [2602.16698](https://arxiv.org/abs/2602.16698)

## Key Contributions
- **Causal validity criterion** for interpretability: mappings from activations to concepts must be causally grounded, not merely correlational
- **Failure mode taxonomy**: non-generalising circuits, assumption-free causal stories, over-claimed interventions
- **Positions Belief-or-Circuitry (2605.08405) as a model example** of causally valid intervention design
- **Positions Emergent-Causal-Geometric (2602.04931) as requiring causal grounding** for the geometry-to-prediction mapping
- **Foundation for Rule 83 CAUSAL-REPRESENTATION-PROBE**: this paper defines what causally valid representation analysis means

## Related Papers
- [[belief-or-circuitry-causal-evidence-for-in-context-graph-learning-2605.08405]] — Case study of causally valid intervention; demonstrates the methodology this paper's framework demands
- [[emergent-causal-geometric-dynamics-across-depth-in-large-language-models-2602.04931]] — Depth-geometry analysis; needs causal grounding per this paper's framework
