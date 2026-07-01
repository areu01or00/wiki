---
title: "Diagnosing and Mitigating Context Rot in Long-horizon Search"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [long-context, llm, context-management, retrieval-augmentation]
sources: ["https://arxiv.org/abs/2606.29718"]
---

# Diagnosing and Mitigating Context Rot in Long-horizon Search

## Overview
Documents and addresses the "context rot" phenomenon in LLM agents performing long-horizon deep search tasks: as context length grows, models increasingly give up prematurely or provide uncertain answers rather than reasoning through accumulated context. Evaluates four flagship open-source models across three benchmarks, finding rot is prevalent and undernoticed. Proposes context management (7 methods across 3 categories) and rot-aware rejection sampling as mitigation strategies, which can be combined for further gains.

## Key Facts
- **Authors**: Unknown
- **Year**: 2026
- **arXiv**: [2606.29718](https://arxiv.org/abs/2606.29718)

## Key Contributions
- First systematic characterization of context rot in deep search scenarios
- Finds rot causes premature abandonment and uncertain answers (not just accuracy degradation)
- Context management: 7 methods evaluated across 3 categories (performance, cost, rot-impact)
- Rot-aware filtering strategy for rejection sampling (3 aggregation methods)
- Shows context management + rejection sampling are combinable for additive improvements

## Related Papers
- [[governance-decay-how-context-compaction-silently-erases-safety-constraints-in-long-horizon-llm-agents-2606.22528]] — Governance Decay also studies context degradation in long-horizon settings, but focuses on safety constraint erasure vs information retrieval degradation
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Plans Don't Persist studies context management as a load-bearing component for agent planning, complementary to context rot's degradation analysis
- [[randomized-yarn-improves-length-generalization-for-long-context-reasoning-2606.23687]] — Randomized-YaRN addresses length generalization orthogonally, focusing on positional encoding adaptation vs rot-mitigation strategies
