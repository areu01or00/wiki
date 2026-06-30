---
title: "EVA: Editing for Versatile Alignment against Jailbreaks"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [llm, alignment, safety, jailbreak, knowledge-editing, agent, skill-distillation]
sources: ["https://arxiv.org/abs/2605.14750"]
---

# EVA: Editing for Versatile Alignment against Jailbreaks

## Overview
EVA is a unified alignment editing framework that defends LLMs and VLMs against jailbreaking attacks by editing safety-related knowledge directly in the model weights. Unlike traditional safety fine-tuning or external filters, EVA treats jailbreak vulnerability as a knowledge-level problem and applies targeted editing to remove exploitable associations while preserving benign capabilities. The framework handles both textual and visual jailbreak triggers, making it the first versatile alignment editing approach covering both modalities.

## Key Facts
- **arXiv**: [2605.14750](https://arxiv.org/abs/2605.14750)
- **Submitted**: 2026-05-DD (from arxiv ID prefix)
- **Theme**: LLM alignment / jailbreak defense / safety editing

## Key Contributions
- First unified alignment editing framework covering both textual and visual jailbreak attacks
- Adversarial trigger identification and targeted erasure approach
- Preserves downstream benign capabilities after safety editing
- Evaluated against 13 jailbreak attack vectors across 8 frontier models


## Related Papers
- [[emergent-concepts]] — Emergent Concepts parent page
