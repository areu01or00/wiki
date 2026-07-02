---
title: "CALIBER: Calibrating Confidence Before and After Reasoning in Language Models"
created: "2026-07-02"
updated: "2026-07-02"
type: entity
tags: [calibration, reasoning, llm]
sources: ["https://arxiv.org/abs/2606.24281"]
---

# CALIBER: Calibrating Confidence Before and After Reasoning in Language Models

## Overview
CALIBER addresses a key gap in reasoning language models: the inability to produce reliable confidence estimates at multiple stages of reasoning. Existing methods elicit confidence only once — either before thinking or after answering — but CALIBER proposes a unified protocol that elicits and supervises confidence estimates at both states, reducing Expected Calibration Error (ECE) by 52.5% over prior methods. This is the first framework to treat pre-reasoning and post-reasoning confidence as a unified information-state problem.

## Key Facts
- **Authors**: Finlay, Conor; Kurien, Joshua; Dash, Saurabh + 2
- **Year**: 2026
- **arXiv**: [2606.24281](https://arxiv.org/abs/2606.24281)

## Key Contributions
- Unified confidence elicitation protocol spanning pre-reasoning and post-reasoning states
- First method to demonstrate that per-state confidence supervision reduces ECE by 52.5% over single-point calibration methods
- Information-state-aware calibration framework where each reasoning step's confidence is matched to its local evidence state
- Demonstrates that reasoning models can be calibrated without sacrificing reasoning quality — the two objectives are not in tension

## Related Papers
- [[calibrating-the-evaluator-does-probability-calibration-mitigate-preference-coupling-in-llm-agent-feedback-loops-2606.31371]] — Related calibration work on preference coupling in LLM agent feedback loops; CALIBER complements by focusing on reasoning-state confidence estimation
