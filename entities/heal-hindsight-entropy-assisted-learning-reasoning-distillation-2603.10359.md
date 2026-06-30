---
title: "HEAL: Hindsight Entropy-Assisted Learning for Reasoning Distillation"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [distillation, reasoning, RL, teacher-student]
sources: ["https://arxiv.org/abs/2603.10359"]
---

# HEAL: Hindsight Entropy-Assisted Learning for Reasoning Distillation

## Overview
This paper addresses a key limitation in distilling reasoning capabilities from Large Reasoning Models (LRMs) into smaller models: standard rejection sampling treats the teacher as a static filter, discarding complex "corner-case" problems where the teacher fails to generate useful demonstrations. HEAL introduces hindsight entropy assistance, which allows the teacher to recover from failure cases by exploring alternative reasoning paths and providing useful signal even on problems where the initial attempt fails.

## Key Facts
- **Authors**: Unknown (per arXiv 2603.10359)
- **Year**: 2026
- **arXiv**: [2603.10359](https://arxiv.org/abs/2603.10359)

## Key Contributions
- Hindsight entropy mechanism for reasoning distillation that extends teacher capability to corner cases
- Overcomes static-filter limitation of standard rejection sampling in LRM distillation
- Enables dense supervision on problems where teacher initially fails
- Provides framework for extracting useful signal from failed teacher reasoning trajectories

## Related Papers
- [[emergent-concepts]] — Parent emergent-concept discovery chain
