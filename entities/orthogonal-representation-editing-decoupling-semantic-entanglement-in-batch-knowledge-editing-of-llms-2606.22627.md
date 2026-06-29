---
title: "Orthogonal Representation Editing: Decoupling Semantic Entanglement in Batch Knowledge Editing of LLMs"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [knowledge-editing, representation-engineering, batch-editing, llm]
sources: ["https://arxiv.org/abs/2606.22627"]
---

# Orthogonal Representation Editing: Decoupling Semantic Entanglement in Batch Knowledge Editing of LLMs

## Overview
Orthogonal Representation Editing (ORE) addresses the key failure mode of batch knowledge editing: semantic representation entanglement, where overlapping concepts and shared syntactic patterns accumulate interference in the representation space, reducing editing precision. ORE constructs a general semantic subspace and enforces orthogonal constraints on edit vectors in the hidden representation space, effectively decoupling semantic entanglement.

## Key Facts
- **Authors**: Wenhao Yu, Zhicong Lu, Bo Lv, Fangyin Ma, Kaiwen Wei, Shihao Yang, Nayu Liu
- **Year**: 2026 (Findings of ACL 2026)
- **arXiv**: [2606.22627](https://arxiv.org/abs/2606.22627)

## Key Contributions
- Identifies semantic representation entanglement as the root cause of batch editing degradation
- Performs edits in hidden representation space with orthogonal constraint enforcement on edit vectors
- Gated non-linear representation head for adaptive editing location learning and precise knowledge injection control
- Superior cross-lingual knowledge editing performance compared to existing methods

## Related Papers
- [[emergent-concepts]] — Parent emergent-concepts wiki page that this discovery extends
