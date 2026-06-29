---
title: "Learning is Forgetting: LLM Training As Lossy Compression"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [information-geometry, theory-of-llm, rate-distortion]
sources: ["https://arxiv.org/abs/2604.07569"]
---

# Learning is Forgetting: LLM Training As Lossy Compression

## Overview
Frames large language model training through the lens of rate-distortion / Information Bottleneck theory, arguing that "learning is forgetting" — pre-training produces models that retain only information relevant to next-sequence prediction and approaches the Information Bottleneck bound on compression. This establishes LLMs as instances of lossy compression and gives an information-geometric primitive for *what* a model stores versus discards during training.

## Key Facts
- **Authors**: Henry C. Conklin, Tom Hosking, Tan Yi-Chern, Julian Gold, Jonathan D. Cohen, Thomas L. Griffiths, Max Bartolo, Seraphina Goldfarb-Tarrant
- **Year**: 2026
- **arXiv**: [2604.07569](https://arxiv.org/abs/2604.07569)
- **Submission date**: 8 Apr 2026

## Key Contributions
- **Lossy-compression framing of LLM training**: casts the pre-training objective as a rate-distortion / Information Bottleneck optimisation in which the *compression rate* is bounded by the next-sequence prediction objective, and *forgetting* of irrelevant information follows from this bound.
- **Empirical approach to the IB bound during pre-training**: provides a rate-distortion estimator (an extension / application of existing estimators) and shows pre-training drives LLMs toward the Information Bottleneck bound on compression of training data.
- **Information-geometric primitive for "what is remembered"**: replaces gradient/parameter-similarity measures (Functional-Information, Functional-Perturbation) with the *information-theoretic retained signal* as the load-bearing primitive, separating memorised signal from compression artefacts.
- **Information-bottleneck motivation for downstream phenomena**: gives a unified theoretical lens over continual-learning (Attribution-Guided), catastrophic-forgetting (Lottery-Tickets-of-LLM), and reasoning-emergence-phenomena by treating all of them as rate-distortion regimes.
- **Decomposes LLM capacity into signal vs distortion components** — useful for assessing whether benchmark gains come from additional signal or from distorted generalisation, complementing the inference-time *cognitive-load* measures of Run 107.

## Related Papers
- [[between-the-layers-lies-the-truth-uncertainty-estimation-via-intra-layer-local-information-scores-2603.22299]] — Local information-scores as the *intra-layer* analog of the *training-time* lossy-compression primitive here.
- [[a-brain-like-synergistic-core-in-llms-drives-behaviour-and-learning-2601.06851]] — PID decomposition with redundancy ↔ synergy that complements lossy-compression retained-signal.
- [[early-warning-signals-of-grokking-via-loss-landscape-geometry-2602.16967]] — Loss-landscape geometry primitive unifying with rate-distortion framing for the *loss surface* over training.
- [[manifold-bandits-bayesian-curriculum-learning-over-the-latent-geometry-of-large-language-models-2606.19750]] — Latent-geometry curriculum learning that rate-distortion theory predicts is most efficient when IB-bound is approached.
- [[multibreak-a-scalable-and-diverse-multi-turn-jailbreak-benchmark-for-evaluating-llm-safety-2605.01687]] — First IB-motivated normalization / efficiency primitive for LLM protection; complementary.
