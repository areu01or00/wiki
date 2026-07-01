---
title: "Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [multi-agent, llm, latent-comms, architecture]
sources: ["https://arxiv.org/abs/2606.05711"]
---

# Beyond tokens: a unified framework for latent communication in LLM-based multi-agent systems

## Overview
Multi-agent LLM systems predominantly use natural language communication — token-by-token message exchange — which is interpretable but suffers from high inference cost, irreversible discretization loss, and ambiguity. This paper presents a unified 3-axis framework categorizing 18 latent communication methods: WHAT (embeddings/hidden states/KV-caches), WHICH alignment (latent-space/layer), and HOW fusion (concatenation/prepending/mathematical ops/cross-attention/cache restoration).

## Key Facts
- **Authors**: (from arxiv 2606.05711)
- **Year**: 2026
- **arXiv**: [2606.05711](https://arxiv.org/abs/2606.05711)

## Key Contributions
- First unified taxonomy of latent communication protocols in LLM multi-agent systems
- 3-axis framework: WHAT × WHICH × HOW — systematically categorizes 18 methods from 2024-2026
- Identifies 5 major design patterns and open challenges: cross-architecture alignment, latent channel security, edge compression, relationship to latent CoT
- Surfaces latent communication as a distinct research area orthogonal to text-based agent protocols

## Related Papers
- [[a-latent-computational-mode-in-large-language-models-2601.08058]] — Latent computational modes in LLMs
- [[argent-signaling-protocol-multi-agent-semantic-drift-2606.19356]] — Multi-agent signaling and semantic drift
- [[benchmarking-open-ended-multi-agent-coordination-in-language-agents-2606.08340]] — Multi-agent coordination benchmarking
