from __future__ import annotations

from pathlib import Path
import pandas as pd


def write_summary_md(path: Path, title: str, sections: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = [f"# {title}", ""]
    content.extend(sections)
    content.append("")
    path.write_text("\n".join(content), encoding="utf-8")


def basic_profile(df: pd.DataFrame) -> str:
    lines = []
    lines.append("## Dataset Profile")
    lines.append(f"- Rows: **{len(df)}**")
    lines.append(f"- Columns: **{len(df.columns)}**")
    lines.append("")
    lines.append("### Columns")
    for c in df.columns:
        lines.append(f"- `{c}` (missing: {int(df[c].isna().sum())})")
    return "\n".join(lines)


def describe_numeric(df: pd.DataFrame) -> str:
    numeric = df.select_dtypes(include="number")
    if numeric.empty:
        return "## Numeric Summary\nNo numeric columns found."
    desc = numeric.describe().to_markdown()
    return "## Numeric Summary\n\n" + desc
