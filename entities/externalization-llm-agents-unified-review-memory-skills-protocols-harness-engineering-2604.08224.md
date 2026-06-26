---
title: "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering"
created: 2026-06-26
updated: 2026-06-26
type: entity
tags: [survey, llm-agent, externalization, infrastructure, memory, skills, protocols, harness]
sources: ["https://arxiv.org/abs/2604.08224"]
---

# Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering

## Overview

Zhou, Chenyu; Chai, Huacan; Chen, Wenteng; Guo, Zihan; Shan, Rong; Song, Yuanyi; Xu, Tianyi; Yang, Yingxuan; Yu, Aofan; Zhang, Weiming; Zheng, Congming; Zhu, Jiachen; Zheng, Zeyu; Zhang, Zhuosheng; Lou, Xingyu; Zhang, Changwang; Fu, Zhihui; Wang, Jun; Liu, Weiwen; Lin, Jianghao; Zhang, Weinan (21 authors) propose **externalization** as the load-bearing primitive for understanding practical LLM-agent progress: instead of changing model weights to acquire new capability, current systems relocate cognitive burden into memory stores, reusable skills, interaction protocols, and the surrounding harness — transforming problems the model cannot reliably solve internally into forms it can solve more reliably. Under this lens, **memory externalizes state across time, skills externalize procedural expertise, protocols externalize interaction structure, and harness engineering serves as the unification layer** that coordinates the three. The review traces a historical progression from weights to context to harness, treats memory / skills / protocols as three coupled externalization forms, and surfaces self-evolving harnesses and shared agent infrastructure as emerging directions.

## Key Facts

- **Authors**: Zhou, Chenyu; Chai, Huacan; Chen, Wenteng; Guo, Zihan; Shan, Rong; Song, Yuanyi; Xu, Tianyi; Yang, Yingxuan; Yu, Aofan; Zhang, Weiming; Zheng, Congming; Zhu, Jiachen; Zheng, Zeyu; Zhang, Zhuosheng; Lou, Xingyu; Zhang, Changwang; Fu, Zhihui; Wang, Jun; Liu, Weiwen; Lin, Jianghao; Zhang, Weinan
- **Year**: 2026
- **Date**: 2026-04-09
- **arXiv**: [2604.08224](https://arxiv.org/abs/2604.08224)
- **Survey / unified-review format**

## Key Contributions

- Articulates **externalization** as the unifying primitive for LLM-agent infrastructure: capabilities are relocated out of the model and into runtime artifacts, transforming hard cognitive burdens into forms the model can solve more reliably
- Frames memory, skills, protocols, and harness engineering as **three coupled forms of externalization** plus one coordination layer — a clean 4-way decomposition rather than ad-hoc per-system taxonomies
- Traces a historical **weights → context → harness** progression showing the field's center of gravity has moved from parameter change to runtime reorganization
- Surfaces the **parametric-vs-externalized capability trade-off** as a load-bearing design tension, with implications for evaluation, governance, and long-term model-infrastructure co-evolution
- Identifies **self-evolving harnesses** and **shared agent infrastructure** as emerging directions — i.e., infrastructure that updates itself based on observed agent behavior
- First systems-level framework in the wiki that explicitly reframes agent progress as **better external cognitive infrastructure** rather than **stronger models**

## Related Papers

- [[are-we-ready-for-an-agent-native-memory-system-2606.24775]] — companion memory-systems survey from a data-management perspective (Run 46 sibling: same memory-as-infrastructure angle but framed through DB/KG/OS hierarchies)
- [[agent-memory-characterization-and-system-implications-of-stateful-long-horizon-workloads-2606.06448]] — systems-level 4-axis taxonomy of agent memory (Run 41)
- [[memory-is-reconstructed-not-retrieved-graph-memory-llm-agents-2606.06036]] — graph-conditioned memory reconstruction (Run 45)
- [[agent-skill-evaluation-and-evolution-frameworks-benchmarks-2606.11435]] — four-paradigm survey of agent skill evaluation (Run 43)
- [[a-technical-taxonomy-of-llm-agent-communication-protocols-2606.19135]] — agent communication-protocol taxonomy (Run 38)
- [[skillharness-harnessing-safe-skills-computer-use-agents-2606.20636]] — concrete instance of harness-as-unification-layer for computer-use safety (Run 40)
- [[aohp-an-open-source-os-level-agent-harness-for-personalized-efficient-and-2606.23449]] — OS-level agent harness as externalization infrastructure
- [[opid-on-policy-skill-distillation-for-agentic-reinforcement-learning-2606.26790]] — on-policy skill distillation conditioned on self-acquired skills (Run 44)
- [[memtoolagent-leveraging-memory-tool-using-agents-environment-user-feedback-2606.07909]] — tool-use memory mechanism (Run 40)
- [[notes2skills-from-lab-notebooks-to-certainty-aware-scientific-agent-skills-2606.11897]] — certainty-aware skill distillation
- [[openrath-session-centered-runtime-state-for-agent-systems-2606.19409]] — runtime state as externalization surface (Run 27)
- [[gatemem-benchmarking-memory-governance-in-multi-principal-shared-memory-agents-2606.18829]] — multi-principal memory governance (Run 27)
- [[memprobe-probing-longterm-agent-memory-via-hidden-userstate-recovery-2606.24595]] — long-term agent memory via hidden userstate recovery
- [[evoembedding-evolvable-representations-for-long-context-retrieval-and-agentic-memory-2606.21649]] — evolvable representations for agentic memory
- [[evoarena-tracking-memory-evolution-robust-llm-agents-dynamic-environments-2606.13681]] — memory evolution under dynamic environments