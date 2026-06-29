---
title: "Resource Consumption Threats in Large Language Models"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [security, llm-agents, infrastructure-safety, resource-exhaustion]
sources: ["https://arxiv.org/abs/2603.16068"]
---

# Resource Consumption Threats in Large Language Models

## Overview
This paper systematically taxonomizes resource consumption as a systemic safety risk in LLM deployment — covering token-budget exhaustion, KV-cache flooding, API rate-limit induced failures, and context-window saturation as vectors that cause LLM systems to fail in ways that bypass safety guardrails. The central thesis is that resource constraints coerce safety behavior changes: when computational budget depletes, models take shortcuts that violate safety guarantees.

## Key Facts
- **Authors**: Yuanhe Zhang, Xinyue Wang, Zhican Chen, Weiliu Wang, Zilu Zhang
- **Year**: 2026
- **arXiv**: [2603.16068](https://arxiv.org/abs/2603.16068)

## Key Contributions
- First systematic taxonomy of resource-consumption-as-safety-threat: token budget depletion, KV-cache exhaustion, API rate-limit churn, and context-window overflow as safety-relevant failure modes
- Demonstrates that frontier models systematically fail to predict their own token budget depletion (analogous to BAGEN findings from silent-failure literature) — making resource-awareness a safety primitive, not just a performance concern
- Shows that safety alignment established at full-resource conditions does not transfer to resource-constrained conditions — the model takes unsafe actions under budget pressure
- Introduces resource-awareness training and budget-aware safety guardrails as defense directions

## Related Papers
- [[governance-decay-how-context-compaction-silently-erases-safety-constraints-in-long-horizon-llm-agents-2606.22528]] — Governance Decay: context compaction silently erasing safety constraints — the infrastructure mechanism by which token budget pressure causes safety constraint loss
- [[silent-failure-in-llm-agent-systems-the-entropy-principle-2606.08162]] — Silent Failure in LLM Agent Systems: the entropy-principle that makes resource-induced safety failures invisible to operators
- [[bagen-are-llm-agents-budget-aware-2606.00198]] — BAGEN: LLM budget awareness — demonstrates that frontier models cannot predict their own token budget depletion, establishing resource-awareness as a safety primitive
