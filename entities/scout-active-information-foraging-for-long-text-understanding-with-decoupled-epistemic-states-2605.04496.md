---
title: "SCOUT: Active Information Foraging for Long-Text Understanding with Decoupled Epistemic States"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [long-context, information-foraging, retrieval, LLM-architecture]
sources: ["https://arxiv.org/abs/2605.04496"]
---

# SCOUT: Active Information Foraging for Long-Text Understanding with Decoupled Epistemic States

## Overview
SCOUT addresses the long-text understanding (LTU) problem at million-token scale by decoupling epistemic states (what the model knows vs. what it needs to know) from the main reasoning process. Query-relevant information is typically sparse relative to the full context; SCOUT uses an active information foraging strategy that selectively retrieves and verifies sparse relevant segments without loading the full context into attention. This contrasts with end-to-end long-context models that suffer from attention dilution and high token consumption.

## Key Facts
- **arXiv**: [2605.04496](https://arxiv.org/abs/2605.04496)

## Key Contributions
- Introduces active information foraging for LTU: separate epistemic state tracking from core reasoning
- Identifies query-relevant information sparsity as the fundamental challenge in long-context understanding
- Proposes decoupled architecture that selectively foraging relevant segments rather than processing full context
- Achieves better reasoning fidelity than end-to-end long-context models at lower computational cost

## Related Papers
- [[endprompt-efficient-long-context-extension-via-terminal-anchoring-2605.14589]] — both address long-context efficiency challenges
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — long-context retrieval and memory architecture for LLM agents
