# Iris Dataset Analysis

## Dataset Profile
- Rows: **147**
- Columns: **5**

### Columns
- `sepal_length` (missing: 0)
- `sepal_width` (missing: 0)
- `petal_length` (missing: 0)
- `petal_width` (missing: 0)
- `species` (missing: 0)
## Numeric Summary

|       |   sepal_length |   sepal_width |   petal_length |   petal_width |
|:------|---------------:|--------------:|---------------:|--------------:|
| count |      147       |    147        |      147       |    147        |
| mean  |        5.85646 |      3.05578  |        3.78027 |      1.20884  |
| std   |        0.8291  |      0.437009 |        1.75911 |      0.757874 |
| min   |        4.3     |      2        |        1       |      0.1      |
| 25%   |        5.1     |      2.8      |        1.6     |      0.3      |
| 50%   |        5.8     |      3        |        4.4     |      1.3      |
| 75%   |        6.4     |      3.3      |        5.1     |      1.8      |
| max   |        7.9     |      4.4      |        6.9     |      2.5      |
## Key Insights (Beginner)
- Petal measurements usually separate species better than sepal measurements.
- Visual scatter plots help detect clustering patterns quickly.
- Cleaning ensures numeric columns are valid and duplicates are removed.

## Outputs
- Cleaned CSV: `data/processed/iris_clean.csv`
- Figures: `reports/figures/iris_petal_length_hist.png`, `reports/figures/iris_sepal_vs_petal.png`

