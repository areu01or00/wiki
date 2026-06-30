---
title: "Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [agentic-ai, world-models, planning, llm-training, reinforcement-learning]
sources: ["https://arxiv.org/abs/2606.27483"]
---

# Internalizing the Future: A Unified Agentic Training Paradigm for World Model Planning

## Overview
LLM agents are fundamentally reactive in long-horizon tasks — unlike humans who employ "what-if" reasoning, standard agents lack an internal world model to simulate future outcomes before commitment. This paper proposes internalizing future-aware planning by training a single autoregressive model to verbalize both a prospective state rollout and a plan-conditioned success estimate (a textual analogue of the Q-value).

## Key Facts
- **arXiv**: [2606.27483](https://arxiv.org/abs/2606.27483)
- **Year**: 2026
- **Theme**: world-model-planning / agentic-training-paradigm / internal-prediction

## Key Contributions
- **Three-stage training paradigm**: (i) World Model Agentic Mid-Training (WM-AMT) to inject latent predictive capabilities into the policy; (ii) Format-Eliciting SFT (FE-SFT) to structure this injected capability; (iii) Foresight-Conditioned Reinforcement Learning (FC-RL) to refine calibration and utility of generated simulations
- **Format-capability gap identification**: Simply fine-tuning agents on look-ahead traces during post-training leads to superficial mimicry of foresight without genuine predictive grounding
- **Evaluated on**: search and mathematical reasoning tasks; consistently outperforms other training baselines
- **First** unified three-stage pipeline for grounded and calibrated internal world modeling in LLM agents in the wiki

## Related Papers
- [[worldevolver-self-evolving-world-models-for-llm-agent-planning-2606.30639]] — WorldEvolver: Self-Evolving World Models for LLM Agent Planning — companion paper on world model self-evolution; orthogonal axis (self-evolution loop vs. three-stage training paradigm)
- [[orca-the-world-is-in-your-mind-2606.30534]] — Orca: General World Foundation Model — NSP-based world foundation model; orthogonal axis (latent space prediction vs. textual look-ahead rollout)
- [[selaur-self-evolving-llm-agent-via-uncertainty-aware-rewards-2602.21158]] — SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards — self-evolution via uncertainty signals; orthogonal axis (uncertainty-as-reward vs. foresight-conditioned RL)
