---
title: "Don't Blindly Trust It: How Unreliable Feedback Breaks Tool-Using LLM Agents"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [llm-agent, tool-using, feedback-reliability, value-inversion, controlled-comparison, agent-evaluation]
sources: ["https://arxiv.org/abs/2606.21409"]
---

# Don't Blindly Trust It: How Unreliable Feedback Breaks Tool-Using LLM Agents

## Overview
Investigates whether the gains tool-augmented agents achieve under reliable external feedback persist — or invert — when feedback is unreliable, via a controlled matched-loop comparison that fixes the agent loop, prompt, action space, and decoding while varying only the returned observation: faithful, misleading, or absent. Across question answering and fact verification, persistent misleading feedback produces a value inversion — agents that benefit from clean tools can perform worse than agents receiving no task evidence at all — surfacing *feedback-reliability-as-deployment-condition* as a load-bearing primitive for tool-using LLM-agent evaluation.

## Key Facts
- **Authors**: Zhang, Chubin; Wan, Zhenglin; Yu, Xingrui; Zhou, Pengfei; Zhao, Wangbo; et al. (8 authors)
- **Year**: 2026
- **Date**: 2026-06-19
- **arXiv**: [2606.21409](https://arxiv.org/abs/2606.21409)
- **Categories**: cs.CL, cs.AI, cs.LG

## Key Contributions
- Controlled matched-loop comparison isolating the *only* variable of feedback reliability (faithful / misleading / absent), revealing that the structural agent gains under clean tools reverse into *value inversion* under persistent misleading feedback — the agent would have been better off receiving no task evidence.
- Surfaces *feedback-reliability-as-deployment-condition* as the structurally important primitive: tool-using-agent evaluation must characterize the feedback regime, not just the tool accuracy, because the same tool capability can yield opposite rankings under different feedback distributions.
- Methodology-level contribution to agent evaluation — the matched-loop design (fix everything except the observation) provides a clean diagnostic primitive for separating tool-capability from feedback-integration pathologies, applicable beyond the Q&A/fact-verification surface to any tool-using agent deployed against an unreliable external source.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this discovery was logged
- [[constraint-tax-in-open-weight-llms-an-empirical-study-of-tool-calling-suppression-under-structured-output-constraints-2606.25605]] — Sibling tool-calling work: Constraint-Tax diagnoses tool-calling failures under output constraints, Feedback-Reliability diagnoses tool-using failures under unreliable observations — together they bracket the tool-use failure-mode space between structural-output-pathology and observation-reliability-pathology
- [[foresight-failure-detection-long-horizon-robotic-manipulation-2606.23085]] — Sibling deployment-monitoring work: Foresight uses world-model latents to detect manipulation failures, Feedback-Reliability diagnoses a different failure class — *not* detecting that an observation is misleading rather than faithful — surfacing the unmonitored-but-correctable primitive that complements failure detection
- [[calvert-augmenting-agents-with-calibrated-verifier-telemetry-improves-action-and-learning-in-knowledge-intensive-tasks-2606.21777]] — Sibling verifier-telemetry work: CALVERT calibrates verifier feedback signals to improve agent learning, Feedback-Reliability demonstrates what happens when those verifier signals are themselves unreliable — the two together bracket verifier-integrity as the structural axis