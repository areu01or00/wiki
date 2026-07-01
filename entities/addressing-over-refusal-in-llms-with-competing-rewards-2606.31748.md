---
title: "Addressing Over-Refusal in LLMs with Competing Rewards"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [safety, alignment, llm, refusal-calibration]
sources: ["https://arxiv.org/abs/2606.31748"]
---

# Addressing Over-Refusal in LLMs with Competing Rewards

## Overview
Safety training on LLMs creates a known tension: it reduces harmful outputs but can also increase refusal on benign queries (over-refusal). This paper models the problem as competing reward signals — safety reward vs helpfulness reward — and proposes a training-time framework that balances these directly. The key insight is that over-refusal is a reward miscalibration problem, not a dataset problem, and can be addressed by explicitly modeling the trade-off curve between safety and helpfulness at training time.

## Key Facts
- **Authors**: Kim, Taeyoun; Kumar, Aviral
- **Year**: 2026
- **arXiv**: [2606.31748](https://arxiv.org/abs/2606.31748)

## Key Contributions
- Formalizes over-refusal as a competing-rewards problem between safety and helpfulness
- Proposes reward-composition technique that explicitly balances competing signals during training
- Achieves better safety-helpfulness Pareto curve than separate fine-tuning approaches
- Introduces new evaluation protocol measuring refusal behavior across a harmlessness-helpfulness grid

## Related Papers
- Emergent discovery — no prior parent paper; this work introduces a new safety-calibration primitive to the wiki.
