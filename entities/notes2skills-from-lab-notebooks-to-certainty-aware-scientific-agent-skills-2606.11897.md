---
title: "Notes2Skills: From Lab Notebooks to Certainty-Aware Scientific Agent Skills"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [arxiv, emergent-concept, llm-research]
sources: ["https://arxiv.org/abs/2606.11897"]
---

# Notes2Skills: From Lab Notebooks to Certainty-Aware Scientific Agent Skills

## Overview
Scientific discovery workflows usually contain and rely heavily on lab notes, where researchers record observations, interpret uncertain results, and plan follow-up experiments. Such informative lab notes preserve evolving scientific reasoning and author uncertainty, rather than polished final results exhibited in publications, providing a valuable opportunity for AI to engage in scientific exploration at a more comprehensive and deeper level. However, most prior work on scientific text focuses on papers, protocols, or structured databases, leaving informal laboratory notes underexplored as inputs to AI agents for science. This gap matters because lab notes often intermingle validated observations, tentative judgments, and possible experimental next steps within the same passage. If these signals are conflated, an AI agent may mistake uncertain scientific judgments for confirmed conclusions or executable actions. To this end, we present Notes2Skills, a two-stage framework for turning lab notebooks into verifiable skills for scientific AI agents while preserving the author's certainty. Across seven conditions and three wet-lab sessions, Notes2Skills is the only configuration that neither mistakes uncertain notes for firm instructions nor discards firm ones. We show that certainty preservation is the missing piece between lab notebooks and reliable agent skills, opening a path toward safer AI co-scientist systems.

## Key Facts
- **Authors**: Liu, Shi, Chen, Jiayao, Qin, Chengwei, Hu, Yanqing, Zhang, Jufan, Yang, Linyi
- **Year**: 2026
- **Date**: 2026-06-10
- **arXiv**: [2606.11897](https://arxiv.org/abs/2606.11897)
- **Subjects**: Computation and Language (cs.CL)

## Key Contributions
- Two-stage framework turning raw lab notebooks into verifiable agent skills while preserving author certainty markers
- First framework to explicitly separate validated observations, tentative judgments, and proposed next-steps from free-form notebook prose
- Across seven conditions and three wet-lab sessions, Notes2Skills is the only configuration that neither misclassifies uncertain notes as firm instructions nor discards firm ones
- Empirical demonstration that certainty preservation is the missing piece between lab notebooks and reliable agent skills
- Path toward "AI co-scientist" systems that can engage with scientists on the full reasoning arc (observations, uncertainty, next-steps), not just polished final results

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this paper was first recorded via emergent-concept search.
- [[tmax-a-simple-recipe-for-terminal-agents-2606.23321]] — Both papers target the gap between structured-output AI training and the messy reality of practitioner workflows; Tmax covers terminal-agent data while Notes2Skills covers scientific-notebook-to-agent-skill conversion.
- [[agents-last-exam-2606.05405]] — Complementary agent evaluation paradigms: Agents' Last Exam measures expert task performance, Notes2Skills measures a prerequisite for safe scientific-agent deployment (certainty-preserving interpretation of practitioner notes).
