---
title: "LLM-Guided Planning for Multi-hop Reasoning over Multimodal Nuclear Regulatory Documents"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, planning, multi-hop, multimodal, retrieval, domain-specific]
sources: ["https://arxiv.org/abs/2606.29399"]
---

# LLM-Guided Planning for Multi-hop Reasoning over Multimodal Nuclear Regulatory Documents

## Overview
This paper frames nuclear regulatory document review as a multi-hop reasoning task requiring evidence assembly across tens of thousands of pages spanning multiple chapters. An LLM acts as a planning agent that decomposes the review task and orchestrates retrieval across the document corpus, producing structured judgments grounded in cross-referenced evidence.

## Key Facts
- **Authors**: Jeon, Mingyu; Kim, Bokyeong; Cho, Suwan + 2
- **Year**: 2026
- **arXiv**: [2606.29399](https://arxiv.org/abs/2606.29399)

## Key Contributions
- First application of LLM-as-planner to structured regulatory document reasoning
- Proposes a planning decomposition that explicitly tracks evidence provenance across hops
- Demonstrates multi-modal (text + table + figure) retrieval within a single reasoning framework
- Establishes a new benchmark: nuclear regulatory multi-hop QA requiring cross-chapter assembly

## Related Papers
- [[emergent-concepts]] — Parent emergent-concepts chain for reasoning/retrieval discovery context
