import pandas as pd
import logging
import os

OLIST_PATH = "data/raw/olist"

TABLES = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "order_payments": "olist_order_payments_dataset.csv",
    "order_reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "category_translation": "product_category_name_translation.csv",
}

def load_all_tables():
    dataframes = {}
    for name, filename in TABLES.items():
        path = os.path.join(OLIST_PATH, filename)
        df = pd.read_csv(path)
        logging.info(f"✅ {name}: {len(df)} linhas carregadas")
        dataframes[name] = df
    return dataframes