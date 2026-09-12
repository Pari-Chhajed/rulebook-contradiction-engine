# ⚖️ The Rulebook That Argues With Itself

A **deterministic regulatory retrieval and contradiction-resolution engine** designed to process multi-format institutional documents, identify conflicting clauses, provide traceable answers, and refuse plausible but unsupported queries — with **zero hallucination by design**.

The system works across **Markdown documents, tabular fee schedules, and policy PDFs**, classifying every query into one of three deterministic outcomes:

* `ANSWER` — A grounded answer supported by verified document evidence.
* `CONTRADICTION` — Two or more institutional clauses contain mutually incompatible rules.
* `REFUSAL` — The regulatory corpus does not contain sufficient information to answer the query.

---

## 🎯 Key Features

### Deterministic Decision States

The engine produces exactly one of three outcomes for every query:

| State           | Description                                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| `ANSWER`        | Returns a direct answer grounded in the regulatory corpus, along with document citations.            |
| `CONTRADICTION` | Detects mutually incompatible institutional clauses and presents the conflicting rules side-by-side. |
| `REFUSAL`       | Rejects plausible near-miss queries when the regulatory corpus contains no supporting evidence.      |

### 🔎 Traceable Citations

Every response includes verifiable source information:

* Source file name
* Clause or section title
* Exact supporting excerpt

This makes every decision auditable and allows users to trace an answer directly back to the source material.

### 📚 Multi-Format Regulatory Corpus

The retrieval engine supports multiple institutional document formats, including:

* Markdown (`.md`)
* Tabular fee schedules
* Multi-page policy PDFs

### 🧪 Automated Evaluation Suite

The repository includes a standalone CLI benchmark runner covering:

* **3** planted contradiction cases
* **5** standard retrieval queries
* **25** hard near-miss queries designed to test refusal behavior

The complete benchmark contains **33 test cases**.

---

## 📊 Evaluation Results

| Category                  | Test Cases |             Accuracy | Result      |
| ------------------------- | ---------: | -------------------: | ----------- |
| **CONTRADICTION**         |          3 |       3 / 3 (100.0%) | ✅ PASS      |
| **ANSWER**                |          5 |       5 / 5 (100.0%) | ✅ PASS      |
| **REFUSAL — Near-Misses** |         25 |     25 / 25 (100.0%) | ✅ PASS      |
| **Overall Benchmark**     |     **33** | **33 / 33 (100.0%)** | 🏆 **PASS** |

### Overall Accuracy: **100.0%**

The engine successfully handled all **33 benchmark cases**, including contradiction detection, grounded retrieval, and out-of-scope refusal.

---

## 🚀 Quickstart

### 1. Set Up the Environment

Create and activate a Python virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

> **Windows:** Activate the virtual environment with:
>
> ```powershell
> .venv\Scripts\activate
> ```

---

### 2. Generate the Regulatory Corpus

Generate the sample institutional documents and planted contradictions:

```bash
python generate_corpus.py
```

This populates the `data/` directory with the documents used by the retrieval and evaluation pipeline.

---

### 3. Run the Automated Benchmark

Run the complete evaluation suite:

```bash
python eval_runner.py
```

The evaluator tests all three system states:

* `CONTRADICTION`
* `ANSWER`
* `REFUSAL`

It then reports per-category and overall accuracy.

---

### 4. Launch the Interactive Web UI

Start the Streamlit dashboard:

```bash
streamlit run app.py
```

The application provides an interactive interface for querying the regulatory corpus and inspecting the engine's decisions and supporting citations.

---

## 📁 Repository Structure

```text
.
├── data/
│   ├── academic_regulations.md
│   │   # Degree and attendance policies
│   │
│   ├── fee_and_scholarship_schedule.md
│   │   # Tuition tables and fee-waiver provisions
│   │
│   └── hostel_and_medical_policy.pdf
│       # Multi-page policy containing planted exemptions
│
├── eval/
│   ├── contradictions.md
│   │   # Ground-truth log for planted contradictions
│   │
│   └── test_cases.json
│       # 33 benchmark test queries
│
├── engine.py
│   # FastAPI backend and deterministic retrieval engine
│
├── eval_runner.py
│   # Automated CLI evaluation and scoring runner
│
├── app.py
│   # Streamlit interactive UI
│
├── generate_corpus.py
│   # Regulatory corpus generator
│
└── requirements.txt
    # Python dependencies
```

---

## 🧠 How It Works

At a high level, the system follows a deterministic retrieval-and-resolution pipeline:

```text
                User Query
                    │
                    ▼
          ┌───────────────────┐
          │ Query Processing  │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Regulatory Corpus │
          │    Retrieval      │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Evidence & Clause │
          │     Analysis      │
          └─────────┬─────────┘
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
      ANSWER  CONTRADICTION  REFUSAL
```

The key design principle is that **retrieval and evidence determine the response**. When the corpus does not provide sufficient evidence, the engine refuses to answer rather than generating an unsupported response.

---

## 🛡️ Design Philosophy

The system prioritizes **determinism, traceability, and conservative decision-making** over speculative answers.

### No Unsupported Answers

A query that sounds relevant but falls outside the regulatory corpus should result in:

```text
REFUSAL
```

rather than an inferred or fabricated answer.

### Explicit Contradiction Handling

When institutional documents contain conflicting rules, the system does not silently choose one. Instead, it surfaces the conflicting clauses so the disagreement can be inspected directly.

### Evidence-First Responses

Every successful answer is backed by source-level evidence, allowing users to verify where the decision originated.

---

## 🧪 Benchmark Coverage

The evaluation suite intentionally tests three different failure modes:

### 1. Contradiction Detection

Tests whether the engine can identify cases where institutional documents prescribe incompatible rules.

**Expected state:**

```text
CONTRADICTION
```

### 2. Grounded Retrieval

Tests whether the engine can retrieve and answer questions directly supported by the regulatory corpus.

**Expected state:**

```text
ANSWER
```

### 3. Near-Miss Refusal

Tests whether the engine can distinguish between questions that *sound* regulatory but are not actually covered by the available documents.

**Expected state:**

```text
REFUSAL
```

This ensures that high retrieval confidence alone does not result in an unsupported answer.

---

## 📈 Current Benchmark

**33 / 33 test cases passed**

```text
CONTRADICTION   ████████████████████  3/3
ANSWER          ████████████████████  5/5
REFUSAL         ████████████████████ 25/25
──────────────────────────────────────────
OVERALL         ████████████████████ 33/33
```

**Overall accuracy: 100.0%**

---

## 📄 License

Add your project license here, for example:

```text
MIT License
```

if the repository is intended to be released under the MIT License.
