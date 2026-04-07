import schedule
import time
import logging

from pipeline import run_pipeline

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def job():
    logging.info("⏰ Executando pipeline automaticamente...")
    run_pipeline()

# agenda (a cada 10 segundos só pra teste)
schedule.every(10).seconds.do(job)

logging.info("🚀 Scheduler iniciado...")

while True:
    schedule.run_pending()
    time.sleep(1)