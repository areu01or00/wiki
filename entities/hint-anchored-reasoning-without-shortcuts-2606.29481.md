---
title: "To Reason or to Fabricate: Reasoning Without Shortcuts via Hint-Anchored Pairwise Aggregation"
created: 2026-06-01
updated: 2026-06-01
type: entity
tags: [reasoning, llm, rlhf, evaluation]
sources: ["https://arxiv.org/abs/2606.29481"]
---

# To Reason or to Fabricate: Reasoning Without Shortcuts via Hint-Anchored Pairwise Aggregation

## Overview
While reinforcement learning (RL) significantly enhances LLM reasoning, its efficacy is severely undermined by Pre-RL data overlap — RL datasets that overlap with pretraining or SFT corpora cause models to exploit shortcuts by memorizing correct answers and fabricating post-hoc reasoning. This paper introduces hint-anchored pairwise aggregation to detect and correct shortcut exploitation, enabling LLMs to learn genuine reasoning patterns rather than answer-pattern memorization.

## Key Contributions
- Identifies Pre-RL data overlap as a distinct failure mode from standard distribution shift
- Proposes hint-anchored pairwise aggregation for detecting shortcut exploitation in RL-trained reasoning models
- Evaluates on math reasoning tasks (GSM8K, MATH) showing significant accuracy degradation when shortcuts are removed
- First systematic study of RL reasoning shortcut detection and correction in the wiki

## Key Facts
- **arXiv**: [2606.29481](https://arxiv.org/abs/2606.29481)

## Related Papers
- [[emergent-concepts]] — Parent emergent-concepts chain that led to this discovery
