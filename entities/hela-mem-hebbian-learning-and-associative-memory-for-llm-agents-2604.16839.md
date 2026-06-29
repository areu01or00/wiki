---
title: "HeLa-Mem: Hebbian Learning and Associative Memory for LLM Agents"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [memory, hebbian-learning, neuroscience, agent, llm, cross-discipline, architecture]
sources: ["https://arxiv.org/abs/2604.16839"]
---

# HeLa-Mem: Hebbian Learning and Associative Memory for LLM Agents

## Overview
First paper in the wiki to apply **Hebbian learning dynamics** ("neurons that fire together wire together") to LLM-agent long-term memory as a dynamic graph with associative retrieval. Reframes long-term memory as a learnable associative network rather than a passive retrieval store, providing a neuroscience-grounded primitive for memory-evolution in long-horizon agents.

## Key Facts
- **Authors**: Zhu, Jinchang; Li, Jindong; Zhang, Cheng; Liu, Jiahong et al.
- **Year**: 2026
- **arXiv**: [2604.16839](https://arxiv.org/abs/2604.16839)
- **Online Date**: 2026-04-18
- **Domain**: Hebbian neuroscience × LLM-agent-memory × associative-retrieval

## Key Contributions
- **Hebbian-dynamics LLM memory**: applies "fire-together-wire-together" learning rule to LLM-agent memory, allowing the memory graph to *evolve* through use rather than being statically written — a primitive that existing memory systems don't have
- **Associative retrieval via graph dynamics**: replaces semantic-similarity embedding retrieval with associative-retrieval based on co-activation history, surfacing memory items that were useful together in past interactions
- **Long-term coherence for fixed-context agents**: solves the "fixed context window cannot preserve coherence across extended interactions" problem by externalizing memory into a learnable associative network rather than scaling context
- **Cross-discipline primitive**: bridges Hebbian-learning neuroscience × LLM-agent-memory — provides a *learnable* memory primitive distinct from ZenBrain's static 7-layer organization (Run 74 sibling)
- **Inverts the memory-as-store paradigm**: instead of memory being a write-only or retrieve-only store, HeLa-Mem makes memory *learn* from interaction patterns, complementing static-memory primitives like EvoEmbedding (Run 65) and Memory-R2 (Run 55)

## Related Papers
- [[zenbrain-a-neuroscience-inspired-7-layer-memory-architecture-for-autonomous-ai-s-2604.23878]] — Sibling from Run 74 that organizes memory by 7 neuroscience layers (static); HeLa-Mem complements with dynamic Hebbian evolution
- [[memory-r2-fair-credit-assignment-for-long-horizon-memory-augmented-llm-agents-2605.21768]] — Run 55 sibling on long-horizon memory credit assignment; HeLa-Mem's Hebbian learning provides an alternative primitive for memory-evolution
- [[memory-is-reconstructed-not-retrieved-graph-memory-llm-agents-2606.06036]] — Sibling that frames memory as graph-reconstruction; HeLa-Mem extends with Hebbian dynamics for associative retrieval
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — Run 65 sibling on evolvable embeddings for long-context retrieval; HeLa-Mem complements with Hebbian-evolved associative memory
- [[externalization-llm-agents-unified-review-memory-skills-protocols-harness-engineering-2604.08224]] — Cross-discipline primitive on externalization-of-memory in LLM agents; HeLa-Mem provides a neuroscience-grounded mechanism for this externalization