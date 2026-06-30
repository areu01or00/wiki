---
title: "DYNA: Dynamic Episodic Memory Networks for Augmenting Large Language Models with Temporal Knowledge Graphs in Continuous Learning"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [architecture, llm, memory, knowledge-update]
sources: ["https://arxiv.org/abs/2606.15778"]
---

# DYNA: Dynamic Episodic Memory Networks for Augmenting Large Language Models with Temporal Knowledge Graphs in Continuous Learning

## Overview
DYNA augments a frozen LLM with a temporal knowledge graph (TKG) where events are nodes and temporal relations are directed, timestamped edges. At query time, DYNA retrieves relevant nodes via random walks and centrality measures, then augments the LLM's response with the retrieved temporal context. This enables the model to incorporate new knowledge without costly retraining or catastrophic forgetting — the TKG serves as an external, updatable memory that doesn't require gradient updates to the base model.

## Key Facts
- **Authors**: DYNA Authors
- **Year**: 2026
- **arXiv**: [2606.15778](https://arxiv.org/abs/2606.15778)

## Key Contributions
- Temporal Knowledge Graph (TKG) as external episodic memory for frozen LLMs — events as nodes, temporal relations as timestamped directed edges
- Random walk + centrality-based retrieval from TKG at inference time — no gradient updates needed
- Addresses catastrophic forgetting and knowledge obsolescence simultaneously — new events append to TKG without modifying model weights
- Evaluated on temporal question answering across three datasets — shows LLM can reason about temporal relations it never saw during training

## Related Papers
- [[attribution-guided-continual-learning-for-llms-2605.05285]] — Attribution-Guided Continual Learning for LLMs — addresses catastrophic forgetting in LLMs via gradient-direction preservation; DYNA avoids the forgetting problem entirely by never updating model weights
- [[elasticmem-latent-memory-as-a-learnable-resource-for-llm-agents-2605.30690]] — Elastic Memory — learnable latent memory as a resource for LLM agents; DYNA complements this with a structured temporal graph instead of latent vectors
- [[supersede-diagnosing-and-training-the-memory-update-gap-2606.27472]] — Supersede — diagnoses and trains the memory update gap in LLMs; DYNA addresses the same problem via a frozen-LLM + temporal graph architecture that sidesteps the update gap entirely
