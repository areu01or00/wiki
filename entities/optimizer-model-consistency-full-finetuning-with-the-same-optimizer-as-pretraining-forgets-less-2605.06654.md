---
title: "Optimizer-Model Consistency: Full Finetuning with the Same Optimizer as Pretraining Forgets Less"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [fine-tuning, unlearning, optimizer, SFT, LLM]
sources: ["https://arxiv.org/abs/2605.06654"]
---

# Optimizer-Model Consistency: Full Finetuning with the Same Optimizer as Pretraining Forgets Less

## Overview
Full finetuning with the same optimizer as pretraining achieves a better learning-forgetting tradeoff than other optimizers and LoRA during the SFT stage. The phenomenon—termed optimizer-model consistency—shows that models full-finetuned with the same optimizer (e.g., AdamW) as pretraining forget less while maintaining or improving task performance. This is surprising because LoRA and alternative optimizers are widely assumed superior for parameter-efficient fine-tuning.

## Key Facts
- **arXiv**: [2605.06654](https://arxiv.org/abs/2605.06654)

## Key Contributions
- Identifies optimizer-model consistency: full finetuning with same optimizer as pretraining achieves better learning-forgetting tradeoff than alternative optimizers and LoRA
- Shows this holds even against LoRA during SFT, contrary to common assumption
- Demonstrates the tradeoff is robust across model scales and tasks
- Surfaces optimizer-configuration as a fine-tuning design choice with direct implications for knowledge retention vs. acquisition

## Related Papers
- [[few-tokens-big-leverage-preserving-safety-alignment-by-constraining-safety-tokens-during-fine-tuning-2603.07445]] — both probe fine-tuning mechanics and their interaction with safety/capability tradeoffs
- [[energy-based-fine-tuning-of-language-models-2603.12248]] — fine-tuning methodology as a control mechanism for LLM behavior
