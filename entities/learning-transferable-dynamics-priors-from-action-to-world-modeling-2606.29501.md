---
title: "Learning Transferable Dynamics Priors from Action to World Modeling"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [world-modeling, robotics, dynamics-priors, transfer-learning, action-conditioned]
sources: ["https://arxiv.org/abs/2606.29501"]
---

# Learning Transferable Dynamics Priors from Action to World Modeling

## Overview
This paper studies action-conditioned world modeling as a scalable way to learn transferable dynamics priors for robot learning. The key insight is that pretraining a model to predict how actions drive visual scene evolution captures reusable interaction dynamics beyond appearance-level video generation. The resulting world model (A2World) generalizes across tasks and domains.

## Key Facts
- **Authors**: (from arXiv abstract — see paper)
- **Year**: 2026
- **arXiv**: [2606.29501](https://arxiv.org/abs/2606.29501)

## Key Contributions
- Proposes A2World: action-conditioned world model pretrained on large-scale interactive video data
- Demonstrates that dynamics priors transfer across tasks and domains better than appearance priors
- Enables sample-efficient robot learning by leveraging reusable interaction dynamics
- Load-bearing axis: action-driven dynamics priors vs. passive video generation priors

## Related Papers
- [[hallucination-in-world-models-is-predictable-and-preventable-2606.27326]] — Hallucination in world models
- [[the-weakest-link-tells-it-all-outcome-supervised-process-reward-modeling-via-learnable-credit-assignment-2606.27739]] — Process reward modeling and credit assignment
- [[trace2skill-distill-trajectory-local-lessons-into-transferable-agent-skills-2603.25158]] — Trajectory-to-skill distillation for agent skill transfer
