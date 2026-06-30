---
title: "Title:Hint Tuning: Less Data Makes Better Reasoners"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [llm, metacognition, self-awareness]
sources: ["https://arxiv.org/abs/2605.08665"]
---

# Title:Hint Tuning: Less Data Makes Better Reasoners

## Overview
Large reasoning models achieve high accuracy through extended chain-of-thought but generate 5--8 more tokens than necessary, applying verbose reasoning uniformly regardless of problem difficulty. We propose Hint Tuning, a data-efficient approach that teaches models to calibrate reasoning depth. Our key insight: the corresponding instruct model serves as an ideal difficulty probe. By testing what the instruct model can solve with varying guidance, we automatically construct training data across t...

## Key Facts
- **arXiv**: [2605.08665](https://arxiv.org/abs/2605.08665)

## Key Contributions
- first depth-calibration via hint tuning that teaches models to calibrate reasoning verbosity

## Related Papers
- [[emergent-concepts]] — Emergent concepts parent
