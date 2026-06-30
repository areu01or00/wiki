---
title: "Multilingual Unlearning in LLMs: Transfer, Dynamics, and Reversibility"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [unlearning, multilingual, privacy, machine-unlearning, LLM]
sources: ["https://arxiv.org/abs/2606.03291"]
---

# Multilingual Unlearning in LLMs: Transfer, Dynamics, and Reversibility

## Overview
Extends machine unlearning research beyond English by studying multilingual unlearning across five languages using an extended TOFU benchmark. Fine-tuning, unlearning, and querying models with different language permutations reveals that unlearning transfer—the ability of an unlearned model to forget facts across languages it was not specifically unlearned on—is substantial but varies by language and unlearning method. The work also investigates the reversibility of unlearning: whether forgotten knowledge can be reacquired through targeted fine-tuning.

## Key Facts
- **arXiv**: [2606.03291](https://arxiv.org/abs/2606.03291)

## Key Contributions
- First systematic multilingual unlearning study extending TOFU to five non-English languages
- Quantifies unlearning transfer across languages: unlearning in one language often generalizes to others, but not always
- Documents the dynamics of multilingual forgetting and reacquisition (reversibility)
- Surfaces language-agnostic vs. language-specific unlearning mechanisms as an open design question

## Related Papers
- [[knowledgesmith-uncovering-knowledge-updating-in-llms-with-model-editing-and-unlearning-2510.02392]] — model editing and unlearning methodology
- [[repselect-robust-llm-unlearning-via-representation-selectivity-2606.17168]] — unlearning methodology and evaluation
- [[unlearners-can-lie-evaluating-and-improving-honesty-in-llm-unlearning-2605.08765]] — honesty in LLM unlearning evaluation
