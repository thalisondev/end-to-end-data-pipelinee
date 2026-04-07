import requests
import pandas as pd
import logging

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        df = pd.DataFrame(data)

        df = df[["name", "symbol", "current_price", "market_cap"]]

        logging.info("🌐 Dados da API carregados com sucesso")

        return df

    except Exception as e:
        logging.error(f"Erro ao buscar dados da API: {e}")
        return None