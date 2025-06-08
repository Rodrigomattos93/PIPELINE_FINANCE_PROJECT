from datetime import datetime

from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator

from include.extract.bacen.extract_ipca_rate import extract_inflation_from_bacen_api
from include.extract.ibge.extract_unemployment_rate import (
    extract_unemployment_from_ibge_api,
)

DBT_PROJECT_DIR = "/usr/local/airflow/pipeline_project_2"


@dag(
    start_date=datetime(2025, 1, 1),
    schedule="0 0 15 * *",
    catchup=False,
    description="Pipeline that extracts inflation and unemployment data",
    is_paused_upon_creation=True,
)
def pipeline():

    @task
    def extract_inflation_task():
        extract_inflation_from_bacen_api("01/01/2020")

    @task
    def extract_unemployment_task():
        extract_unemployment_from_ibge_api(2020)

    run_dbt = BashOperator(
        task_id="run_dbt", bash_command=f"dbt run --project-dir {DBT_PROJECT_DIR}"
    )

    t1 = extract_inflation_task()
    t2 = extract_unemployment_task()
    t3 = run_dbt

    [t1, t2] >> t3


pipeline()
