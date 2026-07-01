---
title: "Self-Improving Language Models with Bidirectional Evolutionary Search"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [self-improvement, evolutionary-search, post-training, llm, search]
sources: ["https://arxiv.org/abs/2605.28814"]
---

# Self-Improving Language Models with Bidirectional Evolutionary Search

## Overview
BES augments best-of-N sampling and tree search with bidirectional evolutionary operators: forward mutation (autoregressive expansion of partial trajectories) and backward crossover (recombination of completed trajectories into new candidates). Solves the entropy-collapse problem where narrow best-of-N search converges to locally optimal responses. Enables consistent gains on post-training tasks where mainstream algorithms fail to improve.

## Key Facts
- **Authors**: Xu, Guowei; Qi, Zhenting; Su, Huangyuan + 4 others
- **Year**: 2026
- **arXiv**: [2605.28814](https://arxiv.org/abs/2605.28814)

## Key Contributions
- **Bidirectional evolutionary search (BES)**: augments forward search with backward recombination operators that mix partial solution fragments across generations
- Solves the entropy-collapse problem: pure autoregressive expansion converges to a narrow mode; BES maintains population diversity across generations
- Evaluated on three open problem solving benchmarks (MATH, ARC, and a coding benchmark) — outperforms best-of-N and Monte Carlo tree search baselines
- Post-training experiments: BES enables consistent gains where DPO and PPO fail to improve on challenging tasks
- **First bidirectional evolutionary search algorithm applied to LLM self-improvement** — distinct from prior population-based evolutionary methods that lacked backward recombination

## Related Papers
- [[self-improvement-of-large-language-models-a-technical-overview-and-future-outlook-2603.25681]] — Parent survey: BES is a specific algorithm detailed within the broader self-improvement taxonomy survey
- *SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks* (2605.31433) — Sibling: both are self-improvement without external supervision; BES uses evolutionary search while SCOPE uses self-play co-evolution
