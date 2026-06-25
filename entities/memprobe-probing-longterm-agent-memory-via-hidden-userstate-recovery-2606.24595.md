---
title: "MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [llm, agents, memory, evaluation, benchmark]
sources: ["https://arxiv.org/abs/2606.24595"]
---

# MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery

## Overview
Long-term memory promises LLM agents that grow more capable across sessions, maintaining an accurate, evolving understanding of the user that interaction forms. In practice, however, this memory is evaluated mostly through downstream behavior, such as later answers, personalization quality, or task success, which is a weak and indirect signal of whether memory itself is correct. MEMPROBE introduces a probe-style benchmark that targets the hidden user-state directly: can the agent recover facts about the user (preferences, demographics, identity, recurring context) that were disclosed early in a long, noisy conversation, and crucially, can it distinguish facts that were actually stated from plausible-but-never-mentioned ones, without false-confabulation on the negatives. The benchmark operationalizes long-term memory as a *state-recovery* problem and provides a contamination-resistant evaluation protocol that current agentic-memory systems consistently fail.

## Key Facts
- **Authors**: Ma, Enze; Zhou, Yufan; Huang, Wei-Chieh; Yang, Jie; Ma, Huanhuan; Wang, Zixuan; Li, Chengze; Miao, Chunyu; Yu, Philip S.
- **Year**: 2026
- **arXiv**: [2606.24595](https://arxiv.org/abs/2606.24595)
- **Subjects**: cs.CL

## Key Contributions
- Reframes long-term agent memory evaluation from downstream behavior to a direct user-state-recovery probe, exposing a class of failure (confabulated-but-plausible memories) that downstream metrics miss.
- Releases a benchmark with positive/negative fact pairs derived from long, noisy multi-session interactions, with explicit distractors designed to test discrimination between said-vs-not-said user attributes.
- Demonstrates that current long-term-memory agent stacks (retrieval-augmented memory, summarization-based memory, structured-profile memory) substantially underperform a no-memory baseline on the *negative* subset, indicating they confabulate.
- Provides a contamination-resistant protocol (held-out user profiles, time-shifted evaluation) that prevents training-set leakage from inflating scores.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain; discovered via emergent-concept search on the agent-memory axis
- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — Companion: argues that agent memory should be a first-class data-management system; MEMPROBE provides the evaluation substrate that system needs
- [[self-compacting-language-model-agents-2606.23525]] — Companion: inference-time trace compaction at the agent loop; MEMPROBE evaluates the memory persistence layer below that loop
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — Companion: evolvable context-dependent embeddings for agentic memory; MEMPROBE provides the probe that tests whether such embeddings actually store the right state