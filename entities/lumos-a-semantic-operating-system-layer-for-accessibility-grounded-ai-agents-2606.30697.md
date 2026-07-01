---
title: "LUMOS: A Semantic Operating-System Layer for Accessibility-Grounded AI Agents"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent-infrastructure, operating-system, computer-use, accessibility]
sources: ["https://arxiv.org/abs/2606.30697"]
---

# LUMOS: A Semantic Operating-System Layer for Accessibility-Grounded AI Agents

## Overview
LUMOS (Language Model Unified Machine-Readable Operating-System Semantics) proposes a semantic interaction layer between AI agents and operating systems — replacing pixel-based human interfaces with compact, machine-interpretable semantic state, grounded actions, and reliable feedback. The core problem: OS interfaces are designed for human perception (pixels, icons, windows, mouse movement), but AI agents need semantic representations they can reason over reliably.

## Key Facts
- **arXiv**: [2606.30697](https://arxiv.org/abs/2606.30697)
- **Year**: 2026
- **Category**: cs.AI / cs.HC (Human-Computer Interaction)

## Key Contributions
- Semantic OS abstraction layer exposing machine-readable system state (file hierarchies, process tables, network topology) instead of visual screenshots
- Grounded action protocol with reliable feedback loops — actions produce structured state deltas rather than ambiguous visual confirmations
- Token-cost reduction vs screenshot-based agents: 10-100x fewer tokens for equivalent state comprehension tasks
- Accessibility-grounded design: the same semantic layer that helps AI agents also enables accessibility tools for users with visual impairments

## Key Insights
- Current computer-use agents spend 60-80% of tokens interpreting visual output — a fundamental inefficiency given OS already has structured representations of its own state
- The "screenshot" paradigm introduces coordinate uncertainty, visual ambiguity, and latency that structured OS APIs eliminate entirely
- LUMOS treats the OS as a database with a well-defined schema rather than a visual canvas — agents query semantic state directly
- Demonstrates that semantic grounding reduces both hallucinations (wrong pixel interpretation) and action failures (wrong coordinate targets)

## Related Papers
- [[agentvisor-defending-llm-agents-prompt-injection-semantic-virtualization-2604.24118]] — AgentVisor: Semantic privilege separation for LLM agents via OS-style virtualization, framing agent tool calls as system calls
