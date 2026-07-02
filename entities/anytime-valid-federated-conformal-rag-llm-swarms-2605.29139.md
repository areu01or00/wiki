---
title: "Anytime-Valid Federated Conformal RAG for LLM Swarms"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [calibration, conformal-prediction, rag, multi-agent]
sources: ["https://arxiv.org/abs/2605.29139"]
---

# Anytime-Valid Federated Conformal RAG for LLM Swarms

## Overview
FC-RAG provides distribution-free coverage guarantees for answer sets produced by a bandwidth-limited swarm of weak language models. The paper extends fixed-horizon conformal RAG to anytime-valid sequential inference, enabling LLM swarms to maintain coverage guarantees across unbounded interaction horizons without requiring a priori calibration set size.

## Key Facts
- **Authors**: Dubey, Prasanjit; Huo, Xiaoming
- **Year**: 2026
- **arXiv**: [2605.29139](https://arxiv.org/abs/2605.29139)

## Key Contributions
- Anytime-valid extension of conformal prediction for federated LLM RAG — coverage guarantees hold at any stopping time, not just a fixed horizon
- Demonstrates that weak-LLM swarm aggregation can achieve coherent coverage even under bandwidth constraints
- Provides distribution-free marginal coverage over answer sets, independent of swarm composition

## Related Papers
- [[closing-the-reflection-gap-a-free-calibration-bonus-for-agentic-rl-2606.14211]] — Calibration bonus mechanism for agentic RL (different axis: RL training vs. inference-time coverage)
- [[calibration-is-not-control-llm-agent-oversight-needs-intervention-2606.21399]] — LLM agent oversight failure modes (same broad calibration/control axis)
