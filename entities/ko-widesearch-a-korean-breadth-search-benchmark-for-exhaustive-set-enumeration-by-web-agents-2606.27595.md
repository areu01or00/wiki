---
title: "Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [llm-agents, benchmarking, web-agents, evaluation-methodology, multilingual]
sources: ["https://arxiv.org/abs/2606.27595"]
---

# Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents

## Overview
Web-agent benchmarks overwhelmingly measure depth — pinning one obscure answer behind a chain of constraints — while breadth, exhaustively enumerating a closed set and filling each item's attributes, is barely evaluated, especially outside English. Breadth is also hard to build: certifying that a gold set is complete and every cell correct is far costlier than checking a single answer. This paper introduces Ko-WideSearch, a Korean breadth-search benchmark built by an automated synthesize-and-verify pipeline. Each task names a set-parent entity — a TV season, a dynasty, a league — and the agent must exhaustively enumerate all members, a fundamentally different capability than depth-first retrieval.

## Key Facts
- **Authors**: Unknown (per arxiv page)
- **Year**: 2026
- **arXiv**: [2606.27595](https://arxiv.org/abs/2606.27595)

## Key Contributions
- First breadth-first web agent benchmark (vs standard depth-first) measuring exhaustive set enumeration
- Korean language evaluation — addresses English-centric benchmarking gap
- Automated synthesize-and-verify pipeline for gold-set certification
- Orthogonal to depth-first agent benchmarks (WebArena, GAIA, Mind2Web) — tests systematic completeness rather than path efficiency

## Related Papers
- [[agora-an-archive-grounded-benchmark-for-agentic-workplace-document-reasoning-2606.24526]] — Archive-grounded agentic workplace document reasoning benchmark
- [[enterpriseclawbench-benchmarking-agents-from-real-workplace-sessions-2606.23654]] — Real workplace session agent benchmarking
- [[coffeebench-benchmarking-long-horizon-llm-agents-in-heterogeneous-multi-agent-economies-2606.16613]] — Multi-agent economic benchmark for LLM agents
