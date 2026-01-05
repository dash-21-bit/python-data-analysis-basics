# python-data-analysis-basics
python-data-analysis-basics
# Python Data Analysis Basics (Beginner) — Included Datasets, Cleaning, Visualisation
**Repo:** python-data-analysis-basics  
**Author:** Adarsh Ravi (Independent / Project-Based)  
**Level:** Beginner (Python Foundations → Data Handling)  
**Tools:** Python, Pandas, NumPy, Matplotlib

---

## 1. Project Overview

This repository demonstrates practical, beginner-friendly data analysis skills using Python. Many learners stop at “watching tutorials” or “reading about data science,” but recruiters want proof that you can:

- load real datasets,
- inspect and understand columns,
- clean messy values,
- create useful visualisations,
- and produce a small written report.

This project is structured like a miniature data pipeline. It includes two datasets inside the repository, so the project is reproducible even without internet access.

### Included datasets

1. **Iris dataset (`data/raw/iris.csv`)**  
A classic dataset used for exploratory data analysis (EDA) and understanding feature distributions and class patterns. The CSV is downloaded via terminal and committed into this repo for reproducibility.

2. **Messy Sales dataset (`data/raw/sales_messy.csv`)**  
A deliberately “dirty” dataset generated locally to simulate real-world issues: missing values, inconsistent categories, invalid dates, and non-numeric price/quantity values. This is where cleaning skills are demonstrated clearly.

---

## 2. Project Goals

The goals of this repository are:

1. **Prove practical Python + Pandas skills**
   - reading CSV files
   - selecting columns
   - checking missing values
   - converting data types
   - removing duplicates

2. **Build beginner-friendly visualisations**
   - histograms
   - scatter plots
   - bar charts

3. **Create outputs that recruiters can inspect**
   - cleaned datasets saved into `data/processed/`
   - figures saved into `reports/figures/`
   - summaries saved into `reports/*.md`

4. **Follow professional structure**
   - modular code under `src/`
   - runner scripts under `scripts/`
   - clear and reproducible terminal workflow

---

## 3. Repository Structure
python-data-analysis-basics/
├── src/
│   └── analysis_project/
│       ├── init.py
│       ├── load.py
│       ├── clean.py
│       ├── visualize.py
│       └── summarize.py
├── scripts/
│   ├── generate_sales_messy.py
│   ├── run_iris_analysis.py
│   └── run_sales_analysis.py
├── data/
│   ├── raw/
│   │   ├── iris.csv
│   │   └── sales_messy.csv
│   └── processed/
│       ├── iris_clean.csv
│       └── sales_clean.csv
├── reports/
│   ├── iris_summary.md
│   ├── sales_summary.md
│   └── figures/
│       ├── iris_petal_length_hist.png
│       ├── iris_sepal_vs_petal.png
│       ├── sales_total_hist.png
│       ├── sales_by_product.png
│       └── sales_by_city.png
├── requirements.txt
├── pyproject.toml
└── README.md

This structure is intentional:
- `data/raw` is never edited manually.
- `data/processed` stores cleaned outputs.
- `reports` stores human-readable results.
- `src` keeps reusable logic separate from runner scripts.

---

## 4. Installation (Terminal Only)

### 4.1 Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

