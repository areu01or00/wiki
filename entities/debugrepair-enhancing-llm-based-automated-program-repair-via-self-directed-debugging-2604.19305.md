---
title: "DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [code generation, automated program repair, LLM debugging, software engineering, feedback-based APR]
sources: ["https://arxiv.org/abs/2604.19305"]
---

# DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging

## Overview
DebugRepair addresses a critical limitation in existing feedback-based APR: current methods iteratively refine patches using test execution feedback but rely on outcome-level failure symptoms (stack traces, error messages) that reveal how failures manifest without explaining root causes. DebugRepair introduces self-directed debugging — the LLM generates its own debugging hypotheses and iteratively tests them — enabling root-cause-guided patch generation rather than symptom-guided.

## Key Facts
- **Authors**: Wu, Linhao; Pei, Yifei; Yang, Zhen + 9
- **Year**: 2026
- **arXiv**: [2604.19305](https://arxiv.org/abs/2604.19305)
- **Discovered**: 2026-07-01 (Run 287)
- **Theme**: LLM APR / self-directed debugging / root-cause vs symptom-guided repair

## Key Contributions
- Self-directed debugging for APR: LLM generates and tests its own debugging hypotheses
- Root-cause-guided patch generation: moves beyond symptom-level feedback (stack traces) to causal reasoning
- Iterative refinement loop: autonomous debugging cycle without human-in-the-loop
- Demonstrates improved repair rates on challenging bugs where symptom-based feedback fails

## Related Papers
- [[a-systematic-approach-for-large-language-models-debugging-2604.23027]] — LLM debugging taxonomy (DebugRepair's self-directed debugging is a specific instantiation of broader LLM debugging patterns)
- [[agentga-evolving-code-solutions-in-agent-seed-space-via-inherited-parent-archives-2604.14655]] — Agent-driven code evolution (DebugRepair extends to the program repair / debugging axis with self-directed root-cause reasoning)
