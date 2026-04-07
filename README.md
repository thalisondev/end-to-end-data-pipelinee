# 🚀 Data Engineering Pipeline

Projeto focado em simular um ambiente real de engenharia de dados, com pipeline automatizado, arquitetura em camadas e integração com dados externos.

## Arquitetura

O pipeline segue o modelo de camadas:

* **Raw**: dados brutos
* **Processed**: dados tratados
* **Curated**: dados prontos para análise

Fluxo:

Raw → Processed → Curated → Data Warehouse

## Tecnologias

* Python
* Pandas
* SQLite
* Logging
* Schedule
* Requests (API)

## Pipelines

### Pipeline CSV

1. Ingestão de dados CSV
2. Transformação e limpeza
3. Criação de métricas (total_value)
4. Armazenamento em banco de dados
5. Salvamento em camadas (processed e curated)

### Pipeline com API

Integração com API de criptomoedas (CoinGecko):

1. Coleta de dados em tempo real
2. Transformação dos dados
3. Armazenamento em Data Warehouse
4. Salvamento na camada curated

## Automação

O projeto possui um scheduler que executa o pipeline automaticamente em intervalos definidos.


## Análise de Dados

Inclui visualização de receita por produto, permitindo gerar insights a partir dos dados processados.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/ecommerce-data-pipeline.git
cd ecommerce-data-pipeline
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como executar

### Pipeline CSV

```bash
py pipeline.py
```

### 🌐 Pipeline API

```bash
py pipeline_api.py
```

###  Automação

```bash
py -m orchestration.scheduler
```

## Estrutura do Projeto

```
ecommerce-data-pipeline/
 ├── ingestion/
 ├── transformation/
 ├── warehouse/
 ├── orchestration/
 ├── data/
 │    ├── raw/
 │    ├── processed/
 │    └── curated/
 ├── pipeline.py
 ├── pipeline_api.py
 ├── requirements.txt
 └── README.md
```

##  Resultados

* Pipeline automatizado de dados
* Integração com API externa (dados em tempo real)
* Geração de métricas de negócio (receita total, produtos mais vendidos)
* Persistência em múltiplas camadas de dados

##  Objetivo

Simular um ambiente real de engenharia de dados, aplicando boas práticas de arquitetura, organização e automação de pipelines.