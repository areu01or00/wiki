---
title: "From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [uncertainty-estimation, llm-safety, interpretability, hallucination-detection]
sources: ["https://arxiv.org/abs/2606.27679"]
---

# From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models

## Overview
Probe-based uncertainty estimation (UE) has emerged as a prominent approach to detect hallucinations in LLMs by learning uncertainty from internal model signals. This paper provides the first factorised study under matched conditions, isolating the contribution of feature design, training data construction, and evaluation setting. The key finding is that raw hidden states and attention features are difficult to outperform in-domain, but under distribution shift, structured and compressed features are more robust.

## Key Facts
- **Authors**: Ponhvoan Srey, Xiaobao Wu, Cong-Duy Nguyen, Quang Minh Nguyen, Duc Anh Vu, Anh Tuan Luu
- **Year**: 2026
- **arXiv**: [2606.27679](https://arxiv.org/abs/2606.27679)
- **Subjects**: Computation and Language (cs.CL); Artificial Intelligence (cs.AI)

## Key Contributions
- First factorised ablation of probe-based UE methods under matched conditions (feature design × training data × evaluation setting)
- Demonstrates that raw hidden states and attention features are near-optimal in-domain but degrade under distribution shift
- Structured and compressed features (e.g., PCA-projected states) transfer better across distribution shifts
- Prompting strategy and label construction significantly affect probe behaviour
- Benchmark-based pretrained probes serve as stable off-the-shelf baseline for open-ended factual generation

## Related Papers
- [[emergent-concepts]] — Parent meta-page for emergent-concept discoveries
- [[mindgames-a-live-arena-for-evaluating-social-and-strategic-reasoning-in-multi-agent-llms-2605.29512]] — MINDGAMES: Live arena for ToM evaluation (orthogonal: probe-based uncertainty vs. behavioral ToM evaluation)
- [[osctom-rl-guided-adversarial-generation-for-high-order-theory-of-mind-2605.20423]] — OSCToM: Adversarial ToM generation (orthogonal: uncertainty estimation vs. adversarial belief conflict generation)
