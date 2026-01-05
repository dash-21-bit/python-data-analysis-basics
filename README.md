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
### 4.2 Install Dependencies
```
pip install -r requirements.txt
```
### 4.3 Install the package in editable mode
```
pip install -e .
```
## 5. Dataset Preparation

### 5.1 Iris dataset

The Iris CSV is stored in:
	•	data/raw/iris.csv

This dataset is small and classic, making it ideal for:
	•	learning EDA,
	•	plotting distributions,
	•	exploring separation between classes.

### 5.2 Messy sales dataset

The messy sales dataset is generated locally and saved to:
	•	data/raw/sales_messy.csv

This dataset intentionally includes:
	•	mixed date formats (some invalid),
	•	“quantity” values that include text like two,
	•	“price” values that include £99.99,
	•	inconsistent channel categories (ONLINE vs Online vs in store),
	•	missing city/product entries.

These are typical real-world data problems.

To regenerate it:
```
python scripts/generate_sales_messy.py
```
## 6. Analysis Workflow

This project follows a beginner-friendly workflow:
	1.	Load CSV
	2.	Inspect structure
	3.	Clean data (types, missing values, duplicates)
	4.	Create visualisations
	5.	Save cleaned outputs
	6.	Write a summary report

Each dataset has its own runner script:
	•	scripts/run_iris_analysis.py
	•	scripts/run_sales_analysis.py
## 7. Running the Iris Analysis
   Run:
   ```
	python scripts/run_iris_analysis.py
   ```
Outputs created:

	1.	Cleaned dataset

	•	data/processed/iris_clean.csv
	
	2.	Figures:
	•	reports/figures/iris_petal_length_hist.png
	•	reports/figures/iris_sepal_vs_petal.png
	3.	Summary report:
	•	reports/iris_summary.md
	
## 8. Running the Messy sales analysis
Run:
```
python scripts/run_sales_analysis.py
```

Outputs created
	
	1.	Cleaned dataset:

	•	data/processed/sales_clean.csv
	2.	Figures:

	•	reports/figures/sales_total_hist.png
	•	reports/figures/sales_by_product.png
	•	reports/figures/sales_by_city.png

	3.	Summary report:

	•	reports/sales_summary.md

Cleaning actions performed

This analysis includes real-world cleaning steps:
	•	Date parsing
	•	Mixed formats are parsed.
	•	Invalid dates are converted to missing and removed.
	•	Category normalization
	•	ONLINE, Online  → online
	•	IN-STORE, instore → in store
	•	Numeric conversion
	•	quantity converted to numeric; text like two is removed.
	•	price converted to numeric after stripping currency symbols.
	•	Missing values
	•	Missing city/product/channel filled with unknown.
	•	Feature engineering
	•	total = quantity * price

These are the types of steps that appear in real analyst / data roles.

⸻

## 9. Design Explanation (Modular Code)

### 9.1 load.py

Contains simple reusable functions:
	•	load_csv(path) reads a CSV.
	•	save_csv(df, path) writes output without index.

### 9.2 clean.py

Separates cleaning logic per dataset:
	•	clean_iris(df) handles column naming, numeric conversion, duplicates.
	•	clean_sales(df) handles real-world messy strings, date parsing, standardization, and feature engineering.

### 9.3 visualize.py

Contains reusable plotting functions:
	•	histogram
	•	scatter (optional grouping by category)
	•	bar chart for top categories

All figures are saved to disk so the project is portfolio-friendly.

### 9.4 summarize.py

Builds a simple Markdown report:
	•	dataset profile (rows, columns, missing counts)
	•	numeric summary stats table
	•	beginner-friendly insights

⸻

## 10. Validation and Testing Approach

This is a beginner project, so validation is practical:
	1.	Run scripts and ensure output files are created.
	2.	Confirm data/processed/*.csv exists and opens correctly.
	3.	Confirm reports/figures/*.png exists and renders correctly.
	4.	Confirm summaries contain row counts and numeric descriptions.

Manual checks:
	•	The cleaned sales dataset should have numeric quantity, price, and computed total.
	•	The cleaned iris dataset should have numeric feature columns and a consistent species column.

⸻

##11. Limitations
	•	No automated unit tests (can add with pytest later).
	•	Sales dataset is synthetic (generated), not from a real business system.
	•	The plotting is minimal and designed for clarity rather than advanced styling.

These limitations are acceptable for beginner level and can be improved in later levels.

⸻

##12. Future Improvements
	•	Add pytest tests for cleaning functions.
	•	Add command-line interface to select dataset and output paths.
	•	Add more plots (boxplots, correlation heatmaps).
	•	Add outlier detection (IQR / z-score).
	•	Add a single combined HTML report output.
