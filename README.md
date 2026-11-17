# 🛡️ ChaosLLM — Automated AI Safety & Red-Teaming Auditor

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Powered by](https://img.shields.io/badge/Powered%20by-Google%20GenAI-4285F4.svg)](https://aistudio.google.com/)

> **Stress-test and audit LLM system prompts against prompt injections, roleplay hijacks, and instruction leaks before deployment.**

---

## 📌 Overview

As companies deploy generative AI into production, system prompt security has become a critical vulnerability surface. Attackers use jailbreak framing, delimiter manipulation, and indirect instruction overrides to leak sensitive instructions or bypass guardrails.

**ChaosLLM** is an open-source, automated red-teaming tool designed to audit system prompts against curated vulnerability vectors. It executes adversarial probes, employs an automated LLM Judge to evaluate compliance, scores prompt resilience, and generates remediation guidance with downloadable security audit reports.

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A["Target System Prompt"] --> B["ChaosLLM Test Runner"]
    C["Curated Probe Suite<br/>(OWASP LLM Top 10)"] --> B
    B --> D["Target Model Execution<br/>(Google Gemini API)"]
    D --> E["Evaluator & Judge Pipeline<br/>(LLM-as-a-Judge + Heuristics)"]
    E --> F["Safety Score & Radar Metrics"]
    E --> G["Remediation & Hardening Tips"]
    E --> H["Markdown Security Audit Export"]
```

---

## 🎯 Test Categories Covered

1. **System Prompt Leakage (SPL):** Direct commands, code-block extraction, and translation bypasses attempting to dump foundational instructions.
2. **Roleplay & Persona Hijacking (RP):** Fictional framing, unrestricted personas, and simulated administrative debug overrides.
3. **Constraint Bypass (CB):** Negative boundary reverse-engineering and academic/research justification tactics.
4. **Delimiter & Formatting Confusion (DF):** Synthetic boundary injection (`--- END OF INSTRUCTIONS ---`) to trick context parsing.

---

## ✨ Features

- **🎮 Zero-Key Demo Mode:** Test and explore the full suite with realistic simulated responses without configuring an API key.
- **⚡ LLM-as-a-Judge Evaluation:** Uses advanced reasoning to detect nuanced behavioral drift, semantic leaks, and indirect failures.
- **📊 Interactive Visual Dashboard:** Built with Streamlit and Plotly, featuring a real-time Prompt Hardening Index gauge and category breakdown.
- **📑 Downloadable Security Reports:** Generates professional Markdown audit reports ready for engineering compliance reviews.
- **💡 Actionable Remediation:** Provides concrete hardening recommendations (e.g., XML boundary wrapping, negative constraint anchoring).

---

## 🚀 Quickstart Guide

### 1. Clone the Repository
```bash
git clone https://github.com/rakibul200514/ChaosLLM.git
cd ChaosLLM
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy `.env.example` to `.env` and add your free Google Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```
*(Tip: You can get a free API key with 0 credit card required at [Google AI Studio](https://aistudio.google.com/)).*

### 5. Launch the Application
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser!

---

## 📈 Recruiter & Engineering Highlights

- **Systems Engineering:** Clean separation of concerns (`core/test_cases.py`, `core/runner.py`, `core/evaluator.py`, `app.py`).
- **Cost-Optimized:** Built 100% on free-tier APIs and open-source tooling ($0 infrastructure cost).
- **Graceful Fallbacks:** Implements dual-layer evaluation (LLM judge + regex heuristic fallback) for high reliability.

---

## ❓ Frequently Asked Questions (FAQ)

<details>
<summary><b>1. Why is system prompt hardening necessary for production LLMs?</b></summary>
<br>
In production applications, system prompts define foundational boundaries, compliance rules, and sometimes access keys or internal policies. Without hardening, malicious users can employ prompt injections, roleplay traps, or delimiter confusion to hijack the model's persona, leak confidential directives, or bypass business logic. ChaosLLM automates the discovery of these flaws before deployment.
</details>

<details>
<summary><b>2. Does running ChaosLLM require a paid API subscription?</b></summary>
<br>
<b>No.</b> ChaosLLM is designed to be 100% free-tier compatible. You can use Google AI Studio's free Gemini API key (no credit card required). Additionally, ChaosLLM includes a <b>Zero-Key Demo Mode</b> with pre-calibrated simulation vectors so anyone can evaluate the dashboard without any credentials.
</details>

<details>
<summary><b>3. How does the automated evaluation engine score vulnerabilities?</b></summary>
<br>
ChaosLLM uses a dual-layer grading pipeline:
1. <b>LLM-as-a-Judge:</b> An evaluator model analyzes the semantic context, checking whether the response adhered to or violated the target system prompt.
2. <b>Heuristic Engine (Fallback):</b> Lexical overlap analysis and refusal pattern detectors guarantee instant, zero-latency scoring even if the API quota is constrained.
</details>

<details>
<summary><b>4. Can I add custom adversarial test cases?</b></summary>
<br>
Yes! The test architecture is fully modular. Simply open <code>core/test_cases.py</code> and add your probe dictionary with <code>id</code>, <code>category</code>, <code>severity</code>, <code>probe</code>, and <code>intent</code>. The web dashboard will automatically discover and integrate new test vectors.
</details>

<details>
<summary><b>5. Can I test models from OpenAI, Anthropic, or local Ollama instances?</b></summary>
<br>
Yes. The probe execution is decoupled in <code>core/runner.py</code>. You can easily plug in any LiteLLM, OpenAI, or local Ollama endpoint by extending the <code>execute_probe()</code> function.
</details>

<details>
<summary><b>6. Is this tool compliant with AI safety and ethical research standards?</b></summary>
<br>
Yes. ChaosLLM is strictly a <b>defensive security auditing and benchmarking tool</b> created to help engineers identify weaknesses in their own prompts. It aligns with the OWASP Top 10 for LLMs and contains defensive mitigation advice for each finding.
</details>

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.
