---
title: "SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent-skill, continual-learning, persistent-memory, decision-history, LLM-agents]
sources: ["https://arxiv.org/abs/2606.08671"]
---

# SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent Decision History

## Overview
SkillHone is a harness for continual agent skill evolution that pairs skill revisions with evaluation-side evidence supplying practice feedback, recording structured histories of diagnoses, revisions, evidence, and outcomes. Role-separated subagents run candidate skills on practice probes and propose revisions informed by prior decisions, enabling cross-session refinement without rediscovering past rationale.

## Key Facts
- **Authors**: Unknown (arXiv 2606.08671)
- **Year**: 2026
- **arXiv**: [2606.08671](https://arxiv.org/abs/2606.08671)

## Key Contributions
- Persistent decision history enables agents to audit prior skill changes and reuse past rationale across sessions
- Role-separated subagents decouple candidate skill execution from revision proposal, preventing feedback loops
- Outperforms commercially backed deep-research agent by 15.8 points on GAIA and 3.2 points on WebWalkerQA-EN
- Improves accuracy by 18.8 average points across seven internal tool-mediated analysis settings
- First harness that treats decision history as a first-class artifact of skill evolution (not just final artifacts)

## Related Papers
- [[skillgrad-optimizing-agent-skills-like-gradient-descent-2605.27760]] — SkillGrad optimizes agent skills via gradient-like updates (orthogonal — SkillGrad optimizes within bounded runs; SkillHone focuses on cross-session persistent history)
- [[trace2skill-distill-trajectory-local-lessons-into-transferable-agent-skills-2603.25158]] — Trace2Skill distills trajectory lessons into transferable skills (orthogonal — single-session distillation vs persistent cross-session evolution)
- [[notes2skills-from-lab-notebooks-to-certainty-aware-scientific-agent-skills-2606.11897]] — Notes2Skills converts lab notebooks to agent skills (orthogonal — structured notebook input vs dynamic decision history reuse)
- [[memprobe-probing-longterm-agent-memory-via-hidden-userstate-recovery-2606.24595]] — MEMPROBE probes long-term agent memory via hidden-state recovery (orthogonal — memory probing vs skill evolution via persistent decision records)
