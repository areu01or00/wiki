---
title: "From the Inside Out: Progressive Distribution Refinement for Confidence Calibration"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [confidence-calibration, self-training, distribution-shift, uncertainty]
sources: ["https://arxiv.org/abs/2603.16500"]
---

# From the Inside Out: Progressive Distribution Refinement for Confidence Calibration

## Overview
This paper proposes Progressive Distribution Refinement (PDR), a self-training framework that uses a LLM's own internal representations as the self-reward signal for confidence calibration. The key insight is that the model's internal activation geometry contains exploitable information about its own uncertainty — regions closer to decision boundaries exhibit higher calibration error. PDR progressively aligns confidence distributions with actual error rates through iterative self-improvement, achieving 15-23% ECE reduction without accuracy degradation.

## Key Facts
- **Authors**: Yang, Xizhong; Xia, Yinan; Wang, Huiming + 1
- **Year**: 2026
- **arXiv**: [2603.16500](https://arxiv.org/abs/2603.16500)

## Key Contributions
- Introduced Progressive Distribution Refinement (PDR) — self-training via internal representation geometry as self-reward
- Demonstrated that activation-space distance to decision boundaries predicts calibration error
- Achieved 15-23% ECE reduction across 6 LLM families with no accuracy degradation
- Operates without external validators or held-out calibration data
- Proposes self-supervised calibration signal from model's own internal geometry

## Related Papers
- [[a-systematic-evaluation-of-black-box-uncertainty-estimation-methods-for-large-language-models-2606.19868]] — Black-box uncertainty estimation for LLMs
- [[calibrating-the-evaluator-does-probability-calibration-mitigate-preference-coupling-in-llm-agent-feedback-loops-2606.31371]] — Probability calibration in agent feedback loops
- [[certainty-robustness-evaluating-llm-stability-under-self-challenging-prompts-2603.03330]] — LLM stability under self-challenging prompts
