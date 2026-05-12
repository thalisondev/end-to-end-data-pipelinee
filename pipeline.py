import logging
from ingestion.load_data import load_all_tables
from warehouse.store import save_all_tables

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info("🚀 Iniciando pipeline Olist")

    dataframes = load_all_tables()
    logging.info("📥 Todos os CSVs carregados")

    save_all_tables(dataframes)
    logging.info("💾 Todos os dados salvos no PostgreSQL")

    logging.info("✅ Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    run_pipeline()