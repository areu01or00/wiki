---
title: "ReSequel: Robust LLM-assisted Query Rewriting and Optimization using Templatization and Sampling"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [database, llm, inference-efficiency]
sources: ["https://arxiv.org/abs/2606.20853"]
---

# ReSequel: Robust LLM-assisted Query Rewriting and Optimization using Templatization and Sampling

## Overview
ReSequel is an outer optimization layer on top of existing DBMSs that rewrites SQL queries using LLMs. It leverages catalog and statistical metadata to infer template-specific rules that guide the LLM toward effective query transformations, then generates, verifies, and ranks rewritten query variants on sampled data to ensure result correctness and runtime improvements.

## Key Facts
- **Authors**: [Authors on arXiv]
- **Year**: 2026
- **arXiv**: [2606.20853](https://arxiv.org/abs/2606.20853)

## Key Contributions
- Template-specific LLM-guided query rewriting using catalog and statistical metadata
- Verify-and-rank rewritten query variants on sampled data for correctness guarantees
- Workload-level speedups up to 16x over native DBMSs and 22x over prior LLM-based systems
- Works across PostgreSQL, MySQL, and DuckDB with eight benchmarks
