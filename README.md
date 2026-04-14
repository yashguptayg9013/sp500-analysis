# 📊 S&P 500 Market Analysis

A Python-based analysis of S&P 500 historical performance using the `yfinance` API. This project examines long-term index behaviour, sector trends, drawdown cycles, and macro patterns to help investors understand the market's risk-return profile over time.

---

## 📌 Business Question

> *What does the historical behaviour of the S&P 500 tell us about market cycles, recovery patterns, and the risk profile of broad-market index investing?*

---

## 📊 Analysis Coverage

- **Historical Price Trend** — Long-term index performance from 2000 to present
- **Annual & Cumulative Returns** — Year-by-year return breakdown and compounding effect
- **Drawdown Analysis** — Identifying the deepest and longest drawdown periods (dot-com, 2008, COVID)
- **Rolling Volatility** — 30-day and 90-day rolling standard deviation of daily returns
- **Return Distribution** — Frequency analysis and fat-tail risk assessment
- **Macro Event Overlay** — Key market events annotated on the price chart for contextual insight

---

## 🔍 Key Findings

- The S&P 500 delivered a **CAGR of ~10.5%** over the last 20 years despite multiple severe drawdowns
- The **2008 Financial Crisis** produced the deepest drawdown (~56%) with a recovery period of ~5.5 years
- **COVID crash (2020)** was the fastest crash-and-recovery in modern index history — recovering in under 6 months
- Rolling volatility spikes reliably **precede** major drawdown events by 2–4 weeks, offering a risk signal

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![yfinance](https://img.shields.io/badge/yfinance-0078D4?style=flat)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)

---

## 📁 Repository Structure

```
sp500-analysis/
│
├── sp500_analysis.py                  # Main analysis script
├── sp500_analysis.ipynb               # Jupyter notebook version
├── figures/                           # Output visualisations
└── README.md
```

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/yashguptayg9013/sp500-analysis.git
cd sp500-analysis

# Install dependencies
pip install pandas yfinance matplotlib seaborn jupyter

# Run the script
python sp500_analysis.py

# Or open the notebook
jupyter notebook sp500_analysis.ipynb
```

> **Note:** yfinance fetches live data from Yahoo Finance — an internet connection is required.

---

## 💡 Business Relevance

Understanding index-level market behaviour is foundational to portfolio construction, risk management, and financial product design. This analysis provides the quantitative groundwork for discussions around passive investing strategy, volatility-based risk management, and long-term capital allocation.

---

## 📬 Author

**Yash Gupta** — MSc Business Analytics, Dublin Business School
[LinkedIn](https://www.linkedin.com/in/yashguptayg9013/) · [GitHub](https://github.com/yashguptayg9013)
