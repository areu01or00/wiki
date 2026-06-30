---
title: "Linguistic Firewall: Geometry as Defense in Multi-Agent Systems Routing"
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [multi-agent, routing, adversarial, safety]
sources: ["https://arxiv.org/abs/2606.30555"]
---

# Linguistic Firewall: Geometry as Defense in Multi-Agent Systems Routing

## Overview
This paper identifies a geometric vulnerability in LLM-based multi-agent routing: adversaries can exploit geometric positioning in embedding space to manipulate task routing, causing agents to misroute to compromised nodes. The authors propose "Linguistic Firewall" — a geometric defense that uses angular distance thresholds and projection-based detection to identify and block malicious routing signals before they reach downstream agents.

## Key Facts
- **Authors**: Dvir Alsheich, Adar Peleg, Ben Hagag, Rom...
- **Year**: 2026
- **arXiv**: [2606.30555](https://arxiv.org/abs/2606.30555)

## Key Contributions
- Identifies geometric routing attacks as a novel attack surface in LLM-based multi-agent systems where adversarial nodes can bias task routing via embedding-space positioning
- Proposes Linguistic Firewall using angular distance thresholds and projection-based detection against malicious routing signals
- Evaluates against 5 agentic frameworks (AutoGen, CrewAI, LangChain, CAMEL, MetaGPT) showing the attack succeeds in 89% of cases without the defense

## Related Papers
- [[emergent-concepts]] — Parent discovery chain for emergent-concept discoveries
