---
title: "Natural Ungrokking: Asymmetric Control of Which Rules Survive Pretraining"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [training-dynamics, pretraining, rule-acquisition, corpus-statistics, grokking, ungrokking, displacement, asymmetry]
sources: ["https://arxiv.org/abs/2606.26050"]
---

# Natural Ungrokking: Asymmetric Control of Which Rules Survive Pretraining

## Overview
First paper in the wiki to **establish that learned rules can be silently and permanently destroyed during ordinary pretraining**, with no trace in the loss curve — and that this destruction is **predictable from a single corpus statistic (rule-support frequency)** while **control over the rule's fate is asymmetric** (easy to kill with counter-evidence, impossible to restore by injecting support back, even at 450× the natural-sustaining level).

## Key Facts
- **Authors**: Juliana Li, Diya Sreedhar
- **Year**: 2026
- **arXiv**: [2606.26050](https://arxiv.org/abs/2606.26050)
- **Online date**: 2026-06-24

## Key Contributions
- **Natural Ungrokking as within-run reversal**: a small language model that *learns* the pronoun-gender rule by step 925 (generalizes 0.94 to held-out probes) **collapses** to near zero on the same probes by step 3,500, although the rule's evidence is still in the training data — a previously-undocumented same-run, same-rule reversal that is invisible in the loss curve
- **Corpus-statistic-as-fate-determinant**: across un-intervened runs (two corpora × three budgets × three seeds), the **support frequency of the rule's winning pattern** in the training stream is the predictive variable for whether a rule survives; the data-to-parameter ratio only modulates how *deeply* a doomed rule falls
- **Cross-corpus replication**: the same emerge-then-collapse dynamics are observed in public Pythia checkpoints, with collapse depth ordered by model scale as predicted by the corpus-frequency hypothesis
- **Displacement-as-forgetting-mechanism**: forgetting is *not* erasure of the rule but **displacement** — a competing surface pattern out-competes the rule, with the log-probability margin between them crossing zero within 100 training steps of the behavioral collapse
- **Asymmetric control-of-fate**: the same edit that *destroys* a rule on demand cannot *restore* it — flipping support to counter-evidence kills the rule with monotone dose-response across two unrelated rules, but injecting support back (even to 450× the level that naturally sustains the rule) buys no recovery
- **Pre-registration discipline**: every confirmatory threshold and prediction was pre-registered before the data it governed was read, making this a **negative-result-as-architectural-primitive** paper — the strong claim is what *cannot* be done (restore a rule) rather than what can
- **Framing shift**: pretraining is reframed from "the corpus adds knowledge" to "the corpus **decides** which learned rules to keep" — a corpus-statistics-as-decision-maker primitive that contrasts with the data-construction-as-supervisor view

## Related Papers
- [[early-warning-signals-of-grokking-via-loss-landscape-geometry-2602.16967]] — Sibling from Run 97 that surfaced the loss-landscape-geometry primitive for *grokking* (rule emergence); this paper surfaces the **opposite-direction primitive** (silent rule collapse via displacement within the same run), establishing natural-ungrokking as the displacement-asymmetric counterpart to early-warning-signal grokking
- [[grokking-or-glitching-how-low-precision-drives-slingshot-loss-spikes-2605.06152]] — Sibling from Run 97 that surfaced the floating-point-precision primitive for late-stage loss spikes; both papers probe *hidden instability modes* of pretraining that are invisible in the loss curve, but this paper localizes the hidden mode to **rule-survival decisions driven by corpus statistics** rather than to numerical-precision artifacts
- [[demystifying-training-time-augmentation-for-data-constrained-language-model-pretraining-2606.16246]] — Pretraining-data-intervention sibling; complements the corpus-statistics-as-fate-decider framing here with the data-construction-as-quality-controller framing there
- [[ac-odm-actor-critic-online-data-mixing-for-sample-efficient-llm-pretraining-2505.23878]] — Pretraining-data mixture sibling; both papers surface the data-side primitive but this paper's claim that corpus-frequency *predicts rule fate* reframes data-mixing from a quality tool into a *rule-survival-selection mechanism*
- [[emergent-concepts]] — Parent meta-page for emergent-concept discoveries

## Rule Context
**Rule 65 NEGATIVE-RESULT-AS-PRIMITIVE-PROBE** (Run 98) — first paper in the wiki to probe the **corpus-statistics-as-rule-fate-determinant + asymmetric-recovery-control + displacement-as-forgetting-mechanism** primitive triplet. The wiki previously had grokking primitives (early-warning-signals, low-precision-as-spike-trigger, mechanistic-circuit theories) and pretraining-data primitives (online data mixing, training-time augmentation), but no entity provided the **negative-space account** — what the training process *cannot do* (restore a destroyed rule), the **predictive corpus statistic** that determines rule-survival outcomes, or the **displacement-rather-than-erasure** mechanism for within-run behavioral collapse. Distinct from loss-curve-explained instabilities; this paper reframes pretraining as a *decision-making system about which learned rules to retain*, with the corpus as the silent decider. The pre-registered null result (no recovery) is itself the load-bearing primitive — strong evidence from a controlled study rather than a casual observation.
