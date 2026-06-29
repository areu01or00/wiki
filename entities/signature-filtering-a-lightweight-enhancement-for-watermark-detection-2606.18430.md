---
title: "Signature Filtering: A Lightweight Enhancement for Watermark Detection"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [watermarking, llm-detection, signature-filtering, statistical-watermark, robustness]
sources: ["https://arxiv.org/abs/2606.18430"]
---

# Signature Filtering: A Lightweight Enhancement for Watermark Detection

## Overview
First paper in the wiki to introduce *signature filtering* — a detection-time module that learns a small set of "signature" tokens whose presence makes watermark tests unreliable, then removes those tokens before detection — yielding a *plug-in robustness layer* for existing statistical LLM watermarks (Kgw, Sweet, Unigram, Exp) without modifying watermark embedding or text generation. By solving a mixed-integer linear program on a small training set with constraints that maximize the true-positive rate under finite-sample and asymptotic bounds (color-blind, color-adaptive, distributionally correlated attacker models), the work exposes *detection-time pre-filtering as a structurally correct robustness primitive* for statistical LLM watermarks when texts are repetitive, watermarks are weak, or attacks dilute/drop/substitute tokens.

## Key Facts
- **Authors**: not extracted in this run
- **Year**: 2026
- **arXiv**: [2606.18430](https://arxiv.org/abs/2606.18430)
- **Submission date**: 2026-06-16
- **Online date**: 2026-06-24

## Key Contributions
- **Signature filtering as detection-time pre-processing primitive**: rather than redesigning the watermark, *filter* the small set of "signature" tokens (those most likely to be attacked) before applying the watermark detector, raising weak-signal detection rates from 8-31% to 78-99% without altering the embedding scheme.
- **Mixed-integer linear program for signature-set selection**: signatures are computed on a small training set with constraints that maximize true-positive rate, producing a tractable 2-gram and 3-gram signature set applicable across diverse LLMs (OPT-1.3b, OPT-6.7b, Llama2-13b, Llama3.1-8b, Qwen2.5-14b, Phi-3-medium-14b) and benchmark corpora (C4, MBPP, HumanEval, Code-Search-Net).
- **Finite-sample and asymptotic bounds under three attacker models**: color-blind, color-adaptive, and distributionally correlated attackers are each given finite-sample and asymptotic detection guarantees, formalizing *which signature-filtering scheme is robust to which threat model* as a primitive.
- **Stress-test robustness under dilution/deletion/substitution**: 2-gram filters for Kgw-style watermarks preserve clean-text detection gains under 25-50% token perturbation (scrambled sentences, dilution, deletions, substitutions), often matching or outperforming the advanced WinMax watermark — surfacing *signature-filtering as a deployable lightweight hardening layer* on top of standard statistical watermarks.

## Related Papers
- [[acthook-watermarking-llm-agent-trajectories-2602.18700]] — Sibling discovery from same run that surfaces the *agent-trajectory* side of watermarking; ActHook embeds hook actions triggered by secret input keys in agent trajectories while signature filtering hardens *text-output* watermark detection via signature-token removal.
- [[forgetmark-stealthy-fingerprint-embedding-via-targeted-unlearning-2601.08189]] — Sibling discovery from same run that surfaces the *model-fingerprinting* side of provenance detection; ForgetMark uses targeted unlearning with LoRA adapters to embed model-instance fingerprints while signature filtering operates at the *detector-output* layer for watermark text.