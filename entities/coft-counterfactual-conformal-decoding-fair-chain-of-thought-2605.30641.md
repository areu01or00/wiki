---
title: "COFT: Counterfactual-Conformal Decoding for Fair Chain-of-Thought Reasoning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, chain-of-thought, bias, causal-reasoning, fairness]
sources: ["https://arxiv.org/abs/2605.30641"]
---

# COFT: Counterfactual-Conformal Decoding for Fair Chain-of-Thought Reasoning in Large Language Models

## Overview
COFT (Chain of Fair Thought) is a training-free decoding method that applies token-level fairness control at decode time to reduce societal biases that LLMs reveal and amplify during chain-of-thought generation. It creates masked counterfactual prompts (replacing sensitive spans with neutral tokens), compares factual and masked logit distributions through lightweight logit fusion, and uses dual-branch split-conformal calibration to certify per-step candidate token sets at a user-chosen risk level.

## Key Facts
- **Authors**: Arya Fayyazi, Mehdi Kamal, Massoud Pedram
- **Year**: 2026
- **arXiv**: [2605.30641](https://arxiv.org/abs/2605.30641)
- **Subjects**: Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
- **Published**: ICML 2026

## Key Contributions
- **Training-Free Bias Reduction**: Achieves 30-55% (median 38%) reduction in bias metrics without retraining, auxiliary classifiers, or weight access.
- **Counterfactual Masking at Decode Time**: Replaces sensitive spans with neutral tokens at decoding time and compares logit distributions to attenuate attribute-driven biases — a causal intervention at the decoding stage.
- **Distribution-Free Validity Guarantees**: Provides marginal validity guarantees under exchangeability for any frozen causal language model via conformal prediction theory.
- **Per-Step Conformal Calibration**: Uses dual-branch split-conformal calibration to certify per-step candidate token sets at a user-chosen risk level, making CoT bias auditable.
- **Preserves Task Utility**: Reasoning accuracies remain unchanged within run-to-run noise margins; computational overhead is modest (one additional cached forward pass, ≤11%).

## Related Papers
- [[local-causal-attribution-of-chain-of-thought-reasoning-2606.21821]] — Local Causal Attribution of CoT (Run 120) probes which reasoning steps matter via counterfactual importance
- [[pragrest-self-reinforcing-counterfactual-reasoning-for-pragmatic-language-understanding-2606.18624]] — PragReST (Run 122) uses counterfactual traces for pragmatic inference
- [[causal-methods-for-llm-development-and-evaluation-2605.25998]] — Causal Methods for LLM Eval surveys causal frameworks for LLM evaluation
