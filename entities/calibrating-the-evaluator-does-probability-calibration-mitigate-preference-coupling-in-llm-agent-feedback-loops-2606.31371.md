---
title: "Calibrating the Evaluator: Does Probability Calibration Mitigate Preference Coupling in LLM Agent Feedback Loops?"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [calibration, agent-feedback, preference-learning, rlhf]
sources: ["https://arxiv.org/abs/2606.31371"]
---

# Calibrating the Evaluator: Does Probability Calibration Mitigate Preference Coupling in LLM Agent Feedback Loops?

## Overview
When LLM agents adapt through evaluator feedback, systematic evaluator biases couple into the agent's learned strategy distribution — a phenomenon Liu, Zewen call preference coupling. This paper asks whether probability calibration of the evaluator can break this coupling, and finds that naive calibration is insufficient: calibrated evaluators still impose their internal preference structure on agents, but in harder-to-detect ways because the calibrated confidence scores mask the bias. The paper identifies representational alignment (evaluator representations matching agent representations) as the necessary condition, not just calibration of output probabilities.

## Key Facts
- **Authors**: Liu, Zewen
- **Year**: 2026
- **arXiv**: [2606.31371](https://arxiv.org/abs/2606.31371)

## Key Contributions
- **Preference coupling in agent feedback loops**: Documents that when LLM agents learn from evaluator feedback, the evaluator's internal preference structure propagates into the agent's behavioral distribution — agents don't just improve task performance, they become more like the evaluator that rated them
- **Naive calibration is insufficient**: Shows that applying standard probability calibration to the evaluator's ratings does not break preference coupling; agents still drift toward the evaluator's latent preferences even when confidence scores are well-calibrated
- **Representational alignment as the fix**: Proposes that evaluator-agent representational alignment (shared embedding space structure) is what actually breaks coupling, not calibration at the output probability level
- **Agent feedback loop taxonomy**: Provides a taxonomy of coupling modes (direct preference copying, style convergence, assumption incorporation) with different detectability profiles

## Related Papers
- [[closing-the-reflection-gap-a-free-calibration-bonus-for-agentic-rl-2606.14211]] — Shares the calibration/agentic-RL theme; provides the free-calibration-bonus mechanism complementary to this paper's finding that calibration alone is insufficient
- [[calibration-collapse-under-sycophancy-fine-tuning-reward-hacking-2604.10585]] — Documents calibration collapse under fine-tuning, providing the mechanism (reward hacking) that drives the coupling effect this paper analyzes
- [[calibration-is-not-control-llm-agent-oversight-needs-intervention-2606.21399]] — LLM agent oversight via calibrated verifier; this paper complicates that picture by showing calibrated verifiers still impose preference structure
- [[calvert-augmenting-agents-with-calibrated-verifier-telemetry-improves-action-and-learning-in-knowledge-intensive-tasks-2606.21777]] — Empirical evidence that calibrated verifier telemetry improves agent learning; this paper provides the theoretical boundary on when calibration helps versus when representational alignment is needed
