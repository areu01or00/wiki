---
title: "Just how sure are you? Improving Verbalized Uncertainty Calibration in LLMs"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [uncertainty-calibration, llm-safety, confidence, verbalized-reasoning]
sources: ["https://arxiv.org/abs/2606.27023"]
---

# Just how sure are you? Improving Verbalized Uncertainty Calibration in LLMs

## Overview
LLMs increasingly verbalize their own uncertainty in deployed applications, yet the relationship between what these models *say* about their confidence and their actual accuracy is poorly understood. This paper empirically investigates the calibration of verbalized uncertainty expressions — do LLMs that say "I'm not sure" actually perform worse? The authors find that existing LLMs systematically miscalibrate verbalized uncertainty, with models often under- or over-confident depending on the domain, and propose targeted prompting and fine-tuning interventions to improve verbalized uncertainty reliability.

## Key Facts
- **Authors**: Senoglu, Eren; Toschi, Federico; Brunello, Nicolo
- **Year**: 2026
- **arXiv**: [2606.27023](https://arxiv.org/abs/2606.27023)
- **Date**: 2026-06-25

## Key Contributions
- First systematic empirical study of verbalized uncertainty calibration across 5 domain categories (medical, legal, factual, mathematical, commonsense)
- Demonstrates that current LLMs produce confidence expressions that do not reliably track actual accuracy — some models are underconfident on easy tasks, others overconfident on hard ones
- Proposes a prompting-based calibration intervention that improves verbalized uncertainty reliability by ~18% without fine-tuning
- Introduces a verbalized calibration metric (V-Cal) distinct from traditional probability-based calibration

## Related Papers
- [[aura-adaptive-uncertainty-aware-refinement-llm-judge-2606.19714]] — Aura also probes adaptive uncertainty-aware refinement, providing complementary uncertainty-handling primitives
- [[calibration-is-not-control-llm-agent-oversight-needs-intervention-2606.21399]] — LLM agent oversight paper that surfaces the intervention gap when overconfident LLMs make consequential decisions
- [[closing-the-reflection-gap-a-free-calibration-bonus-for-agentic-rl-2606.14211]] — Free calibration bonus via reflection mechanism in agentic RL; complementary to verbalized uncertainty findings
- [[between-the-layers-lies-the-truth-uncertainty-estimation-via-intra-layer-local-information-scores-2603.22299]] — Intra-layer uncertainty estimation via local information scores; mechanistic complement to verbalized calibration
