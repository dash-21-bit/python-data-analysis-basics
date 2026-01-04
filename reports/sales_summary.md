# Sales Dataset Analysis (Messy Data Cleaning)

## Dataset Profile
- Rows: **21**
- Columns: **8**

### Columns
- `order_id` (missing: 0)
- `date` (missing: 0)
- `product` (missing: 0)
- `city` (missing: 0)
- `channel` (missing: 0)
- `quantity` (missing: 0)
- `price` (missing: 0)
- `total` (missing: 0)
## Numeric Summary

|       |   quantity |    price |   total |
|:------|-----------:|---------:|--------:|
| count |   21       |  21      |  21     |
| mean  |    3.38095 | 102.371  | 361.871 |
| std   |    1.49921 |  40.2374 | 248.938 |
| min   |    1       |  49.99   |  49.99  |
| 25%   |    3       |  99.99   | 149.97  |
| 50%   |    3       |  99.99   | 299.97  |
| 75%   |    5       |  99.99   | 499.95  |
| max   |    5       | 199.99   | 999.95  |
## Cleaning Actions Performed
- Parsed mixed date formats (invalid dates removed).
- Normalized `channel` values (e.g., `ONLINE`, `Online ` -> `online`).
- Converted `quantity` and `price` to numeric (removed invalid rows).
- Filled missing categorical fields with `unknown`.
- Created a new feature: `total = quantity * price`.

## Outputs
- Cleaned CSV: `data/processed/sales_clean.csv`
- Figures: `reports/figures/sales_total_hist.png`, `reports/figures/sales_by_product.png`, `reports/figures/sales_by_city.png`

