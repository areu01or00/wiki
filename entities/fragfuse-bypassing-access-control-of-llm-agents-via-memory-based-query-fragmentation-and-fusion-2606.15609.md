---
title: "FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [adversarial-attack, access-control, memory-attack, llm-agent-security]
sources: ["https://arxiv.org/abs/2606.15609"]
---

# FragFuse: Bypassing Access Control of Large Language Model Agents via Memory-Based Query Fragmentation and Fusion

## Overview
FragFuse reveals a novel attack surface arising from LLM agent memory operations: prohibited content that would trigger access control can be fragmented across interactions, stored in long-term memory in benign-appearing fragments, and then reassembled via query fusion to bypass access control mechanisms. This attack is orthogonal to prompt injection (which targets external data) and backdoors (which corrupt model weights) — it exploits the memory subsystem itself as the attack vector.

## Key Facts
- **Authors**: Rao, Zixin
- **Year**: 2026
- **arXiv**: [2606.15609](https://arxiv.org/abs/2606.15609)
- **Discovered**: 2026-06-29

## Key Contributions
- Identifies memory-based query fragmentation and fusion as a novel LLM agent attack vector
- Demonstrates that benign-looking memory fragments can be reassembled to bypass access control
- First attack surface that exploits the memory subsystem (rather than prompts or weights) as the vector
- Proposes query fusion techniques that circumvent existing access-control mechanisms for LLM agents

## Related Papers
- [[what-if-prompt-injection-never-left-exploring-cross-session-stored-prompt-injection-in-agentic-systems-2606.04425]] — Cross-session stored prompt injection: attacks that persist injected content across sessions; FragFuse differs by fragmenting prohibited content rather than injecting full malicious prompts
- [[governance-decay-how-context-compaction-silently-erases-safety-constraints-in-long-horizon-llm-agents-2606.22528]] — Governance Decay: context compaction silently removes in-context constraints; FragFuse differs by attacking memory fragmentation rather than context compaction
