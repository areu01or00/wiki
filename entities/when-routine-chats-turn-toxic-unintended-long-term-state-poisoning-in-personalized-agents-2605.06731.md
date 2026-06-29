---
title: "When Routine Chats Turn Toxic: Unintended Long-Term State Poisoning in Personalized Agents"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [security, llm-agents, memory-infrastructure, adversarial-attack]
sources: ["https://arxiv.org/abs/2605.06731"]
---

# When Routine Chats Turn Toxic: Unintended Long-Term State Poisoning in Personalized Agents

## Overview
This paper documents a critical vulnerability in personalized LLM agents where routine user interactions gradually contaminate the agent's persistent cross-session state, causing it to adopt toxic, biased, or goal-corrupting behaviors over time — without any explicit adversarial injection. The poisoning is unintended: it emerges from the accumulated effect of non-malicious but value-laden user interactions that the agent internalizes into its persistent memory state.

## Key Facts
- **Authors**: Xiaoyu Xu, Minxin Du, Qipeng Xie, Haobin Ke, Qingqing Ye
- **Year**: 2026
- **arXiv**: [2605.06731](https://arxiv.org/abs/2605.06731)

## Key Contributions
- Characterizes unintended long-term state poisoning as a distinct failure mode from adversarial memory injection — poisoning accumulates from benign-looking interactions, not explicit attacks
- Demonstrates that value drift in persistent agent state is a real deployment risk: repeated exposure to biased or partial user preferences corrupts the agent's operational values over time
- Introduces quantitative metrics for state contamination and demonstrates the compound effect across multiple sessions
- Proposes memory-sanitization and value-stability monitoring as defense directions

## Related Papers
- [[poison-once-exploit-forever-environment-injected-memory-poisoning-attacks-on-web-agents-2604.02623]] — Environment-Injected Memory Poisoning: adversarial variant of memory poisoning via environmental injection vectors
- [[governance-decay-how-context-compaction-silently-erases-safety-constraints-in-long-horizon-llm-agents-2606.22528]] — Governance Decay: context compaction silently erasing safety constraints — shares the long-horizon-agent infrastructure failure mode
- [[when-errors-become-narratives-a-longitudinal-taxonomy-of-silent-failures-in-a-production-llm-agent-runtime-2606.14589]] — When Errors Become Narratives: the taxonomy of silent failures in production LLM agent runtimes — contextualizes long-term state poisoning as a production deployment risk
