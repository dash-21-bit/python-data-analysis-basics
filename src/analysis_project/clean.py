from __future__ import annotations

import pandas as pd

def clean_iris(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the iris dataset robustly:
    - normalize column names
    - auto-detect feature columns
    - ensure numeric conversion
    - remove duplicates
    """
    df = df.copy()

    # 1️⃣ Normalize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace(".", "_", regex=False)
    )

    # 2️⃣ Rename known variants to standard names
    rename_map = {
        "sepallength": "sepal_length",
        "sepalwidth": "sepal_width",
        "petallength": "petal_length",
        "petalwidth": "petal_width",
        "name": "species",
    }
    df = df.rename(columns=rename_map)

    # 3️⃣ Detect feature columns safely
    feature_cols = [
        c for c in ["sepal_length", "sepal_width", "petal_length", "petal_width"]
        if c in df.columns
    ]

    if len(feature_cols) < 4:
        raise ValueError(
            f"Expected iris feature columns not found. Found: {df.columns.tolist()}"
        )

    # 4️⃣ Convert features to numeric
    for c in feature_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # 5️⃣ Drop rows with missing feature values
    df = df.dropna(subset=feature_cols)

    # 6️⃣ Clean species column
    if "species" in df.columns:
        df["species"] = (
            df["species"]
            .astype(str)
            .str.replace("Iris-", "", regex=False)
            .str.strip()
        )

    # 7️⃣ Remove duplicates
    df = df.drop_duplicates()

    return df

def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean a messy sales dataset:
    - parse dates from mixed formats
    - normalize channel values
    - convert quantity + price to numeric
    - handle missing city/product/channel
    - compute total = quantity * price
    """
    df = df.copy()

    # Strip whitespace in string columns
    for col in ["date", "product", "city", "channel"]:
        df[col] = df[col].astype(str).str.strip()

    # Parse dates with pandas (invalid -> NaT)
    df["date"] = pd.to_datetime(df["date"], errors="coerce", dayfirst=True)

    # Normalize channel values
    df["channel"] = (
        df["channel"]
        .str.lower()
        .str.replace("-", " ", regex=False)
        .str.replace("  ", " ", regex=False)
        .str.replace("instore", "in store", regex=False)
        .str.strip()
    )

    # Convert quantity to numeric (bad values -> NaN)
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    # Convert price to numeric (remove £ if present)
    df["price"] = df["price"].astype(str).str.replace("£", "", regex=False).str.strip()
    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Fill missing categorical values with "unknown"
    for col in ["product", "city", "channel"]:
        df[col] = df[col].replace({"": "unknown", "nan": "unknown"})

    # Drop rows missing critical numeric fields
    df = df.dropna(subset=["quantity", "price"])

    # Compute total revenue
    df["total"] = df["quantity"] * df["price"]

    # Drop rows missing date if you want time-based charts
    df = df.dropna(subset=["date"])

    # Remove duplicates (same order_id)
    df = df.drop_duplicates(subset=["order_id"])

    return df
