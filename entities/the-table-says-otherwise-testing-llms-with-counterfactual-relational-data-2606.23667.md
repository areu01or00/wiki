---
title: "The Table Says Otherwise: Testing LLMs with Counterfactual Relational Data"
created: 2026-06-29
updated: 2026-06-29
type: entity
tags: [counterfactual-reasoning, relational-reasoning, llm-faithfulness, table-qa]
sources: ["https://arxiv.org/abs/2606.23667"]
---

# The Table Says Otherwise: Testing LLMs with Counterfactual Relational Data

## Overview
ContraTable is a paired original-counterfactual benchmark for evaluating whether LLMs ground their answers in provided relational tables rather than relying on pretraining knowledge. It pairs real-world databases with counterfactual versions that preserve schemas and relationships while changing selected country, club, and player attributes. Experiments on commercial and open-source models reveal that models often fall back on prior knowledge when table evidence conflicts with familiar facts, establishing that table-QA evaluation must measure not only accuracy but also faithfulness to the provided database.

## Key Facts
- **Authors**: Xinzhi Wang, Chunwei Liu
- **Year**: 2026
- **arXiv**: [2606.23667](https://arxiv.org/abs/2606.23667)
- **Subjects**: Databases (cs.DB)
- **Submitted**: 22 June 2026

## Key Contributions
- **ContraTable benchmark**: 214 matched questions across three levels — single-table lookup, multi-table lookup, and multi-table temporal reasoning — with paired original and counterfactual databases
- **Faithfulness evaluation gap**: Demonstrates systematic accuracy-faithfulness divergence: strong instruction-tuned models handle direct lookup but reliability drops as questions require joins, comparison, and temporal reasoning
- **Schema-preserving counterfactual construction**: Counterfactual databases preserve schemas, identifiers, and relationships while changing specific factual attributes, enabling controlled evaluation
- **Practical implication**: Table-QA evaluation should measure both accuracy and faithfulness to the provided database, not just accuracy alone
- **First counterfactual relational QA benchmark in the wiki**: Introduces the counterfactual-evaluation methodology to table-QA, complementing entity-substitution counterfactual approaches in RAG faithfulness

## Related Papers
- [[faithfulness-qa-a-counterfactual-entity-substitution-dataset-for-training-context-faithful-rag-models-2604.25313]] — Counterfactual entity substitution for RAG faithfulness; ContraTable extends this methodology from text retrieval to structured relational data with schema-preserving counterfactuals
- [[chartwalker-benchmarking-the-cross-chart-rag-task-with-hierarchical-knowledge-graphs-2606.23997]] — Cross-chart RAG evaluation; ContraTable provides the relational table counterpart for structured data faithfulness evaluation
- [[liberty-a-causal-framework-for-benchmarking-concept-based-explanations-of-llms-with-structural-counterfactuals-2601.10700]] — Causal framework with structural counterfactuals for LLM explanations; ContraTable operationalizes counterfactual faithfulness testing in the concrete domain of relational database querying
