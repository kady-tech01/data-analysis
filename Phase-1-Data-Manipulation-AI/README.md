# Phase 1: Financial Data Manipulation & Smart Extraction

## 📌 Phase Overview
This module focuses on standardizing, cleaning, and extracting structured financial records from unorganized data sources (CSV statement dumps, PDF invoices, and raw SQL queries). It combines high-performance tabular processing via **Pandas** and **NumPy** with **Large Language Models (LLMs)** to automate messy text categorization and entity extraction.

---

## 🎯 Core Objectives
1. **Data Wrangling & Cleaning:**
   - Standardize messy currency values and heterogeneous date formats into structured `datetime` types.
   - Clean missing records (`NaN`) and deduplicate transaction entries without losing financial accuracy.
2. **Advanced Tabular Transformations:**
   - Execute multi-level group operations (`groupby`) and complex cross-tabulations (`pivot_table`) for period-over-period financial aggregations.
   - Merge and join relational datasets to maintain a unified data schema.
3. **AI-Powered Feature Engineering & Extraction:**
   - Interface Python with OpenAI API / Local LLMs (Ollama) to extract structured JSON entities from raw PDF invoices (`pdfplumber`).
   - Automate category classification for raw bank transaction descriptions (e.g., POS logs).

---

## 🛠️ Stack & Libraries Used
- **Language:** Python 3.10+
- **Data Engineering:** `pandas`, `numpy`
- **Database Connection:** `pymysql`, `sqlalchemy`, MariaDB / MySQL
- **Document Parsing:** `pdfplumber`
- **AI Integration:** OpenAI API / Ollama (`requests`, `json`)

---

## 📂 Phase Folder Architecture

```text
Phase-1-Data-Manipulation-AI/
├── data/
│   ├── raw/                   # Raw CSV and PDF invoice samples
│   └── processed/             # Cleaned datasets ready for database import
├── notebooks/
│   └── 01_financial_eda.ipynb # Data exploration and transformation experiments
└── scripts/
    ├── db_reader.py           # MariaDB connection & data fetch script
    └── financial_cleaner.py    # Pipeline for cleaning and AI text classification