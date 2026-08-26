# Phase 2: Exploratory Data Analysis & Financial Dashboards

## 📌 Phase Overview
This module transitions raw, structured financial datasets into actionable visual insights. It focuses on **Exploratory Data Analysis (EDA)**, **Time-Series Analysis**, and building **Interactive Financial Dashboards**. Using Python's visualization ecosystem alongside Streamlit, this phase enables real-time visual tracking of financial performance indicators (KPIs), anomaly detection, and cash-flow patterns.

---

## 🎯 Core Objectives
1. **Exploratory Data Analysis (EDA):**
   - Uncover data distributions, financial ratios, and underlying variance using statistical visualizations.
   - Identify financial anomalies and transaction outliers using IQR techniques and box plots.
2. **Time-Series & Trend Analysis:**
   - Track period-over-period revenue and expense trajectories.
   - Calculate rolling moving averages to smooth out daily volatility and highlight seasonal behavior.
3. **Interactive Dashboard Development:**
   - Build responsive, filterable web dashboards using **Plotly** and **Streamlit**.
   - Render real-time executive financial summary cards (Gross Income, Total Expenses, Net Profit Margin).

---

## 🛠️ Stack & Libraries Used
- **Data Handling:** `pandas`, `numpy`
- **Static & Statistical Plotting:** `matplotlib`, `seaborn`
- **Interactive Visualization:** `plotly`, `plotly-express`
- **Dashboard Framework:** `streamlit`
- **Data Source:** MariaDB / MySQL (`financial_db`)

---

## 📂 Phase Folder Architecture

```text
Phase-2-Visualization-Dashboards/
├── notebooks/
│   ├── 01_financial_eda.ipynb        # Statistical distributions & anomaly detection
│   └── 02_time_series_trends.ipynb   # Seasonal decomposition & rolling averages
└── app/
    ├── main_dashboard.py             # Streamlit interactive application
    └── components/                   # Custom UI components & plot generators