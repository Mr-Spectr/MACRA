# 💹 MACRA - Market Credibility Risk Analyzer

**MACRA** (Market Credibility Risk Analyzer) is an AI-powered, real-time Indian stock portfolio recommender and market vulnerability dashboard. It leverages LLMs (OpenRouter/Deepseek) to generate professional, data-driven Indian stock portfolios based on user investment preferences, and visualizes them with interactive charts and robust error handling.

---

## 🚀 Features
- **AI-Powered Portfolio Generation:** Uses LLMs to recommend Indian stock portfolios based on investment amount, risk, and duration.
- **Interactive Streamlit Dashboard:** Modern UI with MACRA branding, professional tables, and trading-style charts (bar, pie, candlestick).
- **Robust Error Handling:** Always displays a valid portfolio table, even if the LLM fails, with clear user feedback.
- **LLM Chat Advisor:** Ask follow-up questions about your stocks and get instant, AI-powered answers.
- **Automated Fallbacks:** If the LLM cannot generate a valid table, a sample portfolio is shown with a warning.
- **API-First Design:** Flask backend with `/llm` endpoint for LLM integration and `/predict` for legacy ML.

---

## 🖥️ Quickstart

### 1. Install Requirements
```powershell
pip install -r requirements.txt
```

### 2. Set Up Environment
- Copy `.env.example` to `.env` and fill in your OpenRouter API key and model (or edit directly in `src/api.py`).

### 3. Start Backend API
```powershell
python src/api.py
```

### 4. Start Streamlit Dashboard
```powershell
streamlit run src/dashboard.py
```

---

## 📝 Usage
1. Enter your investment amount (INR), risk level, and duration in the dashboard form.
2. Click **Generate Portfolio**. The dashboard will display a professional table and interactive charts.
3. If the AI cannot generate a portfolio, a sample portfolio will be shown with a warning.
4. Use the **Ask more about your stocks** section to chat with the LLM about your portfolio.

---

## ⚙️ Project Structure
```
MACRA/
  README.md         # This file
src/
  api.py           # Flask backend API (LLM + legacy ML)
  dashboard.py     # Streamlit dashboard frontend
logo/              # MACRA logo assets
requirements.txt   # Python dependencies
.env               # Environment variables (API keys, etc.)
```

---

## 🛡️ Error Handling & Fallbacks
- The dashboard and backend are designed to never crash or show a blank table.
- If the LLM fails, a hardcoded sample portfolio is always shown, with a clear warning.
- All errors are logged and user-friendly messages are displayed.

---

## 🤖 LLM Integration
- Uses OpenRouter/Deepseek or similar LLMs for portfolio generation.
- Strict system prompts ensure the LLM always returns a markdown table in the required format.
- Backend post-processing enforces column order, units, and fills missing data.

---

## 📈 Example Portfolio Table
| Ticker   | Current Price (INR) | Company                     | Sector      | Industry           | Allocation (%) | Risk Analysis         | Rationale              |
|----------|---------------------|-----------------------------|-------------|--------------------|----------------|----------------------|------------------------|
| TCS      | 3800                | Tata Consultancy Services   | IT          | IT Services        | 20             | Low risk, bluechip   | Largecap IT leader     |
| RELIANCE | 2900                | Reliance Industries         | Energy      | Conglomerate       | 15             | Moderate risk        | Diversified business   |
| ...      | ...                 | ...                         | ...         | ...                | ...            | ...                  | ...                    |

---

## 🧑‍💻 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
[MIT](../LICENSE)

---

## 🌐 GitHub Repository
> Please commit and push your changes to your GitHub repository to keep your project up to date.
