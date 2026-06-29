---
title: "Mind the Heads: Topological Representation Alignment for Multimodal LLMs"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [representation, multimodal, alignment, attention]
sources: ["https://arxiv.org/abs/2606.23885"]
---

# Mind the Heads: Topological Representation Alignment for Multimodal LLMs

## Overview
This paper examines how attention heads in Multimodal Large Language Models (MLLMs) develop specialized representations across independently initialized training runs, quantifying layer-by-layer similarity of learned representations. It introduces topological geometric analysis to understand when and why different attention heads converge to similar or divergent representations.

## Key Facts
- **Authors**: Davide Caffagni, Alberto Compagnoni, Federico Melis, Sara Sarto, Pier Luigi Dovesi, Mark Graeser, Nicholas D. Cassem
- **Year**: 2026
- **arXiv**: [2606.23885](https://arxiv.org/abs/2606.23885)

## Key Contributions
- Quantifies attention-head stability across model refits (independently initialized training runs)
- Proposes topological representation alignment metrics to measure when heads converge vs. diverge
- Reveals layer-specific patterns: lower layers show higher cross-run consistency than upper layers
- Applies geometric analysis to identify which attention heads can be treated as interchangeable across models

## Related Papers
- [[emergent-concepts]] — Parent theme: emergent concepts in LLM internal representations
