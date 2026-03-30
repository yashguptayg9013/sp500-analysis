# 📈 S&P 500 Companies — Exploratory Data Analysis

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13-4c72b0)
![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-F37626?logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

> A business-analyst-oriented deep dive into the **503 companies** that constitute the S&P 500 index — exploring sector composition, geographic concentration, index evolution, and company founding patterns.

---

## 📌 Project Overview

The **S&P 500** is the most widely tracked equity index in the world, representing ~80% of available US market capitalisation. Understanding *who* is in the index — and *why* — is foundational knowledge for any business analyst, investor, or strategist.

This project answers:
- Which sectors dominate the index by company count?
- How has index composition evolved over decades?
- Where are S&P 500 companies headquartered?
- What does the sub-industry breakdown reveal about sector diversity?
- Which are the oldest (and newest) index members?

---

## 📂 Repository Structure

```
sp500-analysis/
│
├── data/
│   ├── sp500_companies.csv       ← Raw dataset (503 companies)
│   └── sp500_cleaned.csv         ← Cleaned + feature-engineered version
│
├── notebooks/
│   └── sp500_eda.ipynb           ← Interactive Jupyter notebook (full analysis)
│
├── scripts/
│   └── analysis.py               ← Standalone Python script (reproduces all charts)
│
├── visualizations/               ← All generated charts (PNG, 150 dpi)
│   ├── 1_sector_distribution.png
│   ├── 2_additions_over_time.png
│   ├── 3_top_hq_states.png
│   ├── 4_founding_decade_by_sector.png
│   ├── 5_sector_subindustry_heatmap.png
│   └── 6_sector_pie.png
│
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

| Field | Description |
|---|---|
| `symbol` | Stock ticker symbol |
| `company` | Full company name |
| `sector` | GICS sector classification |
| `sub_industry` | GICS sub-industry |
| `headquarters` | City, State of HQ |
| `date_added` | Date added to the S&P 500 |
| `founded` | Year company was founded |

- **503 companies** | **11 sectors** | **127 sub-industries** | **251 unique HQ locations**

---

## 🔍 Key Findings

### 1. 🏭 Industrials Lead by Volume
Industrials is the largest sector with **79 companies (15.7%)**, followed closely by Financials (76) and Information Technology (73). This challenges the popular narrative that Tech dominates — by *count*, traditional sectors still hold their ground.

### 2. 🗺️ Geographic Concentration
**New York, California, and Texas** together host **173 companies — 34.4% of the entire index**. New York alone houses 40 companies, reflecting its role as the financial capital of the US.

### 3. 🏛️ Remarkable Longevity
**BNY Mellon (est. 1784)** is the oldest S&P 500 member — over 241 years old. The top 10 oldest companies are predominantly in Financials and Consumer Staples, underscoring these sectors' durability.

### 4. 📅 Index Reshaping Over Decades
The **2010s saw the highest additions** to the index (141 companies), followed by the 2000s (98). Since 2020 alone, **91 companies** have been added — signaling active post-pandemic rebalancing and sector rotation.

### 5. 💻 Tech's Rise
Information Technology has grown to become the **3rd-largest sector by company count**, with 73 members spanning 12 sub-industries — from semiconductors to cloud software to IT services.

### 6. 🌍 Internationalization
**8 S&P 500 companies are headquartered in Dublin, Ireland**, primarily US multinationals that relocated for tax efficiency — highlighting how "American" index composition is increasingly a legal, not geographic, question.

---

## 📈 Visualizations

| Chart | Description |
|---|---|
| ![Sector Distribution](visualizations/1_sector_distribution.png) | Company count by sector |
| ![Additions Over Time](visualizations/2_additions_over_time.png) | Index additions per decade |
| ![HQ States](visualizations/3_top_hq_states.png) | Top 10 states by HQ count |
| ![Founding Decades](visualizations/4_founding_decade_by_sector.png) | Founding decade × sector stacked bar |
| ![Heatmap](visualizations/5_sector_subindustry_heatmap.png) | Sector × sub-industry matrix |
| ![Pie](visualizations/6_sector_pie.png) | Sector composition pie chart |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/sp500-analysis.git
cd sp500-analysis
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the analysis script
```bash
python scripts/analysis.py
```

### 4. Or open the Jupyter notebook
```bash
jupyter notebook notebooks/sp500_eda.ipynb
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.9+** | Core language |
| **Pandas** | Data loading, cleaning, transformation |
| **Matplotlib** | Base plotting engine |
| **Seaborn** | Statistical visualizations |
| **Jupyter** | Interactive exploration notebook |

---

## 🔭 Future Work

- [ ] **Enrich with financial data** via `yfinance` (market cap, P/E, EPS, dividend yield)
- [ ] **Sector performance analysis** — overlay returns with composition changes
- [ ] **Choropleth map** — HQ density by US state using `plotly` or `folium`
- [ ] **Predictive model** — can sector + founding decade predict index tenure?
- [ ] **Survivorship bias analysis** — study companies removed from the index

---

## 👤 Author

**[Yash Gupta]**  
Business Analyst | Data Enthusiast  
📧 yashguptayg9013@gmail.com     
🔗 [LinkedIn](https://www.linkedin.com/in/yashguptayg9013/) | [Portfolio](https://github.com/yashguptayg9013)

---

## 📄 License

This project is licensed under the MIT License — feel free to use, share, and build upon it.

---

*Data sourced from public S&P 500 constituent records. Analysis performed for educational and portfolio purposes.*
