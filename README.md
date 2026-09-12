# ⚖️ The Rulebook That Argues With Itself

A deterministic regulatory retrieval and contradiction-resolution engine that parses multi-format institutional documents (Markdown, Tabular Fee Schedules, and PDFs), identifies clause conflicts, and refuses out-of-scope near-miss queries with zero hallucination.

---

## 🎯 Key Features & System Properties

- **3 Deterministic States:**
  - `ANSWER`: Direct, grounded answer accompanied by verified document citations.
  - `CONTRADICTION`: Detects when two institutional clauses present mutually incompatible rules and surfaces both side-by-side.
  - `REFUSAL`: Rejects plausible near-miss queries where the regulatory corpus is silent.
- **Traceable Citations:** Returns file name, clause title, and exact excerpt for every response.
- **Multi-Format Corpus:** Parses standard Markdown files, tabular fee structures, and multi-page policy PDFs.
- **Automated Benchmark Suite:** Includes a standalone CLI eval runner testing all 3 planted contradictions, 5 standard retrieval queries, and 25 hard near-miss refusals.

---

## 📊 Evaluation Results

| Category | Test Cases | Accuracy | Result |
|---|---|---|---|
| **CONTRADICTION** | 3 | 3 / 3 (100.0%) | ✅ PASS |
| **ANSWER** | 5 | 5 / 5 (100.0%) | ✅ PASS |
| **REFUSAL (Near-Misses)** | 25 | 25 / 25 (100.0%) | ✅ PASS |
| **Overall Benchmark** | **33** | **33 / 33 (100.0%)** | 🏆 **100.0%** |

---

## 🚀 Quickstart

### 1. Environment Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
