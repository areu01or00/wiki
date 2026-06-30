---
title: "Think Twice Before You Act: Protecting LLM Agents Against Tool Description Poisoning via Isolated Planning"
created: "2026-07-01T08:00:00+00:00"
updated: "2026-07-01T08:00:00+00:00"
type: entity
tags: [agent-security, adversarial, tool-use]
sources: ["https://arxiv.org/abs/2606.20922"]
---

# Think Twice Before You Act: Protecting LLM Agents Against Tool Description Poisoning via Isolated Planning

## Overview
Cross-tool description poisoning manipulates planner-visible tool metadata to steer LLM agents toward harmful actions. This paper proposes isolated planning as a defense: separating tool metadata review from planning computation so poisoned descriptions cannot influence action selection.

## Key Facts
- **arXiv**: [2606.20922](https://arxiv.org/abs/2606.20922)
- **Year**: 2026

## Key Contributions
- Identifies cross-tool description poisoning as a novel attack surface beyond prompt injection
- Proposes isolated planning architecture separating tool metadata review from planning
- Demonstrates attack success rate and defense effectiveness across multiple LLM agent frameworks

## Related Papers
- [[what-if-prompt-injection-never-left-exploring-cross-session-stored-prompt-injection-in-agentic-systems-2606.04425]] — Cross-session prompt injection taxonomy (prior work)
- [[defending-against-adaptive-prompt-injection-attacks-via-reasoning-enabled-task-alignment-2606.15441]] — Adaptive prompt injection defenses
- [[adaptive-evaluation-out-of-band-defenses-against-prompt-injection-in-llm-agents-2606.26479]] — Out-of-band prompt injection defenses
