---
title: "Agentic Safety is an Epistemic Property, Not a Behavioral One"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [safety, alignment, agentic-ai, epistemic]
sources: ["https://arxiv.org/abs/2606.28347"]
---

# Agentic Safety is an Epistemic Property, Not a Behavioral One

## Overview
The paper argues that contemporary AI safety approaches (pretraining interventions, RLHF, deployment-time controls, red-teaming) certify only behavioral snapshots — which becomes insufficient as AI systems grow more capable, dynamic, embodied, and self-improving. The authors propose that agentic safety must be reframed as an epistemic property: safety depends not just on whether a system behaves acceptably, but on whether it knows, reasons about, and updates its beliefs about safety in context. This shifts the frame from output certification to epistemic agency.

## Key Facts
- **Authors**: Wang, Charles L.; Dorchen, Keir; Jin, Peter
- **Year**: 2026
- **arXiv**: [2606.28347](https://arxiv.org/abs/2606.28347)

## Key Contributions
- Epistemic reframing of AI safety: safety as property of the learner's belief state, not behavioral output
- Addresses the snapshot limitation of current RLHF/alignment pipelines for dynamic, self-improving agents
- Introduces concept of safety-as-epistemic-agency — systems must reason about safety uncertainty, not just avoid tested behaviors
- Framework for evaluating whether agentic systems can update safety beliefs in novel contexts

## Related Papers
- [[emergent-concepts]] — Parent emergent-concept discovery chain that led to this paper's identification
