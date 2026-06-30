---
title: "EpiEvolve: Self-Evolving Agents for Streaming Pandemic Forecasting under Regime Shifts"
created: 2026-06-01
updated: 2026-06-01
type: entity
tags: [self-evolving agent, llm-agent]
sources: ["https://arxiv.org/abs/2606.05513"]
---

# EpiEvolve: Self-Evolving Agents for Streaming Pandemic Forecasting under Regime Shifts

## Overview
EpiEvolve is a self-evolving LLM agent for streaming pandemic forecasting that adapts to regime shifts by storing forecast outcomes in hierarchical episodic memory, reflecting on delayed labels, and distilling recurring errors into strategic rules. It achieves 0.629 accuracy vs 0.325 for CDC ensemble, reducing regime-shift recovery lag from 5 to 2 weeks.

## Key Contributions
- Self-evolving agent architecture: fixed-weight LLM forecaster + hierarchical episodic memory + reflection + regime-aware retrieval
- Chronological protocol preventing future leakage; ablates reflection, strategic memory, and regime-aware retrieval contributions
- Achieves 0.629 average accuracy vs 0.561 static backbone and 0.325 CDC ensemble
- Reduces recovery lag after regime shifts from 5 weeks to 2 weeks
- First streaming-pandemic-forecasting LLM agent with episodic memory and regime-shift adaptation

## Key Facts
- **arXiv**: [2606.05513](https://arxiv.org/abs/2606.05513)
- **Date**: 2026-06-01

## Related Papers
- [[emergent-concepts]] — Parent emergent concepts tracking page
