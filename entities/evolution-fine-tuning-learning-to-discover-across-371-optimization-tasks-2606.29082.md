---
title: "Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [training, llm, self-improvement]
sources: ["https://arxiv.org/abs/2606.29082"]
---

# Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks

## Overview
Evolution Fine-Tuning (EFT) teaches LLMs to acquire iterative evolutionary search capabilities — learning which parts of a solution to mutate, when to backtrack, and how to reuse discovered insights across tasks — by converting evolutionary search trajectories from 371 optimization tasks into supervision. EFT introduces the Finch Collection (156K trajectories across 10 domains) and fine-tunes 2B–9B open-source LLMs. The result: models that surpass base counterparts by 10.22% on held-out tasks and can pair with test-time RL to match SOTA on circle-packing and outperform on the Erdős minimum-overlap problem.

## Key Facts
- **Authors**: Anonymous (arXiv:2606.29082)
- **Year**: 2026
- **arXiv**: [2606.29082](https://arxiv.org/abs/2606.29082)

## Key Contributions
- **Finch Collection**: 156K evolutionary search trajectories spanning 10 domains and 371 optimization tasks (mathematical conjectures, GPU kernel design, scientific law discovery, combinatorial puzzles)
- **EFT mid-training paradigm**: converts search scaffold behavior (mutation selection, backtracking, trajectory reuse) into model weights via supervised fine-tuning — transfers the "practice phase" capability into the model itself
- **Cross-task generalization**: models fine-tuned on evolutionary trajectories outperform base models by 10.22% average on 22 held-out tasks without any task-specific fine-tuning
- **Test-time RL pairing**: EFT models paired with test-time RL achieve SOTA on circle-packing tasks and outperform base model on Erdős minimum-overlap problem
- **First "discovery agent practice phase" paper**: unlike prior work where search scaffolding is discarded, EFT internalizes the iterative evolution capability — making it the first paper to give models a reusable "experience of evolving solutions"

## Related Papers
- [[worldevolver-self-evolving-world-models-for-llm-agent-planning-2606.30639]] — WorldEvolver shares the self-evolution theme; EFT internalizes iterative discovery while WorldEvolver externalizes world model planning
- [[self-improvement-can-self-regress-rise-and-collapse-llm-self-training-2606.21090]] — Self-Improvement Can Self-Regress covers LLM self-training collapse failure modes; EFT is the complementary success-mode — how to make self-evolution work reliably
