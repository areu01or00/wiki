---
title: "Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [safety, agent, prompt-injection, defense]
sources: ["https://arxiv.org/abs/2606.26479"]
---

# Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injection in LLM Agents

## Overview
Recent work (2024 to 2026) has converged on a strategy for defending tool-using LLM agents against indirect prompt injection: rather than training the model to refuse malicious instructions, enforce security outside the model with a deterministic policy that mediates the agent's actions. Systems such as CaMeL, FIDES, Progent, RTBAS, and FORGE realize this with capabilities, information-flow labels, and reference monitors. This paper organizes these out-of-band defenses and evaluates their effectiveness on the AgentDojo benchmark.

## Key Facts
- **Authors**: Praneeth Narisetty, Shiva Nagendra Babu Kore, Uday Kumar Reddy Kattamanchi, Jayaram Kumarapu
- **Year**: 2026
- **arXiv**: [2606.26479](https://arxiv.org/abs/2606.26479)
- **Date**: 25 Jun 2026 (submitted)

## Key Contributions
- **Out-of-band defense taxonomy**: organizes existing out-of-band defense systems (CaMeL, FIDES, Progent, RTBAS, FORGE) as instances of deterministic policy enforcement outside the model
- **AgentDojo benchmark evaluation**: systematic evaluation of out-of-band defenses against indirect prompt injection attacks on tool-using LLM agents
- **Near-elimination claims reassessed**: several systems report near-elimination of attacks on AgentDojo; this paper provides independent replication and identifies where defenses still fail
- **Defense gap characterization**: identifies specific attack classes (planning validity, behavioral change, security intent) that out-of-band defenses do not fully capture

## Related Papers
- [[governance-decay-how-context-compaction-silently-erases-safety-constraints-in-long-horizon-llm-agents-2606.22528]] — Context compaction as a TOCTOU failure mode for agent safety constraints (complementary: Governance Decay focuses on compaction removing constraints; this paper focuses on out-of-band enforcement gaps)
- [[the-defense-trilemma-why-prompt-injection-defense-wrappers-fail-2604.06436]] — Earlier analysis of why wrapper-based prompt injection defenses fail
- [[defending-against-adaptive-prompt-injection-attacks-via-reasoning-enabled-task-alignment-2606.15441]] — Reasoning-enabled task alignment as an alternative defense approach
