---
title: "Hallucination in World Models is Predictable and Preventable"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [world-models, generative-models, hallucination-taxonomy, data-centric, coverage-aware-sampling, curiosity-rewards, mmbench]
sources: ["https://arxiv.org/abs/2606.27326"]
---

# Hallucination in World Models is Predictable and Preventable

## Overview
Hansen and Wang address the structural hallucination failure mode of modern generative world models that render increasingly realistic action-controllable futures while drifting from ground-truth dynamics — and hypothesize that hallucination concentrates in low-coverage regions of the state-action space where lightweight data-centric signals can both detect and mitigate it; they introduce MMBench2, a 427-hour, 210-task dataset for visual world modeling with ground-truth actions, rewards, and live simulators, train a 350M-parameter world model on it, and identify three distinct hallucination modes — perceptual, action-marginalized, and scene-diverging — each anchored to a different stage of the pipeline, develop three lightweight signals that accurately predict where the model will fail, design a coverage-aware sampling technique to close coverage gaps at training time, and use the hallucination predictors as curiosity rewards for targeted online data collection, yielding a data-efficient finetuning recipe that adapts the pretrained world model to entirely unseen environments with as few as 50 real environment trajectories.

## Key Facts
- **Authors**: Hansen, Nicklas; Wang, Xiaolong
- **Year**: 2026
- **arXiv**: [2606.27326](https://arxiv.org/abs/2606.27326)
- **Date**: 2026-06-25

## Key Contributions
- Diagnoses the structural hallucination failure mode of modern generative world models — rollouts remain visually fluent while drifting from ground-truth dynamics, a silent-coherence failure mode that fluency-based evaluation metrics systematically miss because the rendered futures look realistic even when they are physically wrong.
- Hypothesizes and empirically validates that hallucination concentrates in low-coverage regions of the state-action space, making it both *predictable* (lightweight data-centric signals can identify where the model will fail) and *preventable* (coverage-aware sampling at training time + curiosity-reward data collection at deployment time can close the gaps).
- Introduces MMBench2 — a 427-hour, 210-task dataset for visual world modeling with ground-truth actions, rewards, and live simulators — as the load-bearing substrate for measuring and attributing hallucination, structurally distinct from prior benchmarks that hide hallucination behind aggregate metrics or rely on offline logs without ground-truth simulators.
- Identifies three distinct hallucination modes — *perceptual* (anchored to the rendering stage), *action-marginalized* (anchored to the action-conditioning stage where actions lose their causal influence), and *scene-diverging* (anchored to the scene-continuity stage where the rendered scene diverges from the rollout trajectory) — each with a distinct failure signature and a distinct lightweight predictor.
- Develops three data-centric signals that accurately predict where the model will fail (one per hallucination mode), enabling pre-rollout hallucination forecasting rather than post-hoc hallucination detection — inverting the conventional generative-model evaluation framing where hallucination is only observable after the model has already produced the wrong rollout.
- Designs a coverage-aware training-time sampling technique that uses the three hallucination predictors to weight training samples toward low-coverage state-action regions — closing coverage gaps during training rather than relying on post-training correction.
- Uses the hallucination predictors as curiosity rewards for targeted online data collection, enabling data-efficient finetuning to entirely unseen environments with as few as 50 real environment trajectories — yielding a deployment-time recipe that operationalizes hallucination-prevention rather than hallucination-detection.
- Surfaces *data-centric-hallucination-predictability-and-preventability* as the structurally correct primitive for generative-world-model evaluation and improvement — distinct from fluency-based evaluation because the load-bearing axis is *low-coverage-region-identification* rather than aggregate-rendering-quality — and *hallucination-predictors-as-curiosity-rewards* as the load-bearing deployment primitive that closes the train-test coverage gap with target-efficient online data collection.

## Related Papers
- [[emergent-concepts]] — Parent meta-page that aggregates this and other emergent-concept discoveries from the wiki-explore-agent pipeline.
- [[causal-rcm-a-unified-teacher-forcing-and-self-forcing-open-recipe-for-autoregressive-diffusion-distillation-in-streaming-video-generation-and-interactive-world-models-2606.25473]] — Sibling world-model + diffusion-distillation work — Causal-RCM focuses on the training-recipe axis for autoregressive diffusion distillation in streaming video generation, Hallucination-in-World-Models focuses on the failure-mode axis for generative world models with low-coverage-region identification — together they bracket the world-model-training surface between training-recipe design and training-data coverage.
- [[in-context-world-modeling-for-robotic-control-2606.26025]] — Sibling world-model robotics work — ICWM uses world-model context for in-task system identification in VLA control, Hallucination-in-World-Models uses world-model failure-mode signals for training-time and online hallucination prevention — together they bracket the world-model-application surface between inference-time system-adaptation and training/deployment-time failure-prevention primitives.
- [[world-action-models-a-survey-2606.20781]] — Sibling world-model survey work that establishes the taxonomy of world-model action-controllable generation — Hallucination-in-World-Models complements this survey by surfacing the *failure-mode taxonomy* (perceptual / action-marginalized / scene-diverging) and the *coverage-aware mitigation recipe* that surveys typically do not address.
- [[qwen-agentworld-language-world-models-for-general-agents-2606.24597]] — Sibling agentic world-model work — Qwen-AgentWorld builds language world models for general agents, Hallucination-in-World-Models builds coverage-aware hallucination mitigation for visual world models — together they bracket the agentic-world-model surface between language-world-model design and visual-world-model failure prevention.
- [[world-value-models-robotic-manipulation-2606.24742]] — Sibling robotics world-model work — World-Value-Models uses world-model value scores for training-data selection, Hallucination-in-World-Models uses low-coverage-region signals for training-time sampling and online data collection — together they bracket the world-model-deployment surface between training-time data selection (filter existing data) and deployment-time coverage closure (collect new data targeting low-coverage regions).