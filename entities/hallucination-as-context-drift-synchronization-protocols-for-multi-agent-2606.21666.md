---
title: "Hallucination as Context Drift: Synchronization Protocols for Multi-Agent LLM Systems"
created: 2026-06-01
updated: 2026-06-01
type: entity
tags: [multi-agent hallucination, llm-agent]
sources: ["https://arxiv.org/abs/2606.21666"]
---

# Hallucination as Context Drift: Synchronization Protocols for Multi-Agent LLM Systems

## Overview
This paper identifies context drift — divergence of internal knowledge states between concurrent agents — as a primary source of hallucination in multi-agent LLM systems, distinct from model incapacity. It proposes the Shared State Verification Protocol (SSVP) and Context Divergence Score (CDS) as first-class primitives for multi-agent LLM design.

## Key Contributions
- Defines context drift as hallucination source: knowledge-state discrepancy between agents causes joint reasoning failures
- Introduces Context Divergence Score (CDS): lightweight scalar quantifying agent-pair discrepancy across spatial/temporal/task dimensions
- Proposes Shared State Verification Protocol (SSVP): periodic compressed state-summary exchange with high-divergence flagging
- Key finding: full-broadcast synchronization increases hallucination rate by 34% (contamination effect); SSVP reduces HR from 0.658 to 0.463 with 58% fewer API calls
- First paper to reframe hallucination mitigation as a distributed systems problem in multi-agent LLM design

## Key Facts
- **arXiv**: [2606.21666](https://arxiv.org/abs/2606.21666)
- **Date**: 2026-06-01

## Related Papers
- [[emergent-concepts]] — Parent emergent concepts tracking page
