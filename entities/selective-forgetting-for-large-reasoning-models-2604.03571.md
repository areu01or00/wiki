---
title: "Selective Forgetting for Large Reasoning Models"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [unlearning, llm, reasoning-models, privacy]
sources: ["https://arxiv.org/abs/2604.03571"]
---

# Selective Forgetting for Large Reasoning Models

## Overview
Large Reasoning Models (LRMs) generate structured chains of thought (CoTs) before producing final answers, making them especially vulnerable to knowledge leakage through intermediate reasoning steps. This paper proposes a novel LRM unlearning framework that selectively removes sensitive reasoning components while preserving general reasoning capabilities. The approach uses multiple LLMs with retrieval-augmented generation (RAG) to analyze CoT traces, identify forget-relevant segments, and replace them with benign placeholders that maintain logical structure. A new feature replacement unlearning loss simultaneously suppresses the probability of generating forgotten content while reinforcing structurally valid replacements.

## Key Facts
- **Authors**: Tuan Le, Wei Qian, Mengdi Huai
- **Year**: 2026
- **arXiv**: [2604.03571](https://arxiv.org/abs/2604.03571)
- **Subjects**: Artificial Intelligence (cs.AI)
- **Submitted**: 2026-04-04

## Key Contributions
- First LRM-specific selective forgetting framework — targets intermediate reasoning steps, not just final answers
- RAG-based CoT trace analysis to identify forget-relevant segments across the full reasoning chain
- Feature replacement unlearning loss that suppresses forgotten content while reinforcing valid replacements
- Preserves general reasoning capabilities while achieving precise unlearning of targeted knowledge
- Experiments on synthetic and medical datasets verify desired properties

## Related Papers
- [[learning-what-to-forget-improving-llm-unlearning-via-learned-token-level-importance-2606.06320]] — Sibling from same run — ATWU token-level importance scoring for general LLM unlearning
- [[tmas-scaling-test-time-compute-via-multi-agent-synergy-2605.10344]] — Sibling from same run — multi-agent test-time compute scaling
- [[knowledgesmith-uncovering-knowledge-updating-in-llms-with-model-editing-and-unlearning-2510.02392]] — Parent: KnowledgeSmith — foundational LLM unlearning taxonomy
