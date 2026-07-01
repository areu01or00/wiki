---
title: "DD-GEPA: Prompt Optimization for Dialogue Disentanglement Focusing on Task Instruction and Utterance Representation"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [prompt-engineering, dialogue-systems, automatic-prompt-optimization, multi-party-conversation]
sources: ["https://arxiv.org/abs/2606.07894"]
---

# DD-GEPA: Prompt Optimization for Dialogue Disentanglement Focusing on Task Instruction and Utterance Representation

## Overview
Multi-party chat often contains interleaved dialogues because multiple participants discuss different topics simultaneously. Dialogue disentanglement separates entangled utterance sequences into coherent dialogues. While LLMs show promise for this task, they still achieve low accuracy. DD-GEPA proposes an automatic prompt optimization approach that decomposes the prompt into three components — task instruction, utterance representation, and output instruction — and optimizes each using Gradient-based Evolutionary Prompt Adaptation (GEPA).

## Key Facts
- **Authors**: Takada, Naoki; Mori, Tatsunori
- **Year**: 2026
- **arXiv**: [2606.07894](https://arxiv.org/abs/2606.07894)

## Key Contributions
- Decomposes LLM prompt for dialogue disentanglement into three optimizable components
- GEPA (Gradient-based Evolutionary Prompt Adaptation) jointly optimizes task instruction + utterance representation + output instruction
- Shows significant improvement over manual prompt engineering on this task
- First automatic prompt optimization work specifically targeting dialogue disentanglement

## Related Papers
- [[when-gradients-collide-failure-modes-of-multi-objective-prompt-optimization-for-llm-judges-2605.26046]] — "When Gradients Collide": failure modes of multi-objective prompt optimization (related automatic prompt optimization framing)
