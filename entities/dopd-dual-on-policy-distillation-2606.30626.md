---
title: "DOPD: Dual On-policy Distillation"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [distillation, knowledge-transfer, teacher-student, privilege-illusion]
sources: ["https://arxiv.org/abs/2606.30626"]
---

# DOPD: Dual On-policy Distillation

## Overview
DOPD identifies a failure mode in on-policy distillation called "privilege illusion" — when additional privileged information given to teacher or student creates a pattern that conflates the capability gap students should close with the information asymmetry gap that can only be superficially mimicked. DOPD proposes dual on-policy distillation that separates these two gaps, ensuring students learn genuine capabilities rather than exploitable information asymmetries. Published 2026.

## Key Facts
- **Year**: 2026
- **arXiv**: [2606.30626](https://arxiv.org/abs/2606.30626)

## Key Contributions
- Identifies "privilege illusion" failure mode in on-policy distillation
- Dual OPD framework separating capability gap from information asymmetry gap
- Dense token-level supervision with high-quality supervision sources
- Principled approach to teacher-student knowledge transfer

## Related Papers
- [[a-survey-of-on-policy-distillation-for-large-language-models-2604.00626]] — Survey of on-policy distillation for LLMs
