---
title: "CTRL-RAG: Contrastive Likelihood Reward Based Reinforcement Learning for Context-Faithful RAG Models"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [retrieval, rag, training, faithfulness, rl, llm]
sources: ["https://arxiv.org/abs/2603.04406"]
---

# CTRL-RAG: Contrastive Likelihood Reward Based Reinforcement Learning for Context-Faithful RAG Models

## Overview
With the growing use of Retrieval-Augmented Generation (RAG), training LLMs for context-sensitive reasoning and faithfulness is increasingly important. Existing RAG-oriented RL methods rely on external rewards that often fail to evaluate document faithfulness. This paper proposes CTRL-RAG with a Contrastive Likelihood Reward (CLR) that directly optimizes the log-likelihood gap between responses conditioned on prompts with and without supporting evidence. This encourages the model to extract relevant evidence and increase confidence when grounded in a specific context. Experiments show strong performance on single-hop, multi-hop, vertical-domain, and faithfulness benchmarks.

## Key Facts
- **Authors**: Unknown (arXiv 2603.04406)
- **Year**: 2026
- **arXiv**: [2603.04406](https://arxiv.org/abs/2603.04406)

## Key Contributions
- **Internal-external hybrid reward framework**: Combines Contrastive Likelihood Reward (CLR) with external correctness rewards
- **CLR mechanism**: Directly optimizes log-likelihood gap between responses with vs without supporting evidence — rewards evidence grounding and context confidence
- **No RAG self-reward mechanism prior**: First paper to establish a self-reward mechanism for context faithfulness in RAG
- **First-in-wiki**: First contrastive RL approach for context-faithful RAG model training
- **Orthogonal to**: Reason and Verify (2603.10143) — different methodology (RL vs verification-based); Faithfulness-QA (2604.25313) — different training paradigm

## Related Papers
- [[reason-and-verify-a-framework-for-faithful-retrieval-augmented-generation-2603.10143]] — Sibling: verification-based faithfulness framework, different from CTRL-RAG's contrastive RL approach
- [[faithfulness-qa-a-counterfactual-entity-substitution-dataset-for-training-context-faithful-rag-models-2604.25313]] — Counterfactual entity substitution dataset for faithfulness training
