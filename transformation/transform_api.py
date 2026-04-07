def transform_crypto(df):
    df["symbol"] = df["symbol"].str.upper()

    print(" Dados da API transformados!")

    return df