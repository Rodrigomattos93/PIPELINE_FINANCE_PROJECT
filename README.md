# 📊 Data Pipeline Project with Airflow, dbt, Public APIs, and Power BI

This project automates the collection, transformation, and visualization of key economic indicators from Brazil, using a modern stack including Docker, Poetry, Airflow, dbt, and Power BI.

## Overview

- **Public APIs used**:  
  - IBGE: Unemployment data  
  - BACEN: IPCA (inflation index)

- **Database**: PostgreSQL (AWS RDS)

- **Data transformations**: dbt (running inside the Airflow container)

- **Orchestration**: Apache Airflow (via Astro CLI), scheduled monthly (on the 15th)

- **Visualization**: Power BI connected to the final dbt table

- **Code quality**: `pre-commit`, `black`, `isort`

---

## Directory Structure
```
project-root
├───.astro
├───.venv
├───dags
├───db
│   ├───bacen
│   ├───ibge
├───include
│   ├───.dbt
│   └───extract
│       ├───bacen
│       ├───ibge
├───pipeline_project_2
    ├───models
        ├───intermediate
        ├───marts
        └───staging
            ├───bacen_api
            └───ibge_api
```


---

## Prerequisites

- [Docker](https://www.docker.com/)
- [Poetry](https://python-poetry.org/)
- [Astro CLI](https://docs.astronomer.io/astro/cli/install-cli) (to run Airflow in container)

---

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/Rodrigomattos93/PIPELINE_FINANCE_PROJECT.git
cd PIPELINE_FINANCE_PROJECT
```

### 2. Install dependencies with poetry
```bash
poetry env use 3.12.1
poetry env activate
poetry install
poetry run pre-commit install
```

### 3. Start services with Docker + Astro CLI (Windows)
```bash
winget install -e --id Astronomer.Astro
astro dev init
astro dev start
```
For installation instructions on other operating systems, visit the official Astro CLI documentation:  
[https://www.astronomer.io/docs/astro/cli/install-cli](https://www.astronomer.io/docs/astro/cli/install-cli)

### Environment Variables

The project uses `.env` files to manage secrets and configurations. Make sure to create the following:

- `.env` in the project root (for global configs)
```
DB_NAME_DEV=...
DB_HOST_DEV=...
DB_PASS_DEV=...
DB_PORT_DEV=...
DB_SCHEMA_DEV=...
DB_THREADS_DEV=...
DB_USER_DEV=...
```
- `.env` inside `db/` (for DB-specific configs)
```
DB_USER=...
DB_PASS=...
DB_HOST=...
DB_PORT=...
DB_NAME=...
```
- `.env` inside `pipeline_project_2/` (for dbt configs)
```
DB_NAME_DEV=
DB_HOST_DEV=
DB_PASS_DEV=
DB_PORT_DEV=
DB_SCHEMA_DEV=
DB_THREADS_DEV=
DB_USER_DEV=
DBT_PROFILES_DIR=../
```
These files are not tracked by Git, so you must create them manually.


### Automated Monthly Update
Airflow runs the DAG automatically on the 15th of every month

Data is extracted from APIs, loaded into PostgreSQL, transformed with dbt, and visualized via Power BI

### Code Conventions

- Code formatted with black
- Imports organized with isort
- Automatic validation with pre-commit

### Power BI
Power BI consumes the final table created by dbt, ensuring transformations are audited and version-controlled.
![Dashboard Preview](https://github.com/Rodrigomattos93/PIPELINE_FINANCE_PROJECT/blob/main/images/PowerBI.png)



### Author
Rodrigo Mattos
rodrigo.mattos.rocha@poli.ufrj.br
