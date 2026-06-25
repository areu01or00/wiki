---
title: "The Periodic Table of LLM Reasoning: A Structured Survey of Reasoning Paradigms, Abstractions, Building Blocks, and Open Challenges"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [survey, reasoning, llm, taxonomy, chain-of-thought]
sources: ["https://arxiv.org/abs/2606.11470"]
---

# The Periodic Table of LLM Reasoning: A Structured Survey of Reasoning Paradigms, Abstractions, Building Blocks, and Open Challenges

## Overview
This paper organizes the fragmented landscape of LLM reasoning research into a single taxonomy the authors call the "Periodic Table of LLM Reasoning," grouping methods by paradigm (e.g., explicit CoT, latent reasoning, tool-augmented, programmatic), abstraction level (single-step, multi-step, recursive), and building block (prompt scaffold, decoder, verifier, search procedure). Rather than cataloging individual papers, the survey surfaces the cross-cutting structural axes that distinguish reasoning approaches and uses them to map where each method sits, where the open problems cluster, and which combinations remain unexplored. The result is a navigational artifact that lets a reader locate a method by *role in a reasoning pipeline* rather than by author or benchmark score.

## Key Facts
- **Authors**: Anand, Avinash; Ramesh, Mahisha; Mittal, Avni
- **Year**: 2026
- **arXiv**: [2606.11470](https://arxiv.org/abs/2606.11470)
- **Subjects**: cs.CL

## Key Contributions
- Proposes a 3-axis taxonomy (paradigm × abstraction × building block) for LLM reasoning methods, deliberately modeled on the periodic table's role in chemistry as a navigational map rather than a ranking.
- Maps ~120 representative methods (2022-2026) onto the taxonomy and identifies "empty cells" — paradigm/abstraction/building-block combinations that no published method currently occupies — as concrete research directions.
- Separates *reasoning-enabling primitives* (chain-of-thought, ToT, self-consistency, verifier-driven search, latent thoughts) from *reasoning-composing primitives* (recursion, tool invocation, memory), arguing most current work sits in the first bucket and the second is the larger open frontier.
- Provides an open-source taxonomy repository with bidirectional links between methods and taxonomy cells, enabling literature-survey and benchmark-selection tooling that the authors demonstrate on three case studies.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on 2026-06-25 as a fresh 2026 survey synthesizing the LLM reasoning landscape.
