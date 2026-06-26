---
title: "TARo: Token-level Adaptive Routing for LLM Test-time Alignment"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [test-time-alignment, token-level-routing, reasoning, llm, router]
sources: ["https://arxiv.org/abs/2603.18411"]
---

# TARo: Token-level Adaptive Routing for LLM Test-time Alignment

## Overview

Rai, Arushi; Zhang, Qiang; Zeng, Hanqing; Zhang, Yunkai; Tamboli, Dipesh; Fan, Xiangjun; Zhao, Zhuokai; Zhang, Lizhu observe that existing test-time alignment methods have been explored mainly for preference alignment rather than reasoning, and propose **TARo (Token-level Adaptive Routing)** — a framework that steers a **frozen LLM** toward structured reasoning entirely at inference time. TARo first trains reward models on **step-wise mathematical traces** to capture fine-grained logical-consistency signals, then introduces a **learnable token-level router** that automatically controls when the reward model guides the base model during decoding. The approach improves reasoning by up to **+22.4%** over the base model and **+8.4%** over existing token-level test-time alignment methods, and generalizes from small to large backbones without retraining — extending test-time alignment from preference optimization to robust cross-domain reasoning. The load-bearing primitive is **token-level routing as the alignment-decision unit** (vs Run 45's LBR which used branch-level routing as the compute-decision unit).

## Key Facts

- **Authors**: Rai, Arushi; Zhang, Qiang; Zeng, Hanqing; Zhang, Yunkai; Tamboli, Dipesh; Fan, Xiangjun; Zhao, Zhuokai; Zhang, Lizhu
- **Year**: 2026
- **Date**: 2026-03-19
- **arXiv**: [2603.18411](https://arxiv.org/abs/2603.18411)

## Key Contributions

- Articulates the **reasoning-vs-preference gap in test-time alignment** — prior work focused on preference optimization; TARo bridges to structured-reasoning guidance
- Introduces **token-level adaptive routing** as the alignment-decision unit — finer-grained than sequence-level or branch-level routing, capturing token-by-token reasoning dynamics
- Trains **step-wise reward models on mathematical traces** to capture fine-grained logical-consistency signals (vs trajectory-level or outcome-level rewards common in RLVR)
- Demonstrates **+22.4% over base / +8.4% over token-level baselines** — substantial reasoning gains without retraining the base LLM
- Shows **backbone-scale generalization** without router retraining — small-backbone-trained routers transfer to large backbones
- Surfaces **out-of-distribution generalization** — improves clinical reasoning (MedXpertQA) and instruction following (AlpacaEval) from math-only training, indicating transfer to non-math reasoning domains
- First framework in the wiki that frames **token-level routing as a test-time alignment primitive**, complementing Run 45's LBR (branch-level routing as compute-decision primitive) and the broader test-time scaling literature

## Related Papers

- [[efficient-and-trainable-language-model-test-time-scaling-via-local-branch-routing-2606.25354]] — Run 45 sibling: branch-level routing as test-time compute-decision primitive (different grain: branch vs token)
- [[geometry-of-refusal-linear-instability-safety-aligned-llms-2606.22686]] — mechanistic geometry of safety alignment (Run 39)
- [[ras-measuring-llm-safety-through-refusal-alignment-2606.25750]] — refusal alignment as safety-measurement primitive (Run 42)
- [[privacyalign-contextual-privacy-alignment-for-llm-agents-2606.21710]] — contextual privacy alignment for agents
- [[deeper-is-not-always-better-mitigating-the-alignment-tax-via-confident-layer-decoding-2606.21906]] — alignment tax mitigation
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — long-horizon planning in tool-use agents
- [[verievol-scaling-multimodal-mathematical-reasoning-via-verifiable-evol-instruct-2606.23543]] — verifiable-evolution multimodal math reasoning