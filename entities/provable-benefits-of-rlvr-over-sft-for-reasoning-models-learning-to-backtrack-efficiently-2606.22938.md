---
title: "Provable Benefits of RLVR over SFT for Reasoning Models: Learning to Backtrack Efficiently"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [reinforcement-learning, reasoning-models, rlvr, sft-comparison, theory]
sources: ["https://arxiv.org/abs/2606.22938"]
---

# Provable Benefits of RLVR over SFT for Reasoning Models: Learning to Backtrack Efficiently

## Overview
This paper provides the first theoretical analysis of why reinforcement fine-tuning (RLVR) induces better reasoning ability than supervised fine-tuning (SFT). The authors model chain-of-thought reasoning as a pathfinding problem and prove that SFT, trained on golden shortest paths without negative examples, cannot learn efficient backtracking — while RLVR-trained models learn to backtrack efficiently from dead ends using only outcome reward.

## Key Facts
- **arXiv**: [2606.22938](https://arxiv.org/abs/2606.22938)
- **Year**: 2026

## Key Contributions
- Proves exponential separation in inference-time compute between RLVR and SFT for reasoning tasks
- Shows RLVR models learn the location of difficult decisions in reasoning chains, enabling better allocation of inference-time compute
- Demonstrates reasoning traces of an RLVR model can be distilled to train a base model to backtrack efficiently
- First formal characterization of why RLVR outperforms SFT for reasoning models

## Related Papers
- [[prune-you-generate-online-rollout-pruning-faster-better-2603.24840]] — Prune as You Generate: Online rollout pruning for RLVR; both papers address RLVR training efficiency
- [[athena-r1-an-ai-agent-for-treatment-reasoning-over-a-biomedical-tool-universe-2606.28692]] — ATHENA-R1: RL-trained biomedical reasoning agent via RL over 212 tools; empirical application of RLVR training
- [[adaptive-test-time-compute-allocation-for-reasoning-llms-via-constrained-policy-optimization-2604.14853]] — Test-time compute allocation for reasoning LLMs; addresses inference-time compute allocation
