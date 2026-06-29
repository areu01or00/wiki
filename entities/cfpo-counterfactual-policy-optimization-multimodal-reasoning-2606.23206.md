---
title: "CFPO: Counterfactual Policy Optimization for Multimodal Reasoning"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reasoning, reinforcement-learning, multimodal, counterfactual, causal]
sources: ["https://arxiv.org/abs/2606.23206"]
---

# CFPO: Counterfactual Policy Optimization for Multimodal Reasoning

## Overview
CFPO (CounterFactual Policy Optimization) is a novel reinforcement learning framework that enforces causal consistency between visual perception and textual reasoning in Large Vision-Language Models (LVLMs). It introduces a cross-modal counterfactual enhancement mechanism that regularizes the policy by maximizing the discrepancy between the model's predictions and those from a counterfactual state where critical visual cues are suppressed.

## Key Facts
- **Authors**: Zhangyuan Yu, Wanran Sun, Guangjing Yang, Xiaohu Wu, Qicheng Lao
- **Year**: 2026
- **arXiv**: [2606.23206](https://arxiv.org/abs/2606.23206)
- **Subjects**: Computer Vision and Pattern Recognition (cs.CV); Computation and Language (cs.CL)
- **Published**: ICML 2026

## Key Contributions
- **Cross-Modal Counterfactual Enhancement**: The core mechanism suppresses critical visual cues and penalizes when the model's predictions don't change — forcing the model to not over-rely on language priors when visual evidence is removed.
- **Grounding Failure Reduction**: Addresses the root cause of LVLM hallucination drift during long CoT reasoning — the tendency to ignore visual evidence in favor of strong language priors.
- **Seamless Integration with Standard RL**: Works with GRPO and DAPO without requiring external reward models or additional supervision.
- **Consistent Gains**: Improves reasoning fidelity with consistent 3.17%-6.25% gains over standard RL baselines and 1.32%-2.13% over the state-of-the-art perception-aware method (PAPO).

## Related Papers
- [[from-prompts-to-tokens-internalizing-causal-supervision-vlm-multi-image-2606.11745]] — BridgeVLM (2606.11745) internalizes causal supervision in VLMs via RAMP layers (sibling counterfactual VLM paper from same discovery batch)
- [[faithfulness-qa-a-counterfactual-entity-substitution-dataset-for-training-context-faithful-rag-models-2604.25313]] — FaithfulnessQA uses counterfactual entity substitution for RAG faithfulness
- [[causal-rcm-a-unified-teacher-forcing-and-self-forcing-open-recipe-for-autoregressive-diffusion-distillation-in-streaming-video-generation-and-interactive-world-models-2606.25473]] — Causal-RCM applies counterfactual reasoning in world models
