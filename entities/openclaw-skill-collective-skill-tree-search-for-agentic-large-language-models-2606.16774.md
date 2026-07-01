---
title: "OpenClaw-Skill: Collective Skill Tree Search for Agentic Large Language Models"
created: "2026-07-01"
updated: "2026-07-01"
type: entity
tags: [skill-learning, multi-agent, tree-search, agentic-llm, skill-construction]
sources: ["https://arxiv.org/abs/2606.16774"]
---

# OpenClaw-Skill: Collective Skill Tree Search for Agentic Large Language Models

## Overview
Equipping LLM agents with reusable, generalizable skills is crucial for solving complex real-world tasks. This paper proposes Collective Skill Tree Search (CSTS), a framework that automatically constructs structured, diverse skill trees via collective intelligence — multiple LLM agents jointly search, identify, and compose reusable skill primitives into a tree structure that enhances tool use, multi-step reasoning, and dynamic environment interaction.

## Key Facts
- **Authors**: Lin, Tianyi; Sun, Chuanyu; Zhang, Jingyi + 6
- **Year**: 2026
- **arXiv**: [2606.16774](https://arxiv.org/abs/2606.16774)

## Key Contributions
- Introduces Collective Skill Tree Search (CSTS) — a tree-search-based skill construction framework where multiple LLM agents collaboratively build structured skill trees
- The skill tree captures compositional, reusable primitives that generalize across tool use, reasoning, and environment interaction tasks
- Demonstrates significant improvement over single-agent skill acquisition on the OpenClaw benchmark suite
- First paper in the wiki to address collective intelligence for automated skill tree construction — distinct from individual skill learning frameworks

## Related Papers
- [[a-framework-for-evaluating-agentic-skills-at-scale-2606.17819]] — SkillsBench provides the evaluation methodology for agentic skills at scale; OpenClaw-Skill provides the skill construction methodology that SkillsBench can evaluate
