---
title: "SokoBench: Evaluating Long-Horizon Planning and Reasoning in Large Language Models"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reasoning, llm, benchmark, planning]
sources: ["https://arxiv.org/abs/2601.20856"]
---

# SokoBench: Evaluating Long-Horizon Planning and Reasoning in Large Language Models

## Overview
This paper systematically assesses the long-horizon planning and reasoning capabilities of state-of-the-art Large Reasoning Models (LRMs) using Sokoban puzzles as a controlled testbed. The key finding is a consistent performance degradation when solutions require more than 25 moves, suggesting fundamental architectural constraints on forward planning capacity that test-time scaling alone cannot overcome.

## Key Facts
- **arXiv**: [2601.20856](https://arxiv.org/abs/2601.20856)
- **Theme**: LLM planning / long-horizon reasoning benchmark / Sokoban / architectural limitations

## Key Contributions
- Sokoban-based benchmark isolating long-horizon planning from state persistence
- Discovery of the 25-move degradation threshold in LRM forward planning
- Evidence that PDDL tooling provides only modest improvements, pointing to inherent architectural limitations
- First systematic mapping of LRM planning capacity vs. test-time compute scaling

## Related Papers
- [[ask-dont-judge-binary-questions-for-interpretable-llm-evaluation-and-self-improvement-2606.27226]] — Binary-question LLM evaluation framework, orthogonal eval methodology
