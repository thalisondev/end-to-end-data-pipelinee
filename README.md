# End-to-End Data Pipeline

A simple project to simulate how a real end-to-end data pipeline works.

It ingests data from different sources (CSV and API), processes it, and stores everything in a structured database. The goal here is not complexity, but clarity and control over the whole pipeline.

---

## what this does

- reads e-commerce data from CSV  
- fetches crypto data from an API  
- cleans and transforms the data  
- stores everything in SQLite  
- runs the pipeline automatically  
- logs what’s happening  

---

## structure


data_pipeline/
 ingestion/
 processing/
 storage/
 utils/
 data/
 logs/
 main.py


Nothing fancy. Each part does one job.

---

## quick start

install dependencies:

```bash
pip install -r requirements.txt

run the pipeline:

python main.py

that’s it.

how it works
 data comes in (csv + api)
 gets cleaned and transformed
 saved into sqlite
 logs are generated
 scheduler can run everything automatically

why i built this

to understand how data pipelines actually work in practice, not just in theory.

most tutorials show isolated pieces. this connects everything end-to-end.

notes
 simple by design
 easy to modify
 meant to be hacked and extended
 next steps
 move storage to postgres
 add cloud (aws/gcp)
 use airflow for orchestration
 add a dashboard

other languages

🇧🇷 Portuguese: README.pt-br.md

contact

linkedin: https://www.linkedin.com/in/thalison-dev
