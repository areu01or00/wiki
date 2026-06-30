---
title: "What the LLM Should Not Say: Boundary-Aware Context Grounding for A Seven-Channel EEG Agent"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [agentic-ai, llm-orchestration, scientific-llm]
sources: ["https://arxiv.org/abs/2606.26519"]
---

# What the LLM Should Not Say: Boundary-Aware Context Grounding for A Seven-Channel EEG Agent

## Overview
Large language models can make scientific software easier to use, but a general model does not automatically know which measurements a particular sensor can support, which algorithms are implemented, or which conclusions are justified by a computed result. These distinctions are especially important for low-channel EEG, where sparse spatial coverage makes plausible but unsupported interpretations easy to produce. We present NeuraDock Agent, an open-source architecture that separates a deterministic local EEG engine from a hardware-aware language layer. The LLM receives only a compact, allowlisted summary and a versioned context pack describing the seven-channel hardware, reviewed workflows, result fields, implementation boundaries, and scientific limits. Raw EEG and dense per-sample arrays remain local. Evaluated at three levels: (1) 12 recordings produced identical structured results over ten repetitions; (2) request-capture and failure-injection confirmed data boundary and artifact preservation under HTTP, malformed-output, and connection failures; (3) boundary-awareness benchmark tested 36 ordinary and adversarial questions under four context ablations and two LLMs, yielding 288 results supporting hardware-aware grounding as a practical mechanism for calibrating what an EEG agent accepts, qualifies, or refuses.

## Key Facts
- **arXiv**: [2606.26519](https://arxiv.org/abs/2606.26519)

## Key Contributions
-

## Related Papers
- [[emergent-concepts]] — Parent chain that led to this discovery
