from __future__ import annotations

from pathlib import Path

from analysis_project.load import load_csv, save_csv
from analysis_project.clean import clean_sales
from analysis_project.visualize import save_bar, save_histogram
from analysis_project.summarize import basic_profile, describe_numeric, write_summary_md

RAW = Path("data/raw/sales_messy.csv")
CLEAN = Path("data/processed/sales_clean.csv")
SUMMARY = Path("reports/sales_summary.md")

FIG1 = Path("reports/figures/sales_total_hist.png")
FIG2 = Path("reports/figures/sales_by_product.png")
FIG3 = Path("reports/figures/sales_by_city.png")


def main() -> None:
    df = load_csv(RAW)
    df_clean = clean_sales(df)

    save_csv(df_clean, CLEAN)

    # Plots
    save_histogram(df_clean, "total", FIG1)
    save_bar(df_clean, "product", "total", FIG2, top_n=10)
    save_bar(df_clean, "city", "total", FIG3, top_n=10)

    sections = [
        basic_profile(df_clean),
        describe_numeric(df_clean),
        "## Cleaning Actions Performed\n"
        "- Parsed mixed date formats (invalid dates removed).\n"
        "- Normalized `channel` values (e.g., `ONLINE`, `Online ` -> `online`).\n"
        "- Converted `quantity` and `price` to numeric (removed invalid rows).\n"
        "- Filled missing categorical fields with `unknown`.\n"
        "- Created a new feature: `total = quantity * price`.\n",
        "## Outputs\n"
        f"- Cleaned CSV: `{CLEAN}`\n"
        f"- Figures: `{FIG1}`, `{FIG2}`, `{FIG3}`\n",
    ]

    write_summary_md(SUMMARY, "Sales Dataset Analysis (Messy Data Cleaning)", sections)
    print("Sales analysis complete.")
    print(f"Saved cleaned dataset to: {CLEAN}")
    print(f"Saved summary report to: {SUMMARY}")


if __name__ == "__main__":
    main()
