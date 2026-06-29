---
title: "State Contamination in Memory-Augmented LLM Agents"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [safety, agent-memory, multi-agent]
sources: ["https://arxiv.org/abs/2605.16746"]
---

# State Contamination in Memory-Augmented LLM Agents

## Overview
LLM agents increasingly rely on persistent state (transcripts, summaries, memory buffers) to support long-horizon interaction. This creates a failure mode the paper calls **memory laundering**: toxic or adversarial context can be compressed into memory summaries that no longer appear toxic under standard detectors, yet still preserve hostile framing or conflict structure that influences future generations. Using paired counterfactual multi-agent rollouts, the paper introduces **sub-threshold propagation gap (SPG)** to quantify hidden downstream behavioral differences from memory states a deployed monitor would classify as safe.

## Key Facts
- **Authors**: Yian Wang, Agam Goyal, Yuen Chen, Hari Sundaram
- **Year**: 2026
- **arXiv**: [2605.16746](https://arxiv.org/abs/2605.16746)
- **Subjects**: Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

## Key Contributions
- Formalizes **memory laundering** as a distinct failure mode: toxic context compressed into safe-seeming memory summaries
- Introduces **sub-threshold propagation gap (SPG)**: quantifies downstream behavioral differences from sub-threshold memory states
- Shows toxicity propagates through distinct state channels: raw transcript reuse drives overt toxicity; compressed memory carries hidden sub-threshold influence
- Demonstrates that sanitization must happen **before** summarization — cleaning completed summaries leaves laundered influence intact
- Frames safety in memory-augmented agents as a **state-control problem** over evolving context

## Related Papers
- [[supersede-diagnosing-and-training-the-memory-update-gap-2606.27472]] — Diagnoses the memory update gap mechanism; complementary to State Contamination's analysis of what gets stored and how it propagates
- [[trustmem-trustworthy-memory-consolidation-llm-agents-long-term-memory-2606.25161]] — Memory consolidation framework; directly relevant to the trust problem when memory summaries carry hidden influence
- [[the-defense-trilemma-why-prompt-injection-defense-wrappers-fail-2604.06436]] — Prompt injection defense analysis; related to the threat model of adversarial content persisting in agent state
