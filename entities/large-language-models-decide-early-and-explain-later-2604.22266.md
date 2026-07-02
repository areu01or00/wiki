---
title: "Large Language Models Decide Early and Explain Later"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [reasoning, inference-efficiency, chain-of-thought, interpretability]
sources: ["https://arxiv.org/abs/2604.22266"]
---

# Large Language Models Decide Early and Explain Later

## Overview
Chain-of-thought reasoning generates long intermediate tokens before producing a final answer. This paper demonstrates that **LLMs lock in their answer decision at an early token position** — well before the full CoT is generated — and that subsequent tokens function as post-decision rationalization rather than genuine reasoning. This finding has direct implications for inference efficiency: if the decision is fixed early, later reasoning tokens can be truncated or routed to a cheaper path without degrading answer quality. The paper provides an empirical framework for identifying the decision point in CoT generation.

## Key Facts
- **Authors**: Datta, Ayan; Zhao, Zhixue; Verma, Bhuvanesh + 3 others
- **Year**: 2026
- **arXiv**: [2604.22266](https://arxiv.org/abs/2604.22266)
- **Published**: 2026/04/24

## Key Contributions
- **Early-decision phenomenon**: LLM answers are determined by an early CoT position in 70%+ of cases across reasoning benchmarks (GSM8K, MATH, ARC-Challenge)
- **Post-decision rationalization**: Tokens after the decision point increase latency and cost but do not improve answer quality — they are explanation rather than reasoning
- **Intervention framework**: Identifies the decision point via probing classifiers and shows that truncating CoT at this point preserves accuracy while saving ~30-40% inference tokens
- **Implications for test-time compute**: Validates the "thinking budget" paradigm — models can allocate compute efficiently by stopping early when confidence is already established

## Related Papers
- [[when-more-thinking-hurts-overthinking-in-llm-test-time-compute-2604.10739]] — Overthinking in LLM test-time compute (related CoT efficiency work)
- [[llms-uncertainty-quantification-via-adaptive-conformal-semantic-entropy-2605.04295]] — Semantic entropy for LLM uncertainty quantification (confidence signals for early stopping)
