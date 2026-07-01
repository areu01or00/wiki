---
title: "Latent Confidence Alignment for LLM Self-Assessment"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [llm-calibration, metacognition, self-assessment, uncertainty-quantification]
sources: ["https://arxiv.org/abs/2606.21937"]
---

# Latent Confidence Alignment for LLM Self-Assessment

## Overview
Latent Confidence Alignment (LCA) addresses a fundamental gap in LLM confidence calibration: existing approaches compare predicted confidence against observed accuracy but fail to model item difficulty, making it impossible to distinguish genuine self-assessment from response-generation artifacts. The paper frames LLM confidence as a latent variable conditioned on both model beliefs and item difficulty, enabling calibration methods that account for what the model actually knows versus what it coincidentally generates.

## Key Facts
- **arXiv**: [2606.21937](https://arxiv.org/abs/2606.21937)
- **Year**: 2026

## Key Contributions
- Proposes latent-variable confidence modeling separating item difficulty from model belief
- Demonstrates that naive confidence-accuracy correlation masks spurious calibration in LLM responses
- Introduces alignment methods conditioning on latent difficulty estimates derived from model internals

## Related Papers
- [[calibration-collapse-under-sycophancy-fine-tuning-reward-hacking-2604.10585]] — Calibration collapse under reward hacking and sycophancy
- [[calibration-is-not-control-llm-agent-oversight-needs-intervention-2606.21399]] — LLM agent oversight and the limits of calibration as control
- [[position-uncertainty-quantification-in-llms-is-just-unsupervised-clustering-2605.19220]] — Foundational critique of mainstream LLM UQ methods
- [[textual-bayes-quantifying-prompt-uncertainty-in-llm-based-systems-2506.10060]] — Bayesian framing of prompt-level uncertainty in LLM systems
