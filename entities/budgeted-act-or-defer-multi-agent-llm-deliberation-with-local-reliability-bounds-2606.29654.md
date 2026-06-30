---
title: "Budgeted Act-or-Defer Multi-Agent LLM Deliberation with Local Reliability Bounds"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [multi-agent, llm, reasoning, deliberation]
sources: ["https://arxiv.org/abs/2606.29654"]
---

# Budgeted Act-or-Defer Multi-Agent LLM Deliberation with Local Reliability Bounds

## Overview
Multi-agent deliberation among LLMs can improve reasoning, but deployment requires deciding when the current answer is reliable enough to act on and when it should be escalated to human review. This paper formulates budgeted act-or-defer decision making — at each deliberation round, the system maps the debate prefix to a low-dimensional state and computes a k-nearest-neighbor lower confidence bound to determine whether to act or defer.

## Key Facts
- **Authors**: N/A (from abstract)
- **Year**: 2026
- **arXiv**: [2606.29654](https://arxiv.org/abs/2606.29654)

## Key Contributions
- Formalizes budgeted act-or-defer decision making for multi-agent LLM deliberation
- Uses k-nearest-neighbor lower confidence bounds on deliberation state for reliability estimation
- Provides a deployment-ready framework for deciding when LLM agent consensus is sufficient vs. when human escalation is needed
- First act-or-defer deliberation reliability framework for multi-agent LLMs in the wiki

## Related Papers
- [[emergent-concepts]] — Parent emergent concepts chain
