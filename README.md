# 💹 MACRA - Market Credibility Risk Analyzer

**MACRA** (Market Credibility Risk Analyzer) is a real-time vulnerability analysis platform that quantifies the market's credit credibility by integrating population-scale credit metrics, banking risk, and macroeconomic indicators such as GDP, unemployment rates, and public sentiment. It provides a data-driven *Market Vulnerability Score* to aid analysts, regulators, and financial institutions in forecasting regional or national market stability.

---

## 🚩 Problem Statement

Traditional financial institutions lack real-time, comprehensive tools that assess the aggregated credit risk and macroeconomic vulnerability of a population or region. This absence limits early warning capabilities during volatile conditions—especially in developing economies where financial transparency is low and sentiment-driven events can trigger large-scale instability.

---

## ✅ Proposed Solution

MACRA computes a dynamic **Market Vulnerability Score (MVS)** by fusing:

- Individual and institutional credit behavior
- Aggregated bank risk indicators
- Macroeconomic indicators (GDP trends, unemployment)
- Sentiment signals (e.g., news & social media tone)

It delivers these insights via a responsive dashboard, exposing APIs for advanced use and enabling real-time scenario testing.

---

## 🧠 Core Features

- 📊 **Dynamic Market Vulnerability Score (MVS)**
- 🌐 **Region-wise Economic Heatmaps**
- 📉 **What-if simulations for economic shocks**
- 📡 **Sentiment analytics via NLP (future extension)**
- 📱 **Developer-friendly REST API access**
- 🧮 **Explainable ML models for financial interpretability**

---

## 🧰 Tech Stack

| Layer         | Tools & Frameworks                     |
|---------------|----------------------------------------|
| Data Handling | `pandas`, `numpy`                      |
| ML / Scoring  | `scikit-learn`, custom weight models   |
| API Server    | `Flask`                                |
| Frontend UI   | `Streamlit` (dashboard), `React` (optional) |
| Cloud Hosting | `GCP` or `AWS` (for scalable deployment) |
| DevOps        | `Docker`, `GitHub Actions` (optional)  |

---

## 📁 Folder Structure

```bash
macra/
├── data/                # Sample & raw data files
├── notebooks/           # EDA & model experimentation
├── src/
│   ├── ingestion.py     # Data loading & cleaning
│   ├── features.py      # Feature engineering
│   ├── model.py         # Vulnerability scoring logic
│   ├── api.py           # Flask API endpoints
│   └── dashboard.py     # Streamlit frontend
├── Dockerfile
├── requirements.txt
└── README.md
