---
title: "GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [computer-use-agent, benchmark, interaction-modality, matched-benchmark, evaluation-methodology]
sources: ["https://arxiv.org/abs/2606.24551"]
---

# GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents

## Overview

Zhou, Xiao; Zhang, Siyue; Zhao, Yilun; Wei, Jinbiao; Song, Tingyu; Cohan, Arman; Zhao, Chen observe that **computer-use agent evaluations routinely confound interaction modality with task difficulty, initial states, verifiers, and permitted actions** — making it impossible to tell whether a CLI agent's lower success rate is due to model capability or due to differences in task structure, environment setup, or verifier behavior. They introduce a **matched execution-layer benchmark of 440 desktop tasks across 18 applications and 12 workflow categories** where screen-only GUI agents and skill-mediated CLI agents receive identical goals, states, and final-state verifiers while being restricted to modality-native actions, isolating the interaction-modality variable cleanly. The headline finding inverts the naive expectation: the strongest GUI agent reaches **59.1% full pass rate vs the strongest original-skill CLI agent at 48.2%**, but **verifier-guided skill augmentation raises CLI success to 69.3%** — showing that much of the CLI deficit comes from incomplete skill coverage rather than model capability, surfacing *modality-native-bottleneck-isolation* as the load-bearing evaluation primitive for computer-use agent research.

## Key Facts
- **Authors**: Zhou, Xiao; Zhang, Siyue; Zhao, Yilun; Wei, Jinbiao; Song, Tingyu; Cohan, Arman; Zhao, Chen
- **Year**: 2026
- **Date**: 2026-06-22
- **arXiv**: [2606.24551](https://arxiv.org/abs/2606.24551)

## Key Contributions
- Identifies the **interaction-modality-confound pathology** in computer-use-agent evaluation — where existing benchmarks mix modality differences with task/verifier/permitted-action differences, making modality-vs-capability conclusions scientifically meaningless
- Introduces a **matched execution-layer benchmark of 440 desktop tasks across 18 applications and 12 workflow categories** where GUI and CLI agents receive identical goals, states, and final-state verifiers while being restricted to modality-native actions — the matched-control design isolates the modality variable cleanly
- Demonstrates that **GUI agents win on raw capability (59.1% vs 48.2%)** but **CLI agents win after verifier-guided skill augmentation (69.3%)** — inverting the naive modality ranking and showing that the apparent CLI deficit was largely a skill-coverage gap rather than a model-capability gap
- Surfaces the **modality-specific bottleneck diagnosis** — GUI agents are limited by reliable grounded interaction over long-horizon workflows, whereas CLI agents are limited by the coverage and scalability of their skill interfaces — making the structural axis of *which bottleneck dominates* a first-class evaluation dimension
- Demonstrates that **skill coverage, not model capability, is the binding constraint for CLI agents** under matched-control conditions — a counter-intuitive empirical finding enabled only by the matched-modality design
- First paper in the wiki that introduces **interaction-modality-as-isolated-variable** for computer-use-agent evaluation, distinct from Run 37's Beyond-Static-Leaderboards (which argues aggregate scoring is structurally inadequate — this paper isolates modality as a concrete isolated variable the field has been confounding)

## Related Papers
- [[beyond-static-leaderboards-predictive-validity-evaluation-llm-agents-2606.19704]] — Run 37 sibling: aggregate-scoring pathology critique (different methodology axis — Beyond-Static-Leaderboards critiques the scoring surface, GUI-vs-CLI isolates the modality variable)
- [[capable-but-careless-do-computer-use-agents-follow-contextual-integrity-2606.23189]] — CUA contextual-integrity compliance (different CUA safety surface — execution-time rule-following, GUI-vs-CLI isolates modality-specific bottlenecks)
- [[skillharness-harnessing-safe-skills-computer-use-agents-2606.20636]] — CUA safe-skill harness (different CUA design axis — SkillHarness is safety gating, GUI-vs-CLI is modality isolation)
- [[planbench-xl-evaluating-long-horizon-planning-of-llm-tool-use-agents-in-large-scale-tool-ecosystems-2606.22388]] — long-horizon planning evaluation for tool-use agents (different evaluation surface — PlanBench-XL is long-horizon planning, GUI-vs-CLI is modality-isolated task completion)
- [[ebench-elemental-diagnosis-of-generalist-mobile-manipulation-policies-2606.18239]] — multi-axis diagnostic for manipulation policies (different evaluation methodology — EBench decomposes capability dimensions, GUI-vs-CLI isolates a single matched variable)
- [[oragentbench-can-llm-agents-solve-challenging-operations-research-tasks-end-to-end-2606.19787]] — Run 38 sibling: execution-grounded OR benchmark (different domain — ORAgentBench is OR-specific execution, GUI-vs-CLI is modality-matched desktop execution)
- [[emergent-concepts]] (parent wiki page) — meta-cluster for emergent-concept paper discoveries