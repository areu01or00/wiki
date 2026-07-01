---
title: "Automating Potential-based Reward Shaping with Vision Language Model Guidance"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [reinforcement-learning, reward-shaping, vlm, sparse-reward, rl-optimization]
sources: ["https://arxiv.org/abs/2606.27180"]
---

# Automating Potential-based Reward Shaping with Vision Language Model Guidance

## Overview
VLM-PBRS automates the design of potential functions for potential-based reward shaping (PBRS) in RL, which traditionally requires manual engineering. PBRS guarantees policy optimality preservation but needs a heuristic potential function over states. The framework uses a Vision Language Model to generate shaped reward signals that guide exploration toward informative regions of the state space, solving the sparse reward attribution problem without reward hacking.

## Key Facts
- **Authors**: Henrik Müller, Daniel Kudenko
- **Year**: 2026
- **arXiv**: [2606.27180](https://arxiv.org/abs/2606.27180)

## Key Contributions
- First framework automating PBRS potential function design via VLM guidance — removes need for manual heuristic engineering
- VLM-PBRS guarantees preservation of optimal policy set (inherited from PBRS theory) while solving the sparse reward exploration problem
- Addresses the key failure mode of naive reward shaping: reward hacking via auxiliary signal exploitation
- Provides interpretable intermediate feedback signals grounded in visual state understanding

## Related Papers
- [[renio-reweighting-negative-trajectory-importance-for-llm-on-policy-distillation-2606.23104]] — ReNIO: on-policy distillation with negative trajectory importance (RL training pipeline, complementary PBRS addresses early exploration)
- [[self-improvement-can-self-regress-2606.21090]] — Self-Improvement Can Self-Regress: RL collapse failure modes (RL training instability context)
