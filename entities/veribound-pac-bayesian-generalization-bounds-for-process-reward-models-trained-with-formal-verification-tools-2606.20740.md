---
title: "VeriBound: PAC-Bayesian Generalization Bounds for Process Reward Models Trained with Formal Verification Tools"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [reward-model, pac-bayes, formal-verification, learning-theory, process-reward-model]
sources: ["https://arxiv.org/abs/2606.20740"]
arxiv_id: "2606.20740"
---

# VeriBound: PAC-Bayesian Generalization Bounds for Process Reward Models Trained with Formal Verification Tools

## Overview
VeriBound establishes the first PAC-Bayesian generalization theory for Process Reward Models (PRMs) trained on step-level error labels from formal verification tools (Z3, Isabelle). It explains the empirically-observed cross-task generalization from symbolic training tasks to diverse reasoning benchmarks and provides computable sample-complexity bounds for FOVER-style PRM training.

## Key Facts
- **Authors**: Amirul Rahman, Mohammed Sabih Alsharari
- **Year**: 2026
- **arXiv**: [2606.20740](https://arxiv.org/abs/2606.20740)

## Key Contributions
- **PAC-Bayesian generalization bound** relating empirical verification error on formal-verification-annotated training data to expected error on unseen reasoning tasks, with bound depending on verification accuracy and divergence between training/test task distributions.
- **Sample complexity result** showing that $O(d \log(d/\delta) / \epsilon^2)$ formal-verification-annotated examples suffice to achieve generalization error $\epsilon$ with probability $1-\delta$, where $d$ is the complexity of the PRM hypothesis class.
- **Convergence analysis** proving that PRM training with formal-verification supervision converges to a near-optimal policy under verifiable task coverage conditions.
- **Best-of-K downstream bound** characterizing the gap between Best-of-K policy reward and oracle policy reward as a function of PRM generalization error and verification accuracy.
- **First theoretical explanation** for FOVER's empirically-observed cross-task generalization phenomenon — closing the gap between empirical success and theoretical understanding of PRMs trained on automated formal-verification annotations.

## Related Papers
- [[a-verifiable-search-is-not-a-learnable-chain-of-thought-2606.21884]] — Sibling paper that argues verifiable-search is not a learnable CoT primitive; complements VeriBound by showing where verification-driven learning breaks.
- [[discretizing-reward-models-2606.21795]] — Sibling paper on reward-model oversensitivity as structural failure mode; VeriBound provides learning-theory bounds that Discretizing-Reward-Models motivates empirically.
- [[leap-supercharging-llms-for-formal-mathematics-with-agentic-frameworks-2606.03303]] — Adjacent paper on formal mathematics + LLM agentic frameworks; VeriBound's verification-tool training data comes from the same formal-verification ecosystem (Isabelle/Z3) that LEAP leverages.
- [[the-verification-horizon-no-silver-bullet-for-coding-agent-rewards-2606.26300]] — Sibling from Run 50 on the limits of verification-based rewards in coding agents; VeriBound provides a learning-theory view that complements Verification-Horizon's empirical failure-mode analysis.
- [[maxproof-scaling-mathematical-proof-with-generative-verifier-rl-and-population-level-test-time-scaling-2606.13473]] — Sibling paper on generative-verifier RL for mathematical proof; VeriBound's PAC-Bayesian bounds apply to MaxProof's PRM component.