from pathlib import Path
import os

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = Path(
    os.getenv(
        "DATA_DIR",
        ROOT_DIR / "data"
    )
)

RAW_DIR = DATA_DIR / "raw"

BRONZE_DIR = DATA_DIR / "bronze"

SILVER_DIR = DATA_DIR / "silver"

GOLD_DIR = DATA_DIR / "gold"

DATASETS = {
    "orders": "olist_orders_dataset.csv",
    "customers": "olist_customers_dataset.csv",
    "products": "olist_products_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
}