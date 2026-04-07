import sqlite3
import logging

def save_data(df):
    conn = sqlite3.connect("data/warehouse.db")

    df.to_csv("data/curated/curated_sales.csv", index=False)
    df.to_sql("sales_curated", conn, if_exists="replace", index=False)

    conn.close()

    logging.info("Dados salvos na camada curated")

def save_crypto(df):
    if df is None:
        logging.error("DataFrame vazio. Nada para salvar.")
        return

    conn = sqlite3.connect("data/warehouse.db")

    df.to_csv("data/curated/crypto_data.csv", index=False)
    df.to_sql("crypto_data", conn, if_exists="replace", index=False)

    conn.close()

    logging.info("Dados de crypto salvos com sucesso")