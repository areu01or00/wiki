---
title: "LoopTrap: Termination Poisoning Attacks on LLM Agents"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [agent-security, adversarial, llm-agents]
sources: ["https://arxiv.org/abs/2605.05846"]
---

# LoopTrap: Termination Poisoning Attacks on LLM Agents

## Overview
LoopTrap demonstrates that adversaries can inject malicious prompts into an LLM agent's context to poison its termination condition, causing the agent to either loop indefinitely or exit prematurely. The attack exploits the self-evaluation step in iterative agent loops — by distorting what the agent believes is "progress" toward task completion.

## Key Facts
- **arXiv**: [2605.05846](https://arxiv.org/abs/2605.05846)

## Key Contributions
- Identifies termination poisoning as a novel attack surface in LLM agentic loops
- Shows that self-directed loop mechanisms (reason-act-evaluate) are vulnerable to context injection
- Proposes detection countermeasures based on consistency checks across loop iterations

## Related Papers
- [[metis-learning-to-jailbreak-llms-via-self-evolving-metacognitive-policy-optimization-2605.10067]] — Metis: Self-evolving metacognitive policy optimization for LLM security
- [[the-metacognitive-monitoring-battery-a-cross-domain-benchmark-for-llm-self-monitoring-2604.15702]] — Metacognitive monitoring battery for LLM self-monitoring
