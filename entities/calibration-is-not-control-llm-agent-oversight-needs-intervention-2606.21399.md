---
title: "Calibration Is Not Control: Why LLM-Agent Oversight Needs Intervention"
created: 2026-07-01
updated: 2026-07-01
type: entity
tags: [agent-safety, calibration, oversight, llm-agents]
sources: ["https://arxiv.org/abs/2606.21399"]
---

# Calibration Is Not Control: Why LLM-Agent Oversight Needs Intervention

## Overview
Runtime oversight for LLM agents is commonly framed as scalar risk prediction: estimate failure likelihood, confidence, or uncertainty, then intervene once the score crosses a threshold. This paper argues that this framing targets the wrong object for control. The relevant question is not how likely the agent is to fail if it continues, but whether an available intervention would improve the outcome. This shifts the oversight question from "will the agent fail?" to "should I intervene, and how?"

## Key Facts
- **Authors**: Chubin Zhang, Zhenglin Wan, Xingrui Yu, Jingxuan Wu, Qi Wen, Pengfei Zhou, Wangbo Zhao, Ivor Tsang
- **Year**: 2026
- **arXiv**: [2606.21399](https://arxiv.org/abs/2606.21399)

## Key Contributions
- Argues that scalar risk prediction (calibration/uncertainty) is insufficient for runtime LLM-agent oversight — the right question is whether an available intervention would improve the outcome
- Proposes an intervention-centric oversight framework that shifts from failure-probability estimation to cost-benefit analysis of available interventions
- Addresses key failure modes where an agent is unlikely to fail but an intervention would still improve outcome, and where an agent is likely to fail but no available intervention would help
- Demonstrates that calibration metrics (precision-recall on failure) are orthogonal to intervention effectiveness — a well-calibrated overseer can still make poor intervention decisions

## Related Papers
- [[emergent-concepts]] — Parent chain for emergent-concept discoveries
