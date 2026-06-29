---
title: "Jailbreaking LLMs & VLMs: Mechanisms, Evaluation, and Unified Defense"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [adversarial-ai, jailbreak, red-teaming]
sources: ["https://arxiv.org/abs/2601.03594"]
---

# Jailbreaking LLMs & VLMs: Mechanisms, Evaluation, and Unified Defense

## Overview
This paper provides a systematic survey of jailbreak attacks and defenses on LLMs and VLMs, emphasizing that jailbreak vulnerabilities stem from structural factors: incomplete training data, linguistic ambiguity, and generative uncertainty. It proposes a three-dimensional framework covering attack vectors (template/encoding-based, ICL manipulation, RL/adversarial learning, LLM-assisted, fine-tuned, and multimodal perturbations), defense mechanisms (prompt obfuscation, output evaluation, model alignment), and evaluation metrics (ASR, toxicity, query/time cost, Clean Accuracy). The survey spans text-only to multimodal settings and proposes unified defense principles: variant-consistency and gradient-sensitivity detection at the perception layer, safety-aware decoding at the generation layer, and adversarially augmented preference alignment at the parameter layer.

## Key Facts
- **arXiv**: [2601.03594](https://arxiv.org/abs/2601.03594)
- **Online Date**: 2026-01-07
- **Theme**: jailbreak-survey-vlm-vulnerability-unified-defense

## Key Contributions
-

## Related Papers
- [[risk-under-pressure-compute-aware-evaluation-adversarial-robustness-2606.11409]] — Compute-aware adversarial robustness evaluation from Run 128 Rule 85 sibling
- [[disentangling-adversarial-prompts-semantic-graph-defense-2605.27823]] — Semantic graph prompt disentanglement defense from Run 128 Rule 85 sibling
- [[cross-generational-transfer-adversarial-attacks-reveals-non-monotonic-safety-2606.00813]] — Non-monotonic cross-generational alignment transfer from Run 128 Rule 85 sibling
