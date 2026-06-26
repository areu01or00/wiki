---
title: "The Defense Trilemma: Why Prompt Injection Defense Wrappers Fail"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [safety, prompt-injection, adversarial-robustness, theoretical-impossibility, defense-mechanism, lean-verified]
sources: ["https://arxiv.org/abs/2604.06436"]
---

# The Defense Trilemma: Why Prompt Injection Defense Wrappers Fail

## Overview
Proves a theoretical impossibility result for prompt-injection defense wrappers: no continuous, utility-preserving wrapper defense (a function that preprocesses inputs before the model sees them) can make all outputs strictly safe for an LLM with connected prompt space. Establishes three results under successively stronger hypotheses — boundary fixation, ε-robust constraint, and persistent unsafe region — constituting a "defense trilemma" where continuity, utility preservation, and completeness cannot coexist.

## Key Facts
- **Authors**: Zhang, Mingwei; Petrov, Aleksandar; Rivera, Carla
- **Year**: 2026
- **arXiv**: [2604.06436](https://arxiv.org/abs/2604.06436)

## Key Contributions
- **Defense trilemma theorem**: formally proves that for any continuous wrapper defense preserving utility on a connected prompt space, a positive-measure subset of inputs remains strictly unsafe — three-way tradeoff (continuity + utility + completeness) is impossible
- **Three-tier result hierarchy**: boundary fixation (basic case), ε-robust constraint (under Lipschitz regularity), persistent unsafe region (under transversality) — each strengthens the impossibility under weaker assumptions
- **Multi-turn and stochastic extensions**: parallel discrete results requiring no topology, extended to multi-turn interactions, stochastic defenses, and capacity-parity settings
- **Mechanically verified in Lean 4**: full theory machine-checked, empirically validated on three LLMs — establishes defensive-prompt-injection-as-system-property primitive, distinct from training-time alignment or architectural defenses

## Related Papers
- [[multibreak-a-scalable-and-diverse-multi-turn-jailbreak-benchmark-for-evaluating-llm-safety-2605.01687]] — Sibling multi-turn-jailbreak primitive — Defense Trilemma provides the theoretical foundation explaining why MultiBreak's empirical findings generalize
- [[what-intermediate-layers-know-detecting-jailbreaks-from-entropy-dynamics-2606.25182]] — Sibling jailbreak-detection primitive — both surface internal-model signals as defensive mechanism, complementing the wrapper-level impossibility
- [[scaling-rl-for-code-generation-with-synthetic-data-and-curriculum-2603.24202]] — Sibling from Run 70 — orthogonal primitive (synthetic-data curriculum) bracketing the security side with the training-data side
