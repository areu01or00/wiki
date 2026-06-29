---
title: "ForgetMark: Stealthy Fingerprint Embedding via Targeted Unlearning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [watermarking, model-fingerprinting, targeted-unlearning, lora, provenance-detection]
sources: ["https://arxiv.org/abs/2601.08189"]
---

# ForgetMark: Stealthy Fingerprint Embedding via Targeted Unlearning

## Overview
First paper in the wiki to introduce a *stealthy LLM fingerprinting framework* that encodes model-instance provenance via targeted unlearning rather than backdoor triggers — building a compact, human-readable key-value set with an assistant model and predictive-entropy ranking, then training lightweight LoRA adapters to *suppress* the original values on their keys while preserving general capabilities. By relying on probabilistic forgetting traces rather than fixed trigger-response patterns, ForgetMark avoids high-perplexity triggers, reduces heuristic-detector exposure, and lowers false triggers, achieving 100% ownership verification on fingerprinted models across diverse architectures while surpassing backdoor baselines in stealthiness and robustness to model merging and moderate incremental fine-tuning.

## Key Facts
- **Authors**: not extracted in this run
- **Year**: 2026
- **arXiv**: [2601.08189](https://arxiv.org/abs/2601.08189)
- **Submission date**: 2026-01-13
- **Online date**: 2026-01-20

## Key Contributions
- **Targeted-unlearning fingerprinting as a structurally-correct provenance primitive**: existing invasive backdoor fingerprints suffer from high-perplexity triggers easily filtered by perplexity tests, fixed response patterns exposed by heuristic detectors, and spurious activations on benign inputs; ForgetMark sidesteps all three by encoding provenance via *forgetting traces* — lightweight LoRA adapters trained to suppress specific value tokens on specific key prompts — making the fingerprint structurally hard to detect because the model simply does not generate the value any more, rather than producing an anomalous trigger.
- **Predictive-entropy-ranked key-value set construction**: an assistant model and predictive-entropy ranking are used to build a *compact, human-readable key-value set* (rather than opaque trigger strings), preserving interpretability of the fingerprint while minimizing overlap with natural distributions.
- **Black/gray-box ownership verification via likelihood + semantic aggregation**: ownership is verified by aggregating *likelihood evidence* (the model is less likely to generate the value under the key) and *semantic evidence* (semantic similarity between generated and original value degrades on key prompts) into a fingerprint success rate, robust under black-box access (only log-probabilities / outputs observable) and gray-box access (intermediate likelihoods observable).
- **100% ownership verification with stealth + robustness to model merging**: ForgetMark achieves 100% ownership verification on fingerprinted models while surpassing backdoor baselines in stealthiness and robustness to model merging and moderate incremental fine-tuning — surfacing *probabilistic-forgetting-traces as the load-bearing provenance primitive* when backdoor-style triggers are too easy to filter, and when downstream model-merging or fine-tuning might collapse fixed response patterns.

## Related Papers
- [[signature-filtering-a-lightweight-enhancement-for-watermark-detection-2606.18430]] — Sibling discovery from same run that surfaces the *watermark-detection-hardening* side of provenance protection; signature filtering operates at the *detector* layer to remove tokens that defeat watermark tests, while ForgetMark operates at the *model* layer to embed fingerprints via targeted unlearning.
- [[acthook-watermarking-llm-agent-trajectories-2602.18700]] — Sibling discovery from same run that surfaces the *agent-trajectory* side of watermarking; ActHook embeds hook actions in agent trajectories triggered by secret input keys while ForgetMark uses unlearning-driven likelihood suppression as the load-bearing fingerprint primitive.