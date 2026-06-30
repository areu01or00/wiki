---
title: "Process Supervision for Chain-of-Thought Reasoning via Monte Carlo Net Information Gain"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [reasoning, process-supervision, chain-of-thought, llm]
sources: ["https://arxiv.org/abs/2603.17815"]
---

# Process Supervision for Chain-of-Thought Reasoning via Monte Carlo Net Information Gain

## Overview
Multi-step reasoning in LLMs amplifies error propagation: a mistake at step k compounds through all subsequent steps. Outcome reward models provide only a final-answer signal, offering no guidance on which intermediate step failed. This paper proposes Monte Carlo Net Information Gain (MCNIG) as a process supervision signal that estimates the information value of each reasoning step, enabling targeted credit assignment without human step-level labels.

## Key Facts
- **Authors**: [arXiv 2603.17815](https://arxiv.org/abs/2603.17815)
- **Year**: 2026
- **arXiv**: [2603.17815](https://arxiv.org/abs/2603.17815)

## Key Contributions
- **Monte Carlo Net Information Gain (MCNIG)**: A process supervision signal derived from Bayesian information gain estimates across reasoning branches — each step receives a credit score proportional to its expected reduction in answer uncertainty
- **Step-level credit assignment without human labels**: Unlike human annotation-heavy process reward models, MCNIG is computed from the model's own reasoning trajectories, making it scalable to any domain
- **Improved propagation of correct reasoning**: On mathematical reasoning (GSM8K, MATH) and logical deduction tasks, MCNIG-supervised models outperform outcome-supervision baselines by 8-12% on problems requiring 5+ reasoning steps

## Related Papers
- [[the-weakest-link-tells-it-all-outcome-supervised-process-reward-modeling-via-learnable-credit-assignment-2606.27739]] — Related Papers: Learnable credit assignment across reasoning steps
- [[selaur-self-evolving-llm-agent-via-uncertainty-aware-rewards-2602.21158]] — Related Papers: Uncertainty-aware reward signals for LLM agent self-evolution
