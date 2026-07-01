---
title: "Using Probabilistic Programs to Train Inductive Reasoning in Large Language Models"
created: 2026-07-02
updated: 2026-07-02
type: entity
tags: [reasoning, llm, induction, probabilistic-programming]
sources: ["https://arxiv.org/abs/2606.09856"]
---

# Using Probabilistic Programs to Train Inductive Reasoning in Large Language Models

## Overview
Post-training LLMs for reasoning typically focuses on deductive tasks (math, code) where correctness is verifiable. This paper addresses inductive reasoning: inferring uncertain beliefs from sparse, ambiguous observations — the kind of real-world reasoning agents face in open-ended deployment. The authors use probabilistic programs as both the representation and training target, enabling LLMs to learn structured uncertainty from ambiguous evidence.

## Key Facts
- **Authors**: Zhang, Liyi; Jagadish, Akshay K.; Lake, Brenden M. + 1
- **Year**: 2026
- **arXiv**: [2606.09856](https://arxiv.org/abs/2606.09856)

## Key Contributions
- **Probabilistic program representation for LLM induction**: Uses probabilistic programs (而非 deterministic logic) as the training target for inductive reasoning — models learn to represent and reason over distributions, not just point estimates
- **Addresses data curation challenge**: Provides a method for generating large-scale, high-quality labeled datasets for inductive reasoning — targets that are inherently probabilistic and ambiguous
- **Distinguishes induction from deduction**: Systematically addresses why standard fine-tuning methods fail for inductive targets — the supervision signal is distributions over outcomes, not binary correct/incorrect labels
- **Inductive reasoning as a core LLM capability**: Positions induction as distinct from and complementary to deductive reasoning (math/code) — essential for agents operating in open-ended real-world environments

## Related Papers
- *The Periodic Table of LLM Reasoning* (2606.11470) — Surveys reasoning paradigms including both deductive and inductive modes. This paper provides the missing training methodology for the inductive branch that the survey taxonomy identifies as under-explored.
- *VeriEvol: Scaling Multimodal Mathematical Reasoning* (2606.23543) — Also targets reasoning scaling via verifiable supervision, but focuses on deductive mathematical reasoning. This paper complements it by providing a framework for the inductive branch where verifiability is inherently limited.
