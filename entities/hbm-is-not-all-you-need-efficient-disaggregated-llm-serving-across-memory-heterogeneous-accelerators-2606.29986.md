---
title: "HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators"
created: 2026-07-04
updated: 2026-07-04
type: entity
tags: [llm, inference-efficiency, agentic-systems]
sources: ["https://arxiv.org/abs/2606.29986"]
---

# HBM Is Not All You Need: Efficient Disaggregated LLM Serving across Memory-heterogeneous Accelerators

## Overview
LLM inference comprises a compute-bound prefill phase and a memory-bound decode phase, and recent systems disaggregate them onto separate hardware. Yet today's datacenter GPUs rely on costly HBM whose bandwidth sits almost entirely idle during prefill. LLM serving across memory-heterogeneous acceler

## Key Facts
- **Authors**: Zhixiang Wei, Yun Wang, James Yen, Mingyuan Xia, Zhengwei Qi
- **Year**: 2026
- **arXiv**: [2606.29986](https://arxiv.org/abs/2606.29986)

## Key Contributions
- LLM inference comprises a compute-bound prefill phase and a memory-bound decode phase, and recent systems disaggregate them onto separate hardware. Yet today's datacenter GPUs rely on costly HBM whose bandwidth sits almost entirely idle during prefill. LLM serving across memory-heterogeneous accelerators (MemHA) pairs GDDR-based accelerators for prefill with HBM-based GPUs for decode, promising lower cost without sacrificing performance. We present HMA-Serve, a MemHA-centric disaggregated servin

## Related Papers
- [[emergent-concepts]] — Parent discovery chain for emergent LLM-research papers
