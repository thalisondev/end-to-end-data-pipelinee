from ingestion.api_data import fetch_crypto_data
from transformation.transform_api import transform_crypto
from warehouse.store import save_crypto
from utils.logger import setup_logger
import logging

def run_api_pipeline():
    setup_logger()
    logging.info("Iniciando pipeline de API")

    df = fetch_crypto_data()

    if df is None:
        logging.error("Pipeline interrompido por erro na ingestão")
        return

    df = transform_crypto(df)

    save_crypto(df)

    logging.info("Pipeline finalizado com sucesso")

if __name__ == "__main__":
    run_api_pipeline()