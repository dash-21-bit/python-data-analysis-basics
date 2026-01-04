from __future__ import annotations

from pathlib import Path
import random
import csv

random.seed(42)

OUT = Path("data/raw/sales_messy.csv")
OUT.parent.mkdir(parents=True, exist_ok=True)

products = ["Camera", "Tripod", "Lens", "Bag", "Filter"]
channels = ["online", "Online ", "IN-STORE", "in store", "instore", "ONLINE"]
cities = ["Manchester", "London", "Birmingham", "Leeds", ""]

def maybe_missing(value: str, p: float = 0.08) -> str:
    return "" if random.random() < p else value

def messy_date() -> str:
    # mix formats + some invalid ones
    options = [
        "2025-01-03",
        "03/01/2025",
        "2025/01/03",
        "Jan 03 2025",
        "2025-13-01",  # invalid month
        ""
    ]
    return random.choice(options)

rows = []
for i in range(250):
    product = random.choice(products)
    city = random.choice(cities)
    channel = random.choice(channels)

    qty = random.choice([1, 2, 3, 4, 5, "", "two"])  # includes bad values
    price = random.choice([49.99, 99.99, 149.99, 199.99, "", "£99.99"])  # includes currency text
    date = messy_date()

    rows.append({
        "order_id": f"ORD-{1000+i}",
        "date": maybe_missing(date, 0.05),
        "product": maybe_missing(product, 0.02),
        "city": maybe_missing(city, 0.05),
        "channel": maybe_missing(channel, 0.02),
        "quantity": qty,
        "price": price,
    })

with OUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print(f"Created: {OUT} with {len(rows)} rows")
