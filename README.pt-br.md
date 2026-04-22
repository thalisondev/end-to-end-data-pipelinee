# End-to-End Data Pipeline

Um projeto simples para simular como funciona um pipeline de dados completo (end-to-end) na prática.

Ele coleta dados de diferentes fontes (CSV e API), processa e armazena tudo de forma estruturada. A ideia aqui não é complexidade, mas sim ter clareza e controle sobre todo o fluxo.
---

## o que isso faz

- lê dados de e-commerce via CSV  
- busca dados de criptomoedas via API  
- limpa e transforma os dados  
- armazena tudo em SQLite  
- roda o pipeline automaticamente  
- registra logs do que está acontecendo  

---

## estrutura


data_pipeline/
ingestion/
processing/
storage/
utils/
data/
logs/
main.py


Nada muito complexo. Cada parte faz só o que precisa fazer.

---

## como rodar

instalar dependências:

```bash
pip install -r requirements.txt
```
rodar o pipeline:
```bash
python main.py
```
é isso.

como funciona
os dados entram (csv + api)
passam por limpeza e transformação
são salvos no sqlite
logs são gerados
o scheduler pode rodar tudo automaticamente
por que eu fiz isso

para entender como pipelines de dados funcionam na prática, não só na teoria.

a maioria dos conteúdos mostra partes isoladas. aqui a ideia foi conectar tudo de ponta a ponta.

observações

simples de propósito
fácil de modificar
feito para testar, aprender e evoluir
próximos passos
migrar para postgres
adicionar cloud (aws/gcp)
usar airflow para orquestração
criar um dashboard

contato:
Linkedin: https://www.linkedin.com/in/thalison-dev
