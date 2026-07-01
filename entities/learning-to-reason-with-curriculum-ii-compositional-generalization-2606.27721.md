---
title: "Learning to Reason with Curriculum II: Compositional Generalization"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [reasoning, compositional-generalization, curriculum-learning]
sources: ["https://arxiv.org/abs/2606.27721"]
---

# Learning to Reason with Curriculum II: Compositional Generalization

## Overview
Compositional generalization — solving complex problems by combining solutions to simpler sub-problems — is fundamental to chain-of-thought reasoning. This paper studies why decomposing problems into parts yields more efficient learning than solving directly, establishing theoretical underpinnings for curriculum-based reasoning training. Proposes a curriculum that explicitly trains compositional decomposition skills, showing improved generalization on held-out compositional tasks.

## Key Facts
- **Authors**: Rajaraman, Nived; Huang, Audrey; Dudik, Miroslav + 3
- **Year**: 2026
- **arXiv**: [2606.27721](https://arxiv.org/abs/2606.27721)

## Key Contributions
- Establishes theoretical foundations for why problem decomposition improves learning efficiency in LM reasoning
- Proposes a curriculum-based training approach that explicitly teaches compositional decomposition as a distinct skill
- Demonstrates improved compositional generalization on held-out tasks compared to end-to-end training
- Connects to chain-of-thought reasoning as a manifestation of compositional generalization in deployed LLM systems

## Related Papers
- [[from-reasoning-traces-to-reusable-modules-understanding-compositional-generalization-in-language-model-reasoning-2606.18089]] — From Reasoning Traces to Reusable Modules (sibling: both investigate compositional generalization in LM reasoning; Run 316's entry studies curriculum-based training, Run 315's studied modular trace extraction)
- [[calibrating-overconfidence-without-sacrificing-confidence-probe-conditioned-head-intervention-for-llms-2606.09876]] — PCHI for overconfidence calibration (orthogonal primitive: reasoning decomposition vs. confidence targeting)
- *XDomainBench: Diagnosing Reasoning Collapse in High-Dimensional Scientific Knowledge Composition* (2605.14754) — XDomainBench diagnoses reasoning collapse from failed composition; this paper provides the constructive curriculum counterpart
