---
title: "DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image Generation"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [multi-agent, data-construction, self-evolution, feedback-loop, text-rich-image]
sources: ["https://arxiv.org/abs/2606.31537"]
---

# DataEvolver: Self-Evolving Multi-Agent Data Construction for Text-Rich Image Generation

## Overview
DataEvolver is a self-evolving multi-agent framework for text-rich image data construction that treats data construction as feedback-driven policy evolution. A Retriever collects candidates, a Verifier assigns quality scores and rejection causes, a Critic synthesizes round-level feedback into semantic feedback, and a Generator completes under-covered regions through targeted synthesis. The updated feedback memory guides the next construction round.

## Key Facts
- **Authors**: Unknown (arXiv 2606.31537)
- **Year**: 2026
- **arXiv**: [2606.31537](https://arxiv.org/abs/2606.31537)

## Key Contributions
- First self-evolving multi-agent data construction framework that recycles rejected sample failure signals as actionable feedback
- Four-role agent architecture: Retriever → Verifier → Critic → Generator, with feedback memory between rounds
- Improves OCR-F1 by 85.3% on TextScenesHQ and 35.3% on LongTextBench vs strongest baseline at 0.75M scale (PixArt-alpha)
- Demonstrates that rejected samples contain useful failure signals that, when fed back, prevent repeating the same errors
- Consistent improvements transfer across both evaluated benchmarks and to Show-o2 (not tied to single downstream generator)

## Related Papers
- [[beyond-individual-intelligence-surveying-collaboration-failure-attribution-and-self-evolution-in-llm-based-multi-agent-systems-2605.14892]] — Survey of self-evolution in multi-agent systems (complementary — surveys the space; DataEvolver introduces the specific Retriever-Verifier-Critic-Generator feedback architecture)
- [[q-evolve-self-evolving-llm-agents-with-in-distribution-optimization-2606.07367]] — Q-Evolve self-evolving agents via in-distribution optimization (orthogonal — Q-Evolve optimizes agent weights; DataEvolver evolves the data construction policy itself)
- [[autodata-an-agentic-data-scientist-to-create-high-quality-synthetic-data-2606.25996]] — Autodata agentic data scientist for synthetic data (orthogonal — single-agent synthetic data vs multi-agent feedback-driven data construction evolution)
- [[rise-reliable-improvement-in-self-evolving-vision-language-models-2605.20914]] — RISE self-evolving VLMs (orthogonal — RISE evolves VLMs; DataEvolver evolves the data construction pipeline)
