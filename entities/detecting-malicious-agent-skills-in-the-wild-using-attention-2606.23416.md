---
title: "Detecting Malicious Agent Skills in the Wild using Attention"
created: "2026-07-01T08:00:00+00:00"
updated: "2026-07-01T08:00:00+00:00"
type: entity
tags: [agent-security, supply-chain, detection]
sources: ["https://arxiv.org/abs/2606.23416"]
---

# Detecting Malicious Agent Skills in the Wild using Attention

## Overview
LLM agents load third-party skills (natural-language instruction packages) that execute with user privileges. A single malicious skill can exfiltrate data, hijack the agent, or persist as a supply-chain attack. This paper uses attention pattern analysis to detect malicious skills at load time.

## Key Facts
- **arXiv**: [2606.23416](https://arxiv.org/abs/2606.23416)
- **Year**: 2026

## Key Contributions
- Identifies skill marketplace supply-chain attack surface for LLM agents
- Uses attention-based detection to identify malicious skill behaviors at load time
- Demonstrates detection across real-world skill marketplaces

## Related Papers
- [[adaptive-evaluation-out-of-band-defenses-against-prompt-injection-in-llm-agents-2606.26479]] — Out-of-band defense frameworks for agentic systems
- [[defending-against-adaptive-prompt-injection-attacks-via-reasoning-enabled-task-alignment-2606.15441]] — Adaptive attack defenses
- [[what-if-prompt-injection-never-left-exploring-cross-session-stored-prompt-injection-in-agentic-systems-2606.04425]] — Cross-session attack persistence
