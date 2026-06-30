---
title: "CreativityBench: Evaluating Agent Creative Reasoning via Affordance-Based Tool Repurposing"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [agent, benchmarking, reasoning, creativity, tool-use]
sources: ["https://arxiv.org/abs/2605.02910"]
---

# CreativityBench: Evaluating Agent Creative Reasoning via Affordance-Based Tool Repurposing

## Overview
CreativityBench is a benchmark for evaluating affordance-based creativity in LLMs — specifically, the ability to repurpose available objects by reasoning about their affordances and attributes rather than canonical usage. It constructs 14K grounded tasks requiring non-obvious but physically plausible solutions under constraints, built on a large affordance knowledge base (4K entities, 150K+ annotations).

## Key Facts
- **arXiv**: [2605.02910](https://arxiv.org/abs/2605.02910)
- **Theme**: llm agent benchmarking / creative reasoning / affordance-based tool repurposing / planning evaluation

## Key Contributions
- First benchmark specifically targeting affordance-based creative tool repurposing in LLMs
- 14K grounded tasks with 4K entity affordance KB — tests ability to identify correct object parts, their affordances, and the underlying physical mechanism
- Evaluates 10 state-of-the-art LLMs — reveals that general reasoning capability does not transfer to creative affordance discovery
- Chain-of-Thought and model scaling provide limited gains on this task — creative tool use remains a fundamental gap

## Related Papers
- [[emergent-concepts]] — Parent discovery chain
