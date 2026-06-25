---
title: "PhoneBuddy: Training Open Models for Agentic Phone Use"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [agents, mobile, phone-use, training-data, open-models, llm]
sources: ["https://arxiv.org/abs/2606.23049"]
---

# PhoneBuddy: Training Open Models for Agentic Phone Use

## Overview
PhoneBuddy targets the gap between closed-API agentic-phone-use demos and reproducible open-model training for the same task. The paper argues that the deployment environment for phone-use agents is the *real* Android/iOS surface, not a sandbox, and constructs training data + trajectories that mirror the constraints of that environment. The contribution is a full open recipe — data pipeline, training procedure, and evaluation protocol — for getting an open model to perform reliable phone-use tasks that are usually the provenance of closed frontier systems.

## Key Facts
- **Authors**: Tang, Zhengyang; Lai, Xin; Lyu, Pengyuan; Wang, Xinyuan; Bai, Tianyi; Li, Chenxin; Guo, Yiduo; Shen, Huawen; Liu, Yuxuan; Li, Junyi; Fang, Zhengyao; Ding, Yang; Zhang, Yi; Wang, Weinong; Zhou, Xingran; Wu, Liang; Tang, Fei; Fan, Sunqi; Peng, Shangpin; Ruan, Zheng; Zhang, Anran; Wang, Benyou; Wen, Ji-Rong; Yan, Rui; Zhang, Chengquan; Hu, Han
- **Year**: 2026 (revised 2026-06-22)
- **arXiv**: [2606.23049](https://arxiv.org/abs/2606.23049)
- **Subjects**: cs.CL

## Key Contributions
- Constructs a phone-use training dataset and trajectory set that mirrors real-device constraints (UI state, app boundaries, network latency) rather than sandbox approximations.
- Provides an open training recipe and benchmark for phone-use agents, lowering the bar for open-model replication of a capability that has been dominated by closed-API demos.
- Demonstrates that open models can be trained to perform reliable phone-use tasks with careful data design, closing part of the open/closed gap on this specific agent surface.
- Establishes evaluation methodology for phone-use that emphasizes end-to-end task completion rather than UI-element click accuracy.

## Related Papers
- [[emergent-concepts]] — Parent meta-chain page; this paper was discovered via emergent-concept search on 2026-06-25 as a fresh 2026 contribution to LLM agents / mobile-deployment training data.