import logging
from sqlalchemy import create_engine, text

DB_URL = "postgresql://olist_user:olist_pass@localhost:5432/olist_db"

def get_engine():
    return create_engine(DB_URL)

def save_all_tables(dataframes):
    engine = get_engine()
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS raw"))
    
    for name, df in dataframes.items():
        df.to_sql(name, engine, schema="raw", if_exists="replace", index=False)
        logging.info(f"✅ Tabela 'raw.{name}' salva no PostgreSQL")