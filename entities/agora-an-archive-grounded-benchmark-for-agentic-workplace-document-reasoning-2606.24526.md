---
title: "AGORA: An Archive-Grounded Benchmark for Agentic Workplace Document Reasoning"
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [benchmark, agents, document-reasoning, evaluation, llm-research]
sources: ["https://arxiv.org/abs/2606.24526"]
---

# AGORA: An Archive-Grounded Benchmark for Agentic Workplace Document Reasoning

## Overview
AGORA is a benchmark for *archive-grounded* agentic document reasoning — locating sparse evidence across large, messy collections of workplace files, reconciling inconsistent terminology, units, and time conventions, and computing a final answer under realistic context-window pressure. It pairs 362 questions with eight domain collections totaling 9,664 authentic documents and 372M tokens (far exceeding any model's context window), forcing agents to explore deliberately rather than scan exhaustively. Guo et al. build AGORA via an agentic pipeline that combines cross-document task synthesis, leakage-preventing obfuscation, and difficulty filtering; evaluating eight models, they find even the strongest reaches only 59.4% accuracy with notable variation across domains.

## Key Facts
- **Authors**: Guo, Honglin; Zhang, Qi; Zhang, Yu; Li, Weijie; Zheng, Rui; Lei, Zhikai; Peng, Qiyuan; Xi, Zhiheng; Gui, Tao; Zhang, Qi
- **Year**: 2026
- **Date**: 2026-06-23
- **arXiv**: [2606.24526](https://arxiv.org/abs/2606.24526)
- **Subjects**: Computation and Language (cs.CL)

## Key Contributions
- Defines *archive-grounded reasoning* as a benchmark setting: locating sparse evidence across messy multi-document archives, reconciling terminology / unit / time inconsistencies, and computing a final answer — distinct from parametric-knowledge QA or single-document RAG.
- 362 questions paired with 9,664 authentic workplace documents across 8 domains, totaling 372M tokens — deliberately exceeding all current model context windows to force exploration.
- Agentic benchmark-construction pipeline: cross-document task synthesis, leakage-preventing obfuscation (preventing parametric-memory leakage), and difficulty filtering — a methodology reusable for future agent benchmarks.
- Evaluation of 8 frontier models yields a 59.4% ceiling accuracy, demonstrating the task is far from solved, with substantial cross-domain variation that the authors attribute to differences in archive structure rather than question difficulty.

## Related Papers
- [[emergent-concepts]] — Parent meta-page where this was discovered; complements the Agents' Last Exam and tool-calling-suppression entries on this page by surfacing the *document-reasoning* axis of agentic capability — a workload where the bottleneck is sparse-evidence location and reconciliation, not parametric knowledge.