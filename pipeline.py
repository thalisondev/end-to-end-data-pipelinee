import logging

from ingestion.load_data import load_data
from transformation.transform import transform_data
from warehouse.store import save_data

# configuração do log
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info("🚀 Iniciando pipeline")

    df = load_data("data/raw/raw_sales.csv")
    logging.info("📥 Dados carregados")

    df = transform_data(df)
    logging.info("🔄 Dados transformados")

    save_data(df)
    logging.info("💾 Dados salvos no warehouse")

    logging.info("✅ Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    run_pipeline()