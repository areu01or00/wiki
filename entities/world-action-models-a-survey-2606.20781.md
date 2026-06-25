---
title: "World Action Models: A Survey"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [survey, world-models, embodied-ai, robotics, action-models, vla]
sources: ["https://arxiv.org/abs/2606.20781"]
---

# World Action Models: A Survey

## Overview
A structured survey of World Action Models (WAMs) — embodied predictive-action models that make a forecast of the future available to action — that disambiguates WAMs from broader world models, video-generation models, action-grounded video world models, and Vision-Language-Action policies by decomposing each method along two complementary axes (what it is required to generate, and how its predictive substrate, backbone, action coupling, and deployment regime are composed). Shen, Qiuhong; Zhang, Shihua; Liao, Yue; Li, Qi; Tan, Zhenxiong; Wang, Shizun; Yan, Shuicheng; Wang, Xinchao organize the field around a unifying account of interactability, causality, persistence, physical plausibility, and generalization, surfacing a consistent design pattern — WAMs are not simply video generators with action heads, but predictive-action methods whose design choices trade representational richness against compute, memory, latency, and action-label cost, and the field is moving toward methods that generate less of the future while preserving what control requires.

## Key Facts
- **Authors**: Shen, Qiuhong; Zhang, Shihua; Liao, Yue; Li, Qi; Tan, Zhenxiong; Wang, Shizun; Yan, Shuicheng; Wang, Xinchao
- **Year**: 2026
- **arXiv**: [2606.20781](https://arxiv.org/abs/2606.20781)
- **Subjects**: cs.RO, cs.AI, cs.CV
- **Date**: 2026-06-18
- **Survey homepage**: https://world-action-models.github.io/

## Key Contributions
- Clarifies the boundaries between broad world models, video-generation models, action-grounded video world models, VLA policies, and WAMs — a category overlap that recent rapid expansion has blurred
- Organizes existing WAM work through two complementary views: a generated-object-type axis (rendered futures / latent futures / video-generation-free action reasoning) and a method-anatomy axis (predictive substrate, backbone, action coupling, deployment regime)
- Provides a unified discussion of interactability, causality, persistence, physical plausibility, and generalization, supporting comparative reading across the heterogeneous prior literature
- Catalogs data, evaluation, and open-challenges dimensions, identifying the consistent design pattern that WAMs are predictive-action methods rather than video generators with action heads — and surfacing the field's movement toward methods that generate less of the future while preserving what control requires
- Establishes a common account that supports head-to-head comparison of WAM approaches previously separated by deployment regime, backbone choice, or action-coupling mechanism

## Related Papers
- [[qwen-agentworld-language-world-models-for-general-agents-2606.24597]] — Language world models for general agents (agent-side sibling)
- [[ebench-elemental-diagnosis-of-generalist-mobile-manipulation-policies-2606.18239]] — Robotics multi-axis-diagnostic benchmark (manipulation-policy sibling)
- [[the-periodic-table-of-llm-reasoning-a-structured-survey-of-reasoning-paradigms-abstractions-building-blocks-and-open-challenges-2606.11470]] — Sibling LLM-reasoning survey
