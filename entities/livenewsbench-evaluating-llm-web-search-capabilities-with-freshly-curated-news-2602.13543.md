---
title: "LiveNewsBench: Evaluating LLM Web Search Capabilities with Freshly Curated News"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [evaluation, agentic, web-search, benchmarking, llm]
sources: ["https://arxiv.org/abs/2602.13543"]
---

# LiveNewsBench: Evaluating LLM Web Search Capabilities with Freshly Curated News

## Overview
LiveNewsBench is a benchmark for assessing agentic web search capabilities of LLMs using freshly curated news articles. It addresses the key challenge of evaluating whether LLMs can truly access and reason over real-time information beyond their training data. Questions are intentionally difficult multi-hop queries requiring search, page visits, and reasoning — ensuring clear separation between internal knowledge and search capability.

## Key Facts
- **Authors**: Yunfan Zhang, Kathleen McKeown, Smaranda Muresan
- **Year**: 2026
- **arXiv**: [2602.13543](https://arxiv.org/abs/2602.13543)

## Key Contributions
- First benchmark for agentic web search using freshly curated news (beyond training data)
- Multi-hop questions requiring search + page visits + reasoning
- Automated data curation pipeline enabling frequent benchmark updates
- Supports large-scale training dataset construction for agentic search models
- Human-verified test set subset for reliable evaluation
- First paper in the wiki specifically targeting live/fresh web search evaluation for LLM agents

## Related Papers
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — Tool-use planning benchmark; orthogonal axis (PlanBench evaluates tool-use planning, LiveNewsBench evaluates real-time information retrieval via web search)
- [[agora-an-archive-grounded-benchmark-for-agentic-workplace-document-reasoning-2606.24526]] — Document-reasoning benchmark; orthogonal axis (AGORA evaluates archive-grounded reasoning, LiveNewsBench evaluates live web search and real-time information access)
- [[act-as-a-real-researcher-aarri-bench-frontier-llms-agentic-research-lifecycle-2606.07462]] — Agentic research lifecycle benchmark; orthogonal axis (AARRI evaluates research agent lifecycle, LiveNewsBench specifically targets web-search capability evaluation with fresh news data)
