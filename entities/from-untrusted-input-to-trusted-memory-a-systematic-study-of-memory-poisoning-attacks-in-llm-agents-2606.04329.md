---
title: "From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [agentic-security, memory-systems, adversarial-attack, persistent-state]
sources: ["https://arxiv.org/abs/2606.04329"]
---

# From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents

## Overview
Memory poisoning is a core threat in LLM-based agents: a single adversarial memory write can exert long-term influence over agent behavior across sessions. This paper systematically categorizes four memory write channels (user input, retrieved documents, tool outputs, and cross-session context) and evaluates how untrusted input in any channel can corrupt the agent's persistent memory state. The authors propose defense strategies that distinguish trusted from untrusted input at memory-write time, preventing the agent from treating adversarial content as verified memory.

## Key Facts
- **Authors**: Pritam Dash, Tongyu Ge, Aditi Jain, Tanmay Shah, Zhiwei Shang
- **Year**: 2026
- **arXiv**: [2606.04329](https://arxiv.org/abs/2606.04329)

## Key Contributions
- First systematic taxonomy of memory poisoning attack surfaces across four write channels in LLM agents
- Identifies that cross-session context and tool output channels are the most exploitable poisoning vectors
- Shows that memory trust verification at write-time (not at retrieval-time) is the effective defense primitive
- Evaluates defenses against real-world agent deployments with persistent memory across multiple sessions

## Related Papers
- [[hidden-in-memory-sleeper-memory-poisoning-in-llm-agents-2605.15338]] — Sleeper memory poisoning (Run 124) — persistent, dormant poisoning that activates under specific triggers
- [[poison-once-exploit-forever-environment-injected-memory-poisoning-attacks-on-web-agents-2604.02623]] — Environment-injected memory poisoning (Run 132) — L3 environment-memory-pipeline exploitation
- [[when-routine-chats-turn-toxic-unintended-long-term-state-poisoning-in-personalized-agents-2605.06731]] — Long-term state poisoning (Run 132) — cumulative state contamination in personalized agents
