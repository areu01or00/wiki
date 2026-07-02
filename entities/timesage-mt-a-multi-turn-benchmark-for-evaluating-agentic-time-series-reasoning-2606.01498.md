---
title: "TimeSage-MT: A Multi-Turn Benchmark for Evaluating Agentic Time Series Reasoning"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [agent-eval, time-series, benchmarking, llm]
sources: ["https://arxiv.org/abs/2606.01498"]
---

# TimeSage-MT: A Multi-Turn Benchmark for Evaluating Agentic Time Series Reasoning

## Overview
Time series data informs critical decisions across healthcare, finance, infrastructure, and climate domains. While LLM agents can analyze data through natural language and tools, it remains unclear whether they can conduct reliable time series analysis across multi-turn conversations. TimeSage-MT provides a benchmark with 240 tasks and 2,680 dialogue turns spanning basic exploration to decision-oriented analysis — the first multi-turn agentic evaluation for time series reasoning.

## Key Facts
- **Authors**: Kong, Yaxuan; Yao, Qingren; Nie, Yuqi + 7 others
- **Year**: 2026
- **arXiv**: [2606.01498](https://arxiv.org/abs/2606.01498)

## Key Contributions
- Introduces **TimeSage-MT** — first multi-turn benchmark for agentic time series reasoning with 240 tasks across 8 real-world domains
- Covers 2,680 dialogue turns from basic exploration to decision-oriented analysis
- Systematically evaluates LLM agent capabilities across 8 domains: healthcare, finance, infrastructure, climate, energy, retail, manufacturing, telecommunications

## Related Papers
- [[when-less-is-enough-efficient-inference-via-collaborative-reasoning-2605.01111]] — Collaborative reasoning principles extend to multi-turn time series analysis where different reasoning modes handle routine vs. complex analysis turns
- [[selfbudgeter-adaptive-token-allocation-for-efficient-llm-reasoning-2505.11274]] — Adaptive token allocation is relevant since multi-turn time series conversations have varying complexity per turn
- [[badger-bridging-agentic-and-deterministic-evaluation-for-generative-enterprise-reasoning-2606.02109]] — Both BADGER and TimeSage-MT pioneer agentic evaluation beyond single-step benchmarks
