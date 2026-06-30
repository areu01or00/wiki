---
title: "Repeated post-training is not Self-improving: Diagnosing Scientific Amnesia in Continual DPO Pipelines"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [continual-learning, DPO, RLHF, failure-mode]
sources: ["https://arxiv.org/abs/2606.21089"]
---

# Repeated post-training is not Self-improving: Diagnosing Scientific Amnesia in Continual DPO Pipelines

## Overview
This paper documents Scientific Amnesia, a novel failure mode in continual DPO pipelines where models preserve previously learned behaviors but progressively lose the ability to efficiently acquire new ones, unlike classical catastrophic forgetting which degrades old capabilities.

## Key Facts
- **arXiv**: [2606.21089](https://arxiv.org/abs/2606.21089)
- **Year**: 2026
- **Theme**: continual-DPO self-training failure

## Key Contributions
- Introduces Scientific Amnesia: a new failure mode in continual DPO pipelines where new task acquisition efficiency degrades over consecutive DPO campaigns
- Shows the failure direction is opposite to catastrophic forgetting: old capabilities preserved but new acquisition efficiency declines
- Identifies KL divergence between reference and post-DPO policy as the key predictor of Scientific Amnesia onset
- Proposes an adaptive buffer strategy achieving 40% reduction in scientific amnesia rate without additional compute
- Validated across 6 academic benchmarks and 12 model checkpoints from a production shipping model

## Related Papers
- [[emergent-concepts]] — Parent emergent concepts discovery framework
