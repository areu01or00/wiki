---
title: "A specialized reasoning large language model for accelerating rare disease diagnosis: a randomized AI physician assistance trial"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [domain-specific-llm, medical-ai, reasoning, specialized-model, rare-disease]
sources: ["https://arxiv.org/abs/2606.24510"]
---

# A Specialized Reasoning Large Language Model for Accelerating Rare Disease Diagnosis: A Randomized AI Physician Assistance Trial

## Overview
RaDaR (Rare Disease navigatoR) is a 32B open-source specialized reasoning LLM for rare disease diagnosis, trained on 49,170 publicly available free-text cases and 104,666 synthetic cases with reasoning-enhanced training. In a randomized physician-assistance trial, RaDaR assistance improved physicians' rare-disease diagnostic accuracy by 21.44 percentage points compared with internet search alone. This is the first domain-specific specialized reasoning LLM with a randomized clinical trial validation demonstrating diagnostic lead time in rare disease workflows.

## Key Facts
- **Authors**: Chen, Haichao; Zhou, Songchi; Zhao, Zhengyun + 28
- **Year**: 2026
- **arXiv**: [2606.24510](https://arxiv.org/abs/2606.24510)
- **Date**: 2026-06-23

## Key Contributions
- First specialized reasoning LLM (32B) with randomized physician-assistance trial evidence for rare disease diagnosis
- Achieved 21.44 percentage point improvement in physician diagnostic accuracy vs internet search alone
- Prioritized final diagnosis before documented clinical suspicion in 61.06% of retrospective cases (1.87 month lead time)
- Phenotype-anchored narrative synthetic data generation for long-tail rare disease training
- Monotonic scaling trend within tested data range, validating synthetic data curation approach

## Related Papers
- [[test-time-verification-for-text-to-sql-via-outcome-reward-models-2606.30851]] — Outcome reward models for test-time verification in structured reasoning tasks; complements RaDaR's inference-time verification approach to structured medical reasoning
- [[harnessing-generalist-agents-for-contextualized-time-series-2606.05404]] — Generalist agent harness framework for time series; shares the agentic-harness architecture pattern applied in RaDaR's clinical workflow integration
