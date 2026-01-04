from __future__ import annotations

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def save_histogram(df: pd.DataFrame, column: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure()
    df[column].plot(kind="hist", bins=20)
    plt.title(f"Histogram: {column}")
    plt.xlabel(column)
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def save_scatter(df: pd.DataFrame, x: str, y: str, out_path: Path, color_by: str | None = None) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure()

    if color_by and color_by in df.columns:
        for label, sub in df.groupby(color_by):
            plt.scatter(sub[x], sub[y], label=str(label), alpha=0.7)
        plt.legend(title=color_by)
    else:
        plt.scatter(df[x], df[y], alpha=0.7)

    plt.title(f"Scatter: {x} vs {y}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def save_bar(df: pd.DataFrame, group_col: str, value_col: str, out_path: Path, top_n: int = 10) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    summary = (
        df.groupby(group_col)[value_col]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
    )

    plt.figure()
    summary.plot(kind="bar")
    plt.title(f"Top {top_n}: {group_col} by {value_col} sum")
    plt.xlabel(group_col)
    plt.ylabel(f"Sum of {value_col}")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()
