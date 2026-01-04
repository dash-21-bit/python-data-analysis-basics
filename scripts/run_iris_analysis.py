from __future__ import annotations

from pathlib import Path

from analysis_project.load import load_csv, save_csv
from analysis_project.clean import clean_iris
from analysis_project.visualize import save_histogram, save_scatter
from analysis_project.summarize import basic_profile, describe_numeric, write_summary_md

RAW = Path("data/raw/iris.csv")
CLEAN = Path("data/processed/iris_clean.csv")
SUMMARY = Path("reports/iris_summary.md")

FIG1 = Path("reports/figures/iris_petal_length_hist.png")
FIG2 = Path("reports/figures/iris_sepal_vs_petal.png")


def main() -> None:
    df = load_csv(RAW)
    df_clean = clean_iris(df)

    save_csv(df_clean, CLEAN)

    # Plots
    save_histogram(df_clean, "petal_length", FIG1)
    save_scatter(df_clean, "sepal_length", "petal_length", FIG2, color_by="species")

    sections = [
        basic_profile(df_clean),
        describe_numeric(df_clean),
        "## Key Insights (Beginner)\n"
        "- Petal measurements usually separate species better than sepal measurements.\n"
        "- Visual scatter plots help detect clustering patterns quickly.\n"
        "- Cleaning ensures numeric columns are valid and duplicates are removed.\n",
        "## Outputs\n"
        f"- Cleaned CSV: `{CLEAN}`\n"
        f"- Figures: `{FIG1}`, `{FIG2}`\n",
    ]

    write_summary_md(SUMMARY, "Iris Dataset Analysis", sections)
    print("Iris analysis complete.")
    print(f"Saved cleaned dataset to: {CLEAN}")
    print(f"Saved summary report to: {SUMMARY}")


if __name__ == "__main__":
    main()
