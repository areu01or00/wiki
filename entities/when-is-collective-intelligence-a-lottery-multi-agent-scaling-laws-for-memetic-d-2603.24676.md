---
title: "When Is Collective Intelligence a Lottery? Multi-Agent Scaling Laws for Memetic Drift in LLMs"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [multi-agent, scaling-laws, collective-intelligence, llm]
sources: ["https://arxiv.org/abs/2603.24676"]
---

# When Is Collective Intelligence a Lottery? Multi-Agent Scaling Laws for Memetic Drift in LLMs

## Overview
This paper investigates whether outcomes from multi-agent LLM systems reflect genuine collective reasoning or are instead artifacts of random drift — specifically studying how "memetic drift" (agents converging on arbitrary labels rather than grounded meanings) scales with the number of agents and model size. The authors establish scaling laws for when collective intelligence degrades into a lottery, providing both theoretical conditions and empirical measurements across multiple model families.

## Key Facts
- **Authors**: Hidenori Tanaka et al.
- **Year**: 2026
- **arXiv**: [2603.24676](https://arxiv.org/abs/2603.24676)

## Key Contributions
- First scaling law characterization of memetic drift in multi-agent LLM systems — shows that collective intelligence degrades predictably above a critical agent count threshold
- Demonstrates that label agreement between LLM agents does not imply semantic grounding; agents can converge on arbitrary conventions through drift rather than reasoning
- Reveals that larger models are NOT immune to memetic drift and in some configurations exhibit worse lottery behavior due to stronger self-confirmation
- Introduces controlled experimental framework (naming games variant) enabling systematic measurement of drift vs. reasoning across model families and agent counts

## Related Papers
- [[emergent-concepts]] — Parent discovery chain
