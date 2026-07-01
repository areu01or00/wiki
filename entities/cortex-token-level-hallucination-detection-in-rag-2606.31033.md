---
title: "CORTEX: Token-Level Hallucination Detection in RAG via Comparative Internal Representations"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [rag, hallucination-detection, interpretability, llm-reliability]
sources: ["https://arxiv.org/abs/2606.31033"]
---

# CORTEX: Token-Level Hallucination Detection in RAG via Comparative Internal Representations

## Overview
Proposes CORTEX, a token-level hallucination detection method for Retrieval-Augmented Generation. In long-form RAG outputs, hallucinations arise in localized spans rather than throughout entire responses. CORTEX identifies ungrounded content at the token level, enabling fine-grained localization, by comparing internal representations between RAG-generated and retrieve-and-generate outputs.

## Key Facts
- **Authors**: Kazuaki Furumai, Shuichiro Haruta, Kazunori Matsumoto, Daisuke Kamisaka
- **Year**: 2026
- **arXiv**: [2606.31033](https://arxiv.org/abs/2606.31033)

## Key Contributions
- **Token-level hallucination localization**: Detects hallucinated spans at the token granularity, not whole-response level
- **Comparative internal representations**: Uses representation comparison between RAG and retrieval-only outputs as detection signal
- **Fine-grained grounding**: Enables surgical correction of hallucinated tokens rather than regenerating entire response
- **First comparative-representation-based token-level hallucination detection for RAG in the wiki**

## Related Papers
- [[aurora-asymmetry-and-update-induced-rotation-for-robust-hallucination-detection-in-llms-2606.29545]] — Aurora hallucination detection (broader LLM hallucination context)
- [[ctrl-rag-contrastive-likelihood-reward-reinforcement-learning-context-faithful-rag-2603.04406]] — CTRL-RAG context-faithful RAG (related RAG faithfulness theme)
