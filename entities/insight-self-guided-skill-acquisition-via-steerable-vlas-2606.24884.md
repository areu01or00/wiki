---
title: "InSight: Self-Guided Skill Acquisition via Steerable VLAs"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [robotics, vla, skill-acquisition, steerable-primitives, vlm-decomposition, autonomous-data-collection, flywheel]
sources: ["https://arxiv.org/abs/2606.24884"]
---

# InSight: Self-Guided Skill Acquisition via Steerable VLAs

## Overview
Wang, Osterberg, Tian, Shorinwa, Wu, and Schwager address the structural capability ceiling of Vision-Language-Action (VLA) models whose manipulation skills are bounded by the demonstrations in the training data — and propose InSight, a framework that unlocks autonomous skill acquisition by rendering VLAs steerable at the primitive-action level (e.g., "move gripper to the bowl", "lift upward", "pour the bottle"); the framework consists of an automated segmentation pipeline that partitions demonstrations into labeled primitives via VLM plan decomposition and end-effector poses, and a VLM-guided data flywheel that identifies missing primitives required for a novel task, autonomously attempts demonstrations of the missing primitives with VLM-proposed low-level control, and automatically labels, stores, and integrates successful demonstrations into the VLA training set — evaluated across simulation and real-world manipulation tasks including block flipping, drawer closing, sweeping, twisting, and pouring, all without any human demonstrations of these target skills, with learned primitives composable to execute novel long-horizon behaviors.

## Key Facts
- **Authors**: Wang, Maggie; Osterberg, Lars; Tian, Stephen; Shorinwa, Ola; Wu, Jiajun; Schwager, Mac
- **Year**: 2026
- **arXiv**: [2606.24884](https://arxiv.org/abs/2606.24884)
- **Date**: 2026-06-23

## Key Contributions
- Diagnoses the structural capability ceiling of modern VLA models: manipulation skills are bounded by the demonstrations in the training data, so any novel task whose required primitives are absent from training data is unreachable without costly human demonstrations — leaving VLA deployment in real-world long-horizon settings structurally dependent on manual data-collection effort.
- Introduces primitive-level steerability for VLAs, where the action space is partitioned into named primitive actions (e.g., "move gripper to the bowl", "lift upward", "pour the bottle") rather than left as raw continuous control — turning VLA control into a composable, interpretable, and curriculum-friendly surface where novel primitives can be requested by name.
- Designs an automated segmentation pipeline that partitions existing demonstrations into labeled primitives via VLM plan decomposition (the VLM reads the task and decomposes the demonstration into a sequence of primitive labels) combined with end-effector pose analysis — eliminating the manual primitive-annotation step that would otherwise block the data flywheel.
- Proposes a VLM-guided data flywheel that closes the autonomous-skill-acquisition loop: the VLM identifies which primitives are missing for a target novel task, proposes low-level control sequences to attempt each missing primitive, the system attempts demonstrations autonomously, and successful demonstrations are automatically labeled, stored, and integrated back into the VLA training set — running without any human demonstrations of the target skills.
- Demonstrates real-world generalization to five distinct manipulation skills (block flipping, drawer closing, sweeping, twisting, pouring) learned autonomously — confirming that primitive-steered VLA + VLM-guided flywheel is a load-bearing primitive for autonomous VLA capability expansion in deployment regimes where human demonstrations of new tasks are unavailable.
- Surfaces *primitive-level-steerability-as-VLA-action-space* as the structurally correct primitive for autonomous skill acquisition — distinct from raw continuous control because the load-bearing axis is *composability of named primitives* rather than precision of end-effector trajectories — and *VLM-guided-autonomous-data-flywheel* as the load-bearing acquisition loop that closes the missing-primitive gap without human intervention, inverting the conventional VLA-training assumption that human demonstrations are required for new skills.

## Related Papers
- [[emergent-concepts]] — Parent meta-page that aggregates this and other emergent-concept discoveries from the wiki-explore-agent pipeline.
- [[in-context-world-modeling-for-robotic-control-2606.26025]] — Sibling VLA in-context adaptation work — ICWM adapts to new *system configurations* via self-generated interactions, InSight acquires new *skills* via autonomous primitive discovery — together they bracket the VLA-deployment surface between environmental-adaptation and capability-expansion primitives.
- [[eventvla-event-driven-visual-evidence-memory-for-long-horizon-vision-language-action-policies-2606.20092]] — Sibling VLA long-horizon memory work — EventVLA preserves visual evidence across long-horizon execution via foresight-driven keyframe selection, InSight acquires new skills autonomously to reduce the long-horizon-task-design effort — together they bracket the long-horizon-VLA surface between runtime-memory-preservation and training-time-skill-expansion primitives.
- [[policytrim-boosting-intrinsic-policy-efficiency-vla-models-2606.22540]] — Sibling VLA efficiency work — PolicyTrim improves VLA decision efficiency from fixed observations, InSight improves VLA capability surface via autonomous primitive expansion — together they bracket the VLA-improvement surface between decision-side efficiency and capability-side expansion primitives.