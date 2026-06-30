---
title: "CaliDist: Calibrating Large Language Models via Behavioral Robustness to Distraction"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [calibration, llm-evaluation, robustness]
sources: ["https://arxiv.org/abs/2606.05799"]
---

# CaliDist: Calibrating Large Language Models via Behavioral Robustness to Distraction

## Overview
CaliDist identifies that standard LLM calibration methods ignore a critical dimension: **behavioral robustness to distraction** — a model's confidence should reflect its stability when faced with irrelevant or misleading information. The paper introduces a post-hoc calibration method that evaluates how well a model's confidence tracks its performance under cognitively distracting contexts.

## Key Facts
- **Authors**: [arXiv](https://arxiv.org/abs/2606.05799)
- **Year**: 2026
- **arXiv**: [2606.05799](https://arxiv.org/abs/2606.05799)

## Key Contributions
- Identifies **behavioral robustness to distraction** as an underexplored calibration axis — standard calibration curves are measured in clean conditions, but real-world inputs often contain misleading context
- Introduces **CaliDist**: a post-hoc calibration method that adjusts confidence scores based on a model's stability under semantically similar but distracting inputs
- Demonstrates that models with high standard calibration scores can still be poorly calibrated under distraction (confidence stays high even when distracted by irrelevant context)
- Shows that CaliDist calibration generalizes across distribution shifts better than temperature scaling or Platt scaling
- Applies to QA, summarization, and mathematical reasoning tasks

## Related Papers
- [[uncertainty-calibration-benchmarking-llm-long-form-qa-2602.00279]] — Long-form QA calibration benchmarking; CaliDist extends calibration evaluation to the behavioral robustness dimension
- [[calibration-collapse-under-sycophancy-fine-tuning-reward-hacking-2604.10585]] — Calibration collapse under fine-tuning; shares the theme of confidence failing to track actual capability under distributional change
- [[calibration-is-not-control-llm-agent-oversight-needs-intervention-2606.21399]] — Agent oversight calibration; related by the calibration-for-agents theme, distinct axis (intervention vs distraction robustness)
