---
title: "CLOSER-VLN: Closed-Loop Self-Verified Retrieval-Augmented Reasoning for Aerial Vision-Language Navigation"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [vision-language-navigation, retrieval-augmented-reasoning, aerial-agents, self-verification, multimodal]
sources: ["https://arxiv.org/abs/2606.28397"]
---

# CLOSER-VLN: Closed-Loop Self-Verified Retrieval-Augmented Reasoning for Aerial Vision-Language Navigation

## Overview
CLOSER-VLN addresses the open-loop decision-execution problem in vision-language navigation for aerial (UAV) agents. Existing VLN methods generate candidate actions from instructions and observations but rarely verify or correct them before execution, causing cascading errors in long-horizon navigation tasks. The paper introduces closed-loop self-verified reasoning where the agent validates planned actions against environmental context before committing to them.

## Key Facts
- **Authors**: Shaoxuan Li, Xiangyu Dong, Xiaoguang Ma, Junfeng Chen, Haoran Zhao, Yaoming Zhou
- **Year**: 2026
- **arXiv**: [2606.28397](https://arxiv.org/abs/2606.28397)

## Key Contributions
- Closed-loop self-verified reasoning for aerial vision-language navigation — verify before executing
- Addresses open-loop failure mode: cascading errors from unverified action commitments
- Retrieval-augmented reasoning for VLN — grounding navigation decisions in retrieved context
- Self-verification as a core reasoning primitive, not just action execution
- Unseen environments generalization via reasoning verification rather than task-specific policy training

## Related Papers
- [[emergent-concepts]] — Parent emergent concepts wiki
