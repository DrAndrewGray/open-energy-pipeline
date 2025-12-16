# open-energy-pipeline

End-to-end data engineering project that ingests open energy and weather data, 
loads it into a DuckDB-based warehouse, and models it with dbt to create an 
analytics-friendly schema (staging → core marts). 

The goal is to demonstrate a modern, reproducible data stack:
- Python for ingestion and orchestration
- DuckDB as an embedded analytics warehouse
- dbt for transformations and data modelling
- Basic tests and documentation

> This project is designed as a portfolio piece to showcase practical data 
> engineering skills: building reliable pipelines rather than one-off scripts.

---

## Architecture

**High level:**

1. **Ingestion (Python)**
   - Fetch raw energy and weather data from open data sources or local CSVs.
   - Validate and normalise the payloads.
   - Store raw data in DuckDB `raw_*` tables.

2. **Warehouse (DuckDB)**
   - Single `energy.duckdb` file in `data/warehouse/`.
   - Schemas:
     - `raw_*` for ingested data
     - `stg_*` for cleaned, typed staging models
     - `dim_*` / `fact_*` for the analytics layer

3. **Transformations (dbt)**
   - `staging` models: type casting, renaming, basic cleaning.
   - `core` models: 
     - `dim_date`, `dim_region`
     - `fact_energy_daily` (e.g. daily energy usage / production per region)

4. **Orchestration**
   - A local Python orchestration script that runs:
     - ingestion → DuckDB load → `dbt run` → `dbt test`.
   - Can later be turned into an Airflow DAG or Prefect flow.

5. **Analytics / Exploration**
   - Jupyter notebook(s) in `src/open_energy_pipeline/notebooks/` to:
     - Run example queries against the warehouse.
     - Plot simple relationships (e.g. energy vs. temperature over time).

---

## Tech stack

- **Python** (3.10+): `pandas`, `requests`, `duckdb`, `pydantic`, `pyyaml`, `loguru` or `logging`
- **DuckDB**: columnar OLAP database, stored as a single file.
- **dbt Core**: SQL-based transformations and testing.
- **pytest**: basic unit tests for ingestion logic.

---

## Getting started

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/open-energy-pipeline.git
cd open-energy-pipeline
