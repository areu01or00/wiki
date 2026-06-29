---
title: "What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [security, agent-memory, prompt-injection]
sources: ["https://arxiv.org/abs/2606.04425"]
---

# What If Prompt Injection Never Left? Exploring Cross-Session Stored Prompt Injection in Agentic Systems

## Overview
Modern agentic systems transform LLMs from session-bounded assistants into stateful systems that persist and evolve shared world state across sessions through memories, filesystems, and long-lived contextual artifacts. Inspired by stored cross-site scripting in web systems, this paper introduces **cross-session stored prompt injection**: a successful injection persists within agentic system state and silently influences future executions long after the original attacker interaction has ended. The paper develops a formal taxonomy and benchmark for studying how adversarial content persists and affects agentic systems across sessions.

## Key Facts
- **Authors**: Yuanbo Xie, Tianyun Liu, Yingjie Zhang, Suchen Liu, Yulin Li, Liya Su, Tingwen Liu
- **Year**: 2026
- **arXiv**: [2606.04425](https://arxiv.org/abs/2606.04425)
- **Subjects**: Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI)

## Key Contributions
- Introduces **cross-session stored prompt injection**: prompt injection as a persistent, long-lived system-level vulnerability (not just session-level)
- Develops a **taxonomy** of how adversarial content persists across sessions in agentic system state
- Creates a **benchmark and sandbox toolkit** for quantitative analysis across models, attack goals, and persistence channels
- Shows that persistence transforms prompt injection from an ephemeral model-level threat into a system-level vulnerability embedded in agent execution state
- Frames the core insight: agent state is a **shared, evolving attack surface** that outlives the original injection event

## Related Papers
- [[the-defense-trilemma-why-prompt-injection-defense-wrappers-fail-2604.06436]] — Analyzes why prompt injection defense wrappers fail; directly relevant to the attack surface this paper identifies
- [[plans-dont-persist-why-context-management-is-load-bearing-for-llm-agents-2606.22953]] — Documents context management as a load-bearing concern for LLM agents; complements the cross-session persistence analysis
- [[silent-failure-in-llm-agent-systems-the-entropy-principle-2606.08162]] — Characterizes silent failure modes in LLM agent systems; cross-session persistence is a form of silent, delayed failure
