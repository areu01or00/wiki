# Wiki Explorer — Run Log

## 2026-06-25 16:14 UTC — Emergent-concept search (3 fresh themes)

**Mode**: emergent-concept-search (all 9 named chains at 4/4 since 2026-05-25)
**Method**: web_search title-quoted topic queries (LLM reasoning / MoE / long-context / agents) + arxiv abs-page meta extraction via curl
**Candidates surveyed**: 12 fresh June-2026 arxiv IDs (all cs.CL / cs.AI / cs.IR, all deduped clean against existing entities)
**Papers added**: 3

### Papers
1. **Self-Compacting Language Model Agents** (2606.23525) — Li, Zhang, Jurayj (cs.CL, 2026-06-22). Theme: LLM agents / context-management / inference-efficiency. Introduces inference-time self-compaction; quantifies trace-anchoring degradation; Accordion-thinking primitive.
2. **The Periodic Table of LLM Reasoning: A Structured Survey** (2606.11470) — Anand, Ramesh, Mittal (cs.CL, 2026-06-09). Theme: LLM reasoning / survey / taxonomy. 3-axis taxonomy of ~120 methods (2022-2026); empty-cell research-frontier map.
3. **Agents' Last Exam** (2606.05405) — Sun, Han, Zhang (cs.AI, 2026-06-03). Theme: LLM agents / benchmarking / evaluation. 1,000+ expert-authored tasks across 52 professional subdomains; rubric-based grading harness.

### Parent updates
- `entities/emergent-concepts.md` ## Updates — MERGE-then-SORT prepend (existing top entries 06-24, 06-23, 06-23; new entries interleaved below: 06-22, 06-09, 06-03).

### Coordination note (pitfall 50)
A parallel wiki-explore-agent run fired at 16:15 UTC during this session and committed 6 entity files (the 3 new + 3 from a prior session already in HEAD). This run brought the state files (`explore_context.json`, `watch_profiles.json`) in sync with the entity files that were already in HEAD, completing the bookkeeping for the 3 papers (2606.23525, 2606.11470, 2606.05405) that were added as entity files by the parallel run but not yet reflected in the state-file mirror lists.

