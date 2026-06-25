---
title: "Distilling Examples into Task Instructions: Enhanced In-Context Learning for Real-World B2B Conversations"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [in-context-learning, distillation, b2b-conversations, low-resource-nlp, knowledge-extraction]
sources: ["https://arxiv.org/abs/2606.15641"]
---

# Distilling Examples into Task Instructions: Enhanced In-Context Learning for Real-World B2B Conversations

## Overview
Rotman, Kopilov, Zalmanson, and Allouche address the gap between standard in-context-learning (ICL) few-shot classification and the practical demands of specialized-domain deployment, introducing the Call Playbook dataset of five classification tasks over real-world B2B conversations and proposing knowledge-extraction methods that distill verbose few-shot examples into compact, interpretable representations of structured classification criteria and precise task descriptions — achieving a 99% reduction in token usage, up to 7% macro-AUC improvement over traditional ICL, and robustness as context grows (whereas advanced token-compression baselines degrade by over 9 F1 points).

## Key Facts
- **Authors**: Rotman, Guy; Kopilov, Adi; Zalmanson, Danit Berger; Allouche, Omri
- **Year**: 2026
- **arXiv**: [2606.15641](https://arxiv.org/abs/2606.15641)
- **Date**: 2026-06-14

## Key Contributions
- Releases Call Playbook, a five-task classification benchmark built from real-world multi-party B2B conversations targeting core sales concepts — explicitly designed to expose ICL failure modes in specialized domains where context length grows by concatenating few-shot examples.
- Identifies the load-bearing limitation of standard ICL on specialized-domain text: concatenation of multiple few-shot examples inflates context without proportionally improving classification, and existing token-compression baselines (which compress raw tokens) degrade by over 9 F1 points as context grows.
- Proposes knowledge-extraction methods that distill verbose few-shot examples into two compact, interpretable artifacts: (1) structured classification criteria, and (2) precise task descriptions — yielding a 99% reduction in token usage while improving macro-AUC by up to 7% over traditional ICL.
- Surfaces a deployment-relevant design pattern for low-resource classification: explicit distillation of *what each example demonstrates* into *what the task is* is more robust under context growth than compressing raw tokens, and it enables direct refinement of classification logic — addressing transparency, efficiency, and user interaction requirements that opaque token-compression baselines leave unmet.

## Related Papers
- [[emergent-concepts]] — Parent meta-page that aggregates this and other emergent-concept discoveries from the wiki-explore-agent pipeline.
- [[fastmix-fast-data-mixture-optimization-via-gradient-descent-2606.14971]] — Sibling LLM-training-data systems work; both frame distillation as a route to compact, learned representations rather than raw-data compression (FastMix distills data mixtures into gradient-derived weights; this paper distills examples into structured criteria and task descriptions).
- [[the-periodic-table-of-llm-reasoning-a-structured-survey-of-reasoning-paradigms-abstractions-building-blocks-and-open-challenges-2606.11470]] — Sibling reasoning-paradigm survey; together they frame in-context demonstration design as a reasoning primitive that benefits from explicit abstraction rather than implicit pattern-matching.
- [[distill-once-adapt-life-long-dataset-distillation-continual-2606.20196]] — Sibling dataset-distillation work for continual test-time adaptation; both distill information into compact synthetic artifacts (DO-ALL: privacy-preserving anchors; this paper: structured criteria + task descriptions) and surface distillation as the load-bearing primitive for resource-constrained deployment.