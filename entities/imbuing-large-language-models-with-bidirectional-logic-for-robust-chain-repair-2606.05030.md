---
title: "Imbuing Large Language Models with Bidirectional Logic for Robust Chain Repair"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [reasoning, llm, chain-of-thought, fine-tuning]
sources: ["https://arxiv.org/abs/2606.05030"]
---

# Imbuing Large Language Models with Bidirectional Logic for Robust Chain Repair

## Overview
Autoregressive CoT reasoning is unidirectional — each step only conditions on prior tokens, causing error snowballing when a single mistake corrupts the entire chain. TRI (Teleological Reasoning Infilling) introduces goal-conditioned bridging as a fill-in-the-middle task, enabling surgical repair of corrupted reasoning segments without regenerating the full trace.

## Key Facts
- **Authors**: (from arxiv 2606.05030)
- **Year**: 2026
- **arXiv**: [2606.05030](https://arxiv.org/abs/2606.05030)

## Key Contributions
- Prefix-Suffix-Middle (PSM) sequence rearrangement with three sentinel tokens enabling bidirectional attention in decoder-only transformers
- Two-stage training: SFT on formally verified (P, S, M) triples + DPO with symbolic Lean 4 / Python verifier as sole reward oracle
- Dual-system inference loop: causal draft model generates trace → verifier pinpoints failures → TRI infills only the damaged segment
- 31.2% token reduction per problem at state-of-the-art performance across three benchmarks

## Related Papers
- [[agentic-chain-of-thought-steering-for-efficient-and-controllable-llm-reasoning-2606.03965]] — Agentic CoT steering for efficient reasoning control
- [[a-verifiable-search-is-not-a-learnable-chain-of-thought-2606.21884]] — Verification vs CoT learnability