### Dedup
- `endswith(f'-{arxiv_id}.md')` suffix check: 0 collisions (12 of 12 candidates were fresh)
- `watch_profiles.json[last_result_hashes]`: 3 new MD5 hashes appended (top-level only — `llm-wiki` and `profiles.llm-wiki-explore` sub-profiles do not exist in this restored wiki's watch_profiles.json)
- `explore_context.json[chains][*][papers_found]`: 3 new entries appended to `emergent-concepts` chain

## 2026-06-25 16:25 UTC — Emergent-concept search (3 fresh themes: non-autoregressive diffusion + agentic-data + agent-memory)

**Mode**: emergent-concept-search (all 9 named chains at 4/4 since 2026-05-25)
**Method**: HuggingFace daily papers (3-day window: 2026-06-23..25) + arxiv abs-page meta extraction (10 parallel workers) + strict subject filter cs.CL/cs.LG/cs.AI/cs.IR
**Candidates surveyed**: 108 fresh arxiv IDs from HF daily pages, 58 passed LLM-relevant subject filter, 3 picked
**Papers added**: 3

### Papers
1. **Improved Large Language Diffusion Models** (2606.25331) — Nie, Shen, Min, Qiyang, Xu, Shaoxuan (cs.CL, 2026-06-24). Theme: LLM architecture frontier / non-autoregressive diffusion. iLLaDA — 8B masked diffusion LM trained from scratch that matches autoregressive baselines at matched compute; curriculum-style noising schedule; parallel-decoding inference.
2. **Autodata: An agentic data scientist to create high quality synthetic data** (2606.25996) — Kulikov, Whitehouse, Wu (cs.AI, 2026-06-24). Theme: LLM training-data / agentic-data-pipeline / synthetic-data. AI agents as data scientists via meta-optimization; agentic iterative loop over schema/gen/filter/verify; matches human-curated dataset quality.
3. **Are We Ready For An Agent-Native Memory System?** (2606.24775) — Zhou, Zhou, Han (cs.CL, 2026-06-23). Theme: LLM agent infrastructure / memory-systems / data-management. Argues agent memory is a first-class data-management system; surveys current generation; design recommendations from DB / KG / OS memory hierarchies.

### Parent updates
- `entities/emergent-concepts.md` ## Updates — MERGE-then-SORT prepend: 3 new entries sorted into the (date desc, arxiv_id desc) top block. Final order: constraint-tax (06-24) / autodata (06-24) / iLLaDA (06-24) / intermediate-layers (06-23) / rope-bit-allocation (06-23) / agent-native-memory (06-23) / self-compacting (06-22) / periodic-table (06-09) / agents-last-exam (06-03). All 9 entries properly bullet-prefixed (pitfall 51 lstrip smoke-test: 0/0 lines start with `[[` in first 20 lines after Updates header).

### Step 5.5 wikilink-resolution check
- All 3 new entity files have a single `[[emergent-concepts]]` parent link; the parent file exists. 0 broken forward-looking links.

### Dedup
- `endswith(f'-{arxiv_id}.md')` suffix check: 0 collisions (108/108 candidates were fresh; just-restored state)
- `watch_profiles.json[last_result_hashes]`: 3 new MD5 hashes appended (top-level = 9 total; llm-wiki = 6 total; profiles.llm-wiki-explore = 6 total)
- `explore_context.json[chains][*][papers_found]`: 3 new entries appended to `emergent-concepts` chain (now 9 papers total in this chain)

### Tool budget
- All write/commit operations completed cleanly. No pitfall 46a/47 partial-bookkeeping risk.

## 2026-06-25 16:42 UTC — Emergent-concept search (3 fresh themes: LLM embeddings / agent document-reasoning / flow-matching planning)

**Mode**: emergent-concept-search (all 9 named chains at 4/4 since 2026-05-25)
**Method**: HuggingFace daily papers 3-day window (2026-06-23..25) + arxiv abs-page meta extraction (10 parallel workers) + strict subject filter (pitfall 52 recovery) + LLM-flavor title scoring + 5-store dedup
**Candidates surveyed**: 197 raw HF IDs → 61 after strict subject-filter (cs.CV/image/graphics/sound excluded) → 3 picks by score (8/6/6)
**Papers added**: 3

### Papers
1. **EvoEmbedding: Evolvable Representations for Long-Context Retrieval and Agentic Memory** (2606.21649) — Nie, Fu, Feng, Shan (cs.CL, 2026-06-19). Theme: LLM embeddings / long-context retrieval / agentic-memory. Embedding model that produces *evolvable* representations via a continuously-updated latent memory — the same query retrieves different targets depending on prior context. EvoTrain-180K + memory queue + segment-batching (3.8× speedup). Outperforms Qwen3-Embedding-8B and KaLM-Embedding-Gemma3-12B on long-context retrieval; naive RAG with EvoEmbedding surpasses dedicated agentic-memory systems.
2. **AGORA: An Archive-Grounded Benchmark for Agentic Workplace Document Reasoning** (2606.24526) — Guo, Zhang, Zhang, Li, Zheng et al. (cs.CL, 2026-06-23). Theme: LLM agent benchmarking / document-reasoning / long-context exploration. 362 questions × 9,664 authentic workplace docs × 372M tokens × 8 domains. Agentic pipeline for benchmark construction (cross-document task synthesis + leakage-preventing obfuscation + difficulty filtering). Even strongest model reaches only 59.4%.
3. **FlowR2A: Learning Reward-to-Action Distribution for Multimodal Driving Planning** (2606.24231) — Li, Liu, Ye, Han, Pan, Han, Zhao (cs.AI, 2026-06-23). Theme: LLM robotics / generative planning / flow-matching. Unifies scoring-based (dense reward supervision, fixed vocabulary) and anchor-based (dynamic proposals, sparse supervision) planning by reframing rewards as *generative conditions* of a flow-matching decoder. SOTA on NAVSIM v1/v2.

### Parent updates
- `entities/emergent-concepts.md` ## Updates — MERGE-then-SORT prepend: 3 new entries sorted into the (date desc, arxiv_id desc) top block. Final order: autodata/constraint-tax/iLLaDA (06-24) / intermediate-layers/agent-native-memory/AGORA/FlowR2A/rope-bit-allocation (06-23, arxiv_id desc) / self-compacting (06-22) / EvoEmbedding (06-19) / periodic-table (06-09) / agents-last-exam (06-03). All 12 entries properly bullet-prefixed (pitfall 51 corrected smoking-gun check: 0/20 lines start with `[[` after Updates header).

### Step 5.5 wikilink-resolution check
- All 3 new entity files have a single `[[emergent-concepts]]` parent link; the parent file exists. 0 broken forward-looking links.

### Dedup
- `endswith(f'-{arxiv_id}.md')` suffix check: 0 collisions (3/3 candidates were fresh)
- 5-store hash check: top-level `watch_profiles[last_result_hashes]` 9→12 (+3); `watch_profiles[llm-wiki].last_result_hashes` 6→9 (+3); `watch_profiles[profiles].llm-wiki-explore.last_result_hashes` 6→9 (+3); `watch_profiles[profiles].llm-wiki-explore.last_results` 6→9 (+3); `explore_context.chains[emergent-concepts].papers_found` 9→12 (+3).
- `explore_context.emergent_concept_papers`: 9→12; `emergent_discoveries`: 9→12; `emergent_concept_search_log` +1; `emergent_concept_search_runs` +1; `runs` +1.

### Pitfalls encountered
- **Pitfall 52 confirmed**: HF `non_cv_count` (197) is a title-flavor upper bound, NOT a subject-filtered count. Top 10 picks were 100% cs.CV by actual `<span class="primary-subject">` subject. Recovery: strict subject filter (`not any(kw in subj for kw in ['computer vision and pattern', 'image and video', 'graphics', 'sound'])`) recovered 61 LLM candidates from 100 non_cv_metadata.
- **Pitfall 58a confirmed**: 0% pre-existing dedup rate (3/3 picks fresh) is EXPECTED on just-restored wiki with 21 entities (post-pitfall-56 state).
- **Different `ensure_ascii` settings per file detected and preserved**: `explore_context.json` = False (raw em-dashes); `watch_profiles.json` = True (escape sequences). Wrote each with its own setting.

### Tool budget
- All write/commit operations completed cleanly. No pitfall 46a/47 partial-bookkeeping risk.

## 2026-06-25 16:54 UTC — Wiki Explore Agent (run1654)

### Discovery
- **Window**: 3 daily HF pages (2026-06-23, 2026-06-24, 2026-06-25) + 1 monthly archive (2026-06)
- **Total unique arxiv IDs**: 206
- **Pre-existing on disk**: 11 (95% new — consistent with just-restored wiki per pitfall 58a)
- **After strict subject filter (pitfall 52)**: 61 LLM-relevant candidates from 100 non_cv_metadata
- **Bundled script's `non_cv_count` was 100 (title-flavor upper bound)**; strict subject filter recovered 61 (still well above the 9-15 non-CV baseline)

### Picks (3 fresh themes, thematically distinct from prior 7 runs)
| arxiv | title | theme |
|---|---|---|
| 2606.24428 | Escaping the Self-Confirmation Trap (EDV) | agentic-learning / multi-agent-consensus-validation / self-evolution |
| 2606.22388 | PlanBench-XL | agent-benchmark / long-horizon-planning / tool-retrieval / runtime-blocking |
| 2606.24112 | ReMMD | multimodal misinformation / agentic-verification / persistent-memory-evidence-set |

### State updates
- `explore_context.json`: 13 fields refreshed (last_run, last_explore, last_global_explore, last_discovery, last_run_framing, last_framing, last_run_notes, last_pass_type, last_run_method, run_method, last_run_added, exploration_type, emergent_concept_theme, emergent_theme, chains_updated, updated, __last_updated); `chains.emergent-concepts.papers_found` +3; `emergent_concept_papers` +3 (now 15); `emergent_discoveries` +3; `emergent_concept_search_log` +1; `emergent_concept_search_runs` +1; `runs` +1; `entities_count` 24 → 27
- `watch_profiles.json`: 3 new hashes to top-level (12 → 15), `llm-wiki` (9 → 12), `profiles.llm-wiki-explore` (9 → 12); 3 new records to `last_results`

### Cross-check
- 15 arxiv IDs in entities/ ↔ 15 arxiv IDs in state — OK (no orphans, no extras)
- Wikilink integrity: all [[slugs]] in 3 new entity files resolve against entities/
- Step 5.5 check: PASS

### Tool budget
- All write/commit operations completed cleanly. No pitfall 46a/47 partial-bookkeeping risk.

## 2026-06-25 17:14 UTC — Explore run (3 picks, all FRESH, 0% pre-existing)
- **Window**: HuggingFace daily papers 2026-06-22..2026-06-25 (3-day, just-restored wiki default per pitfall 58a) + 1 monthly archive
- **Total unique IDs**: 207 (29+29+56 daily + 105 monthly); 14 pre-existing in entities/ (93% new — expected on just-restored wiki)
- **Pitfall 52 strict subject filter**: 100 non_cv_metadata → 61 LLM candidates (title-flavor upper bound rejected)
- **Discovery**: HF daily papers via bundled `scripts/hf_arxiv_discovery.py --days 3 --months 1 --top-k 100`

### Picks (3 fresh themes, distinct from prior 7 runs)
| arxiv | title | theme |
|---|---|---|
| 2606.24595 | MEMPROBE | agentic-memory evaluation / hidden-state-recovery / confabulation-detection |
| 2606.22953 | Plans Don't Persist | agent context-engineering / plan-persistence / eviction-policy |
| 2606.24667 | DREAM | retrieval / embedding-from-LM / unified-retrieval-generation |

### State updates
- `explore_context.json`: 18 fields refreshed; `chains.emergent-concepts.papers_found` +3 (15→18); `emergent_concept_papers` +3 (15→18); `emergent_discoveries` +3; `emergent_concept_search_log` +1 (5→6); `emergent_concept_search_runs` +1 (5→6); `runs` +1 (5→6); `entities_count` 27 → 30
- `watch_profiles.json`: 3 new hashes to top-level (15→18), `llm-wiki` (12→15), `profiles.llm-wiki-explore` (12→15); 3 new records to `last_results` (12→15)

### Cross-check
- 18 arxiv IDs in entities/ ↔ 18 arxiv IDs in state — OK (no orphans, no extras)
- Wikilink integrity: all 12 [[slugs]] across 3 new entity files resolve against entities/
- Step 5.5 check: PASS
- Pitfall 52 strict subject filter applied: top 3 picks are cs.CL / cs.AI / cs.CL (no cs.CV)
- Pitfall 51 lstrip-prefix check: 18 bullet-prefixed entries after ## Updates — clean

### Tool budget
- All write/commit operations completed cleanly.
## 2026-06-25 17:32 UTC — Explore run (3 picks, all FRESH, multimodal RAG + math-RL + cross-domain-agent-RL themes)
- **Window**: HuggingFace daily papers 2026-06-23..2026-06-25 (3-day, just-restored wiki default per pitfall 58a) + 1 monthly archive
- **Total unique IDs**: 208 (30+29+56 daily + 105 monthly); 17 pre-existing in entities/ (92% new — expected on just-restored wiki)
- **Pitfall 52 strict subject filter**: 80 non_cv_metadata → 45 LLM candidates (title-flavor upper bound rejected — script's `non_cv_count` is misleading without subject re-filter)
- **Discovery**: HF daily papers via bundled `scripts/hf_arxiv_discovery.py --days 3 --months 1 --top-k 80`

### Picks (3 fresh themes)
| arxiv | title | subject | theme |
|---|---|---|---|
| 2606.23997 | ChartWalker | cs.IR | multimodal RAG / cross-chart-reasoning / hierarchical-KG |
| 2606.23543 | VeriEvol | cs.AI | multimodal math reasoning / verifiable Evol-Instruct / RL-data-pipeline |
| 2606.20002 | Connect the Dots | cs.LG | long-horizon agents / cross-domain-RL / agent-training |

### State updates
- `explore_context.json`: 18 fields refreshed; `chains.emergent-concepts.papers_found` +3 (18→21); `emergent_concept_papers` +3 (18→21); `emergent_discoveries` +3; `emergent_concept_search_log` +1 (6→7); `emergent_concept_search_runs` +1 (6→7); `runs` +1 (6→7); `entities_count` 30 → 33
- `watch_profiles.json`: 3 new hashes to top-level (18→21), `llm-wiki` (15→18), `profiles.llm-wiki-explore` (15→18); 3 new records to `last_results` (15→18)

### Cross-check
- 21 arxiv IDs in entities/ ↔ 21 arxiv IDs in state — OK (no orphans, no extras)
- Wikilink integrity: 12 [[slugs]] across 3 new entity files (3 each, all resolve against entities/) — PASS
- Step 5.5 check: 1 broken link caught (the-periodic-table-of-llm-reasoning → the-periodic-table-of-llm-reasoning-a-structured-survey-...) and fixed pre-write
- Pitfall 52 strict subject filter applied: top 3 picks are cs.IR / cs.AI / cs.LG (no cs.CV)
- Pitfall 51 lstrip-prefix check: 21 bullet-prefixed entries after ## Updates — clean
- Pitfall 61 header-duplication check: H2 count = 4 (Scope / Updates / Auto-Discovered Profiles / Chain Status) — clean
- Encoding preserved: explore_context=False (raw em-dash), watch_profiles=True (escape sequences) — divergent state stable

### Tool budget
- All write/commit operations completed cleanly. No pitfall 46a/47 partial-bookkeeping risk.

### MERGE-then-SORT detail
- N_EXISTING_TOP = 3 (new) + 5 (existing top buffer) = 8
- Extracted 8 existing entries (Autodata, Constraint Tax, iLLaDA, entropy-dynamics, agent-native-memory, DREAM, MEMPROBE, AGORA)
- Merged 8 existing + 3 new = 11 entries, sorted arxiv-id-desc
- Top 11 IDs: 25996, 25605, 25331, 25182, 24775, 24667, 24595, 24526, **23997 (NEW)**, **23543 (NEW)**, 20002 (NEW)
- Three new entries landed at positions 9, 10, 11 (correct: lower arxiv-IDs than all 8 existing tops)
- File size: 22,359 → 25,584 chars (+3,225 = expected delta)

### 2026-06-25 17:43 UTC — emergent-concept run (run-1739)
- Method: HuggingFace 3-day daily (2026-06-25..2026-06-23) + monthly archive → 208 unique IDs
- Script: hf_arxiv_discovery.py with --days 3 --months 1 --top-k 100
- Pitfall 52 fired (script Non-CV=188 but top 10 were 100% cs.CV by primary-subject)
- Applied Step 2.5 strict subject filter: 188 → 60 LLM candidates
- LLM-flavor scoring picked top 3:
  - PrivacyAlign (2606.21710, cs.CL, 2026-06-19): agentic-privacy / contextual-alignment
  - Holistic Data Scheduler (2606.24133, cs.LG, 2026-06-23): pretraining-data-mixing / multi-objective-RL
  - EnterpriseClawBench (2606.23654, cs.CL, 2026-06-22): enterprise-agent-evaluation / real-workflow-benchmarking
- All 3 picks verified genuinely new (5-store dedup + filesystem endswith check)
- All 3 entity files written; Step 5.5 wikilink-resolution check: 0 broken
- Prepended to entities/emergent-concepts.md via MERGE-then-SORT (top-8 re-sort, arxiv-ID desc)
- 11-entry merged pool (8 existing + 3 new); new entries landed positions 9, 10, 11
- Preamble-preservation smoke check (pitfall 62): first line = `---` (frontmatter intact)
- File-size sanity check: orig=25584 → new=28278 chars (exact match, no doubling)
- State writes: explore_context.json (15+ top-level fields + chain-level) + watch_profiles.json (4 top + 2 sub-profile)
- ensure_ascii detection: explore_context=False (raw em-dash), watch_profiles=True (escape) — stable divergent state
- Step 7.5 entity↔state cross-check: 24 filesystem arxiv IDs == 24 state arxiv IDs, 0 orphans, 0 extras

### 2026-06-25 17:58 UTC — emergent-concept run (run-1758)
- Method: HuggingFace 3-day daily (2026-06-25..2026-06-23) + monthly archive → 208 unique IDs
- Script: hf_arxiv_discovery.py with --days 3 --months 1 --top-k 100
- Pitfall 52 fired (script Non-CV=185 but raw count was title-flavor upper bound); applied strict subject filter: 185 → 60 LLM candidates
- LLM-flavor scoring + overlap=0 vs prior 36 themes picked top 3:
  - ReNIO (2606.23104, cs.LG, 2026-06-22): on-policy distillation / negative-trajectory-importance estimation
  - PhoneBuddy (2606.23049, cs.CL, 2026-06-22): mobile-deployment / open-model phone-use training
  - Look Light, Think Heavy (2606.22565, cs.CL, 2026-06-21): multimodal-CoT capability audit
- All 3 picks verified genuinely new (5-store dedup + filesystem endswith check)
- All 3 entity files written; Step 5.5 wikilink-resolution check: 0 broken
- Prepended to entities/emergent-concepts.md via MERGE-then-SORT (top-8 re-sort)
- 8-entry merged pool (5 existing + 3 new); new entries landed positions 6, 7, 8 (older than existing Jun-23/24 top)
- Preamble-preservation smoke check (pitfall 62): first line = `---` (frontmatter intact)
- File-size sanity check: 28278 → 31305 chars (+3027, no doubling)
- State writes: explore_context.json (15+ top-level fields + chain-level + 3 list appends) + watch_profiles.json (3 new hashes each at top-level + llm-wiki + llm-wiki-explore sub-profile)
- ensure_ascii detection: explore_context=False (raw em-dash), watch_profiles=True (escape) — stable divergent state
- Step 7.5 entity↔state cross-check: 27 filesystem arxiv IDs == 27 state arxiv IDs, 0 orphans, 0 extras
- Pitfall-60 defensive isinstance guards for watch_profiles sub-profiles fired correctly (both sub-profiles present)
- log.md presence: yes (pitfall 58 not triggered); staged in same atomic commit

### 2026-06-25 18:08 UTC — emergent-concept run (run-1808)
- Method: HuggingFace 3-day daily (2026-06-23..2026-06-25) → 115 unique IDs
- Custom HF discovery script at /tmp/hf_discover_run1808.py (parsed HF `<article>` blocks: `<h3><a href="/papers/{arxiv_id}">Title</a></h3>` pattern); 10-worker ThreadPoolExecutor for parallel arxiv metadata fetch (115 IDs in 4.4s)
- Pitfall 52 strict subject filter applied: 115 → 80 LLM-relevant candidates (excluded cs.CV/cs.GR/cs.MM/eess.AS/physics/cs.SE)
- Combined sort: subject-preference (cs.CL=100, cs.LG=95, cs.AI=90) + LLM-flavor title-boost + recency window + base score → top 3 picks:
  - CalVerT (2606.21777, cs.CL, 2026-06-23): LLM-agent verifier-telemetry / knowledge-intensive-QA
  - Demystifying Training-Time Augmentation (2606.16246, cs.LG, 2026-06-23): data-constrained-pretraining / training-time-augmentation / compute-abundant-regime
  - AC-ODM (2505.23878, cs.LG, 2026-06-23): pretraining-efficiency / online-data-mixing / actor-critic-RL (originally posted 2025/05/29, re-surfaced by HF on 2026-06-23)
- All 3 picks verified genuinely new (5-store dedup + filesystem endswith check; 0% pre-existing rate expected per pitfall-58a for just-restored wiki)
- All 3 entity files written; Step 5.5 wikilink-resolution check: 7 wikilinks total, all resolve (forward + backward links to existing entities)
- Prepended to entities/emergent-concepts.md via MERGE-then-SORT (N_EXISTING_TOP=5, top-8 re-sort)
- 8-entry merged pool (5 existing 06-24/06-23 + 3 new 06-23); new entries landed positions 6, 7, 8 (older than existing 06-23 entries by arxiv-id tiebreak: 2606.21777 > 2606.16246 > 2505.23878)
- Preamble-preservation smoke check (pitfall 62): first line = `---` (frontmatter intact)
- H2 count check: 4 (Scope, Updates, Auto-Discovered Profiles, Chain Status) — no doubled-section-header bug (pitfall 61)
- File-size sanity check: 31457 → 35029 chars (+3572, no doubling)
- State writes: explore_context.json (entities_count 39→42, chains_updated=['emergent-concepts'], 1 record each to emergent_concept_search_log/runs/emergent_concept_search_runs + 3 records each to emergent_concept_papers/emergent_discoveries/chains[emergent-concepts].papers_found) + watch_profiles.json (3 new hashes at top-level + llm-wiki + llm-wiki-explore sub-profile + 3 last_results records)
- ensure_ascii detection: explore_context=False (raw em-dash absent, no encoding), watch_profiles=True (escape sequences) — stable divergent state confirmed
- Step 7.5 entity↔state cross-check (pre-commit): 30 filesystem arxiv IDs == 30 state arxiv IDs, 0 orphans, 0 extras
- Pitfall-60 defensive isinstance guards for watch_profiles sub-profiles: both llm-wiki (dict) and profiles.llm-wiki-explore (dict) present, writes succeeded
- Per-run counter suffix on all 5 /tmp/ artifacts: run1808 (per sibling-subagent /tmp/*.py interference fix)
- log.md presence: yes; staged in same atomic commit

## 2026-06-25 18:29 UTC (run1823)
- Emergent-concept pass via 3-day HF window (2026-06-22..2026-06-25)
- 115 raw HF papers → 52 after Step 2.5 strict subject filter → top-3 LLM-flavor picks
- 3 new entity pages created:
  - LingxiDiagBench (2602.09379, cs.AI, 2026-02-10): Chinese psychiatric-consultation multi-agent benchmark
  - When Agents Commit Too Soon (2606.22936, cs.AI, 2026-06-22): premature-commitment diagnostic for long-horizon LLM agents
  - HAKARI-Bench (2606.22778, cs.IR, 2026-06-22): lightweight retrieval-architecture benchmark
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT (N_EXISTING_TOP=30, all existing entries >= min_new_date so new entries sort below)
- State files: explore_context.json (33 in emergent_concept_papers, 33 in chains[emergent-concepts].papers_found), watch_profiles.json (33 top-level hashes + 33 in each sub-profile after orphan-fix pass)
- Pitfalls hit: 62 (preamble-loss — first attempt lost preamble; recovered via git checkout + corrected recipe), 61 (boundary-header-doubling — first attempt doubled H2s; recovered via fixed tail-extraction logic)
- Pitfalls cleanly avoided: 50 (cross-check pre-commit), 52 (strict subject filter), 28 (wikilink resolution check — caught broken rl-index link in HAKARI page, removed), 53 (list appends), 60 (defensive isinstance), 64 (chains_updated REPLACE not append), 65 (custom HF parser since bundled script missing — wrote /tmp/hf_discover_run1823.py)

## 2026-06-25 18:38 UTC (run1830)
- Emergent-concept pass via 3-day HF window (2026-06-22..2026-06-25, end_d=2026-06-25)
- 115 raw HF papers → 80 after Step 2.5 strict subject filter (35% CV/graphics/sound excluded) → 49 fresh after 5-store dedup → 3 manual picks from LLM-flavor + LLM-research relevance
- 3 new entity pages created:
  - RL-Index (2606.16316, cs.IR, 2026-06-15): GRPO-trained offline index-rationale augmentation that shifts reasoning compute from query time to indexing
  - Counsel (2606.21627, cs.AI, 2026-06-19): first public meta-evaluation dataset for LLM-as-judge on agentic tasks (tau-bench + DA-Code), human-labeled spot-on / location-only / should-not-flag
  - Beyond Reward Engineering (2606.18831, cs.CL, 2026-06-17): data-recipe-first long-context RL with minimal outcome-based GRPO, +7.2/+3.2/+6.4 on Qwen3-4B/8B/30B-A3B + agentic transfer (GAIA +4.8, BrowseComp +7.0)
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT (N_EXISTING_TOP=10, new dates 06/15-06/19 inserted at positions 9-11 after 2026-06-24 and 2026-06-23 entries)
- State files: explore_context.json (36 in emergent_concept_papers, 36 in chains[emergent-concepts].papers_found), watch_profiles.json (36 top-level hashes + 36 in each sub-profile)
- ensure_ascii detection: explore_context=False (raw em-dash absent), watch_profiles=True (escape sequences) — stable divergent state confirmed
- Step 7.5 entity↔state cross-check (pre-write): 33 filesystem == 33 state arxiv IDs, 0 orphans, 0 extras
- Step 7.5 entity↔state cross-check (post-write): 36 filesystem == 36 state, 0 orphans, 0 extras
- Pitfalls cleanly avoided: 4/32/41/46/49/62 (MERGE-then-SORT + preamble preservation), 52 (strict subject filter), 28 (wikilink resolution check — all 17 new wikilinks resolved), 53 (list-shaped appends for search_runs/runs), 60 (defensive isinstance on watch sub-profiles), 63 (no execute_code in cron context — used write_file + terminal), 64 (chains_updated REPLACE not append), 65 (custom HF parser — bundled script missing), 66 (N_EXISTING_TOP > len(new_entries) safe default)
- Step 2.5 strict subject filter recovered 80 LLM candidates from 115 raw non_cv_metadata (32 CV + 3 cs.GR + 0 cs.SD excluded); top-3 picks are all cs.CL/cs.AI/cs.IR with score=4
- Per-run counter suffix on /tmp/ artifacts: run1830 (sibling-subagent /tmp/*.py interference fix)

## 2026-06-25 18:51 UTC (run1850)
- Emergent-concept pass via 3-day HF window (2026-06-23..2026-06-25, end_d=2026-06-25)
- 115 raw HF papers → 80 after Step 2.5 strict subject filter (35 CV/graphics/sound excluded) → 46 fresh after 5-store dedup → 3 picks from LLM-flavor + subject-priority scoring
- 3 new entity pages created:
  - OpenThoughts-Agent (2606.24855, cs.AI, 2026-06-23): open end-to-end data curation pipeline for agentic LLMs; 100+ controlled ablations; 100K-example dataset; Qwen3-32B @ 44.8% avg over 7 agentic benchmarks (3.9pp > Nemotron-Terminal-32B)
  - Qwen-AgentWorld (2606.24597, cs.CL, 2026-06-23): first family of language world models (35B-A3B + 397B-A17B) simulating 7 agentic domains via long CoT, trained on 10M+ trajectories with CPT/SFT/RL pipeline + AgentWorldBench
  - Tapered Language Models (2606.23670, cs.LG, 2026-06-22): depth-aware capacity allocation via MLP-width cosine taper; +perplexity on 3 scales × 4 architectures (Transformer, Gated Attention, Hope-attention, Titans) at no extra params
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT (N_EXISTING_TOP=8, new dates 06/22-06/23 interleaved at positions 5, 8, 11)
- State files: explore_context.json (39 in emergent_concept_papers, 39 in chains[emergent-concepts].papers_found), watch_profiles.json (39 top-level hashes + 39 in llm-wiki + 39 in profiles.llm-wiki-explore)
- ensure_ascii detection: explore_context=False (raw em-dash), watch_profiles=True (escaped) — divergent stable state confirmed (3rd consecutive run)
- Step 7.5 entity↔state cross-check (post-write): 39 filesystem == 39 state arxiv IDs, 0 orphans, 0 extras
- Pitfalls hit: NONE in main flow
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + N_EXISTING_TOP=len(new)+5), 52 (strict subject filter — 80 LLM candidates from 115 raw), 28 (wikilink resolution — all 9 new wikilinks resolved), 53 (list appends for search_runs/runs), 60 (defensive isinstance on watch sub-profiles — both llm-wiki + profiles.llm-wiki-explore updated cleanly), 63 (no execute_code — used write_file + terminal pattern), 64 (chains_updated REPLACE not append), 65 (custom HF parser — bundled script still missing; wrote /tmp/hf_discover_run1850.py)
- Per-run counter suffix on all /tmp/ artifacts: run1850 (per sibling-subagent /tmp/*.py interference fix)
- log.md presence: yes; staged in same atomic commit
## 2026-06-25 18:58 UTC — Run summary
- Theme: LLM agent autonomy under-evaluated safety axes (privilege + context) + reasoning theory boundary
- Discovery: HF daily 3-day window 2026-06-23..25 (115 unique arxiv IDs) → strict subject non-CV filter (43 candidates) → LLM-flavor kw scoring → top 3 picks
- Picks (3):
  - A Verifiable Search Is Not a Learnable Chain-of-Thought (2606.21884, cs.LG, 2026-06-20): CoT distillation provably fails for cryptarithm (0.01-0.07 across 11 designs + RLVR + self-training) even with 97-100% line-level arithmetic; mechanistic gap not capability gap; holds 3B→671B
  - When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents (2606.20023, cs.SE, 2026-06-18): ToolPrivBench across 8 domains × 5 risk patterns; general safety alignment does NOT transfer to least-privilege tool choice; privilege-aware post-training defense proposed
  - Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity? (2606.23189, cs.AI, 2026-06-22): AgentCIBench — 11/15 frontier agents leak on >50% of contextual-integrity scenarios; 67.9% avg leakage; failures persist end-to-end in environment
- Parent [[emergent-concepts]] ## Updates: 3 entries prepended via MERGE-then-SORT Recipe C (N_EXISTING_TOP=len(new)+5=8; all new dates 06/18-06/22 older than existing top 06/23-06/24; landed at positions 9, 10, 11)
- State files: explore_context.json (42 in emergent_concept_papers, 42 in emergent_discoveries, 39 in chains[emergent-concepts].papers_found), watch_profiles.json (42 top-level hashes + 42 in llm-wiki + 42 in profiles.llm-wiki-explore + 39 in profiles.llm-wiki-explore.last_results)
- ensure_ascii detection: explore_context=False (raw em-dash), watch_profiles=True (escaped) — divergent stable state confirmed (4th consecutive run)
- Step 7.5 entity↔state cross-check (post-write): 42 filesystem == 42 state arxiv IDs after commit; 0 orphans pre-write (the 3 orphans in the pre-write check were the 3 new entity files being added in this run — expected)
- Pitfalls hit: NONE in main flow
- Pitfalls cleanly avoided: 4/32/41/46/49/62/66/66b (MERGE-then-SORT + preamble preservation + Recipe C + last-entry-boundary fix), 52 (strict subject filter — 43 LLM candidates from 115 raw), 28 (wikilink resolution — all 12 new wikilinks resolved across 3 new entity files), 48 (canonical slug + suffix-match dedup — 0 collisions), 53 (list appends for search_runs/runs), 59 (pre-write entity↔state cross-check detected expected orphans as the new files being added in this run), 60 (defensive isinstance on watch sub-profiles — both llm-wiki + profiles.llm-wiki-explore updated cleanly), 63 (no execute_code — used write_file + terminal pattern), 64 (chains_updated REPLACE not append), 65 (custom HF parser in /tmp/hf_discover_run1858.py — bundled scripts/hf_arxiv_discovery.py still missing on the restored wiki)
- Per-run counter suffix on all /tmp/ artifacts: run1858 (per sibling-subagent /tmp/*.py interference fix)
- log.md presence: yes; staged in same atomic commit