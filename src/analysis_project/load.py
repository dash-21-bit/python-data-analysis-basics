from __future__ import annotations

from pathlib import Path
import pandas as pd


def load_csv(path: Path) -> pd.DataFrame:
    """
    Load a CSV into a pandas DataFrame.
    """
    return pd.read_csv(path)


def save_csv(df: pd.DataFrame, path: Path) -> None:
    """
    Save a DataFrame to CSV (no index column).
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
