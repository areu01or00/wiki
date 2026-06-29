---
title: "Emergent Alignment"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [alignment, self-correction, ethics, rlhf]
sources: ["https://arxiv.org/abs/2606.19527"]
---

# Emergent Alignment

## Overview
Investigates whether LLMs can discern when their own outputs are misaligned with human ethics and self-correct. Endows an LLM with a conscience step that reviews its own reasoning and outputs, and extends the training loss with an alignment component using Direct Preference Optimization (DPO) to steer the model away from non-ethical outputs — an online technique applicable across training, fine-tuning, adversarial prompting, and zero-shot settings.

## Key Facts
- **Authors**: Kolář, Martin
- **Year**: 2026
- **arXiv**: [2606.19527](https://arxiv.org/abs/2606.19527)

## Key Contributions
- Conscience step: LLM reviews its own reasoning and outputs for ethical misalignment
- DPO-based alignment component that steers away from non-ethical outputs
- Online technique applicable across training, fine-tuning, adversarial prompting, and zero-shot
- First paper in wiki to systematically study emergent ethical self-correction via conscience-step mechanism

## Related Papers
- [[emergent-concepts]] — Parent emergent-concept page for arxiv LLM-research discovery
