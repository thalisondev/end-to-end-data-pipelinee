import pandas as pd
import logging

def transform_data(df):
    required_columns = ["price", "quantity", "date"]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Coluna faltando: {col}")

    df["total_value"] = df["price"] * df["quantity"]
    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna()

    df.to_csv("data/processed/processed_sales.csv", index=False)

    logging.info("Dados transformados com sucesso")

    return df