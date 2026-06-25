---
title: "Autodata: An agentic data scientist to create high quality synthetic data"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [data, synthetic-data, agents, llm-research, training-data]
sources: ["https://arxiv.org/abs/2606.25996"]
---

# Autodata: An agentic data scientist to create high quality synthetic data

## Overview
Autodata is a general method that uses AI agents as data scientists to build high-quality training and evaluation data via meta-optimization, framing synthetic-data construction as an agentic iterative loop over schema design, sample generation, quality filtering, and rubric verification. The authors train (meta-optimize) the agentic data scientist end-to-end and show that the resulting synthetic datasets match or exceed the downstream model quality of carefully curated human-authored datasets while being produced at a fraction of the cost.

## Key Facts
- **Authors**: Kulikov, Ilia, Whitehouse, Chenxi, Wu, Tianhao
- **Year**: 2026
- **Date**: 2026-06-24
- **arXiv**: [2606.25996](https://arxiv.org/abs/2606.25996)
- **Subjects**: Artificial Intelligence (cs.AI)

## Key Contributions
- Agentic loop formulation: AI agents as data scientists performing schema design, generation, filtering, and verification
- Meta-optimization procedure that trains the agentic data scientist end-to-end
- Empirical demonstration that synthetic data from meta-optimized agents matches human-curated data quality on downstream tasks
- Cost-quality Pareto improvement over manually curated datasets

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered
