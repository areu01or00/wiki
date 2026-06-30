---
title: "Toward Secure and Reliable PDDL Formalization of Large Language Models with Planner-in-the-Loop Feedback"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [planning, formal-verification, llm, safety]
sources: ["https://arxiv.org/abs/2606.29700"]
---

# Toward Secure and Reliable PDDL Formalization of Large Language Models with Planner-in-the-Loop Feedback

## Overview
This paper addresses the critical problem of LLM-generated planning specifications that are both executable and verifiable. The authors present NL-PDDL-Bench, a multi-domain benchmark for natural-language-to-PDDL specification, coupled with a planner-in-the-loop framework that uses validator and planner diagnostics to repair non-executable specifications through localized edits.

## Key Facts
- **Authors**: (from arxiv abstract extraction — needs author field)
- **Year**: 2026
- **arXiv**: [2606.29700](https://arxiv.org/abs/2606.29700)

## Key Contributions
- NL-PDDL-Bench: multi-domain benchmark for NL-to-PDDL specification with planner-verified executability and difficulty scaling by object count
- Planner-in-the-loop framework: uses validator and planner diagnostics for localized repair of non-executable specifications
- Planner-grounded optimization recipe combining LoRA SFT + offline DPO + inference-time planner repair (no online planner during training)
- Unified evaluation suite for parseability, solvability, specification similarity, and plan-level consistency
- Demonstrates substantial gains in planner success and plan-level agreement; highlights value of externally verifiable formalization for safety-sensitive LLM deployment

## Related Papers
- [[emergent-concepts]] — Parent topic node for emergent LLM research
