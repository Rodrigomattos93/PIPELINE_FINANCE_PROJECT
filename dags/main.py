import os
from datetime import datetime

from airflow.decorators import dag, task
from extract.bacen.extract_ipca_rate import extract_inflation_from_bacen_api
from extract.ibge.extract_unemployment_rate import \
    extract_unemployment_from_ibge_api


@dag(
    start_date=datetime(2025, 1, 1),
    schedule="*/1 * * * *",
    catchup=False,
    description="Pipeline that extracts inflation and unemployment data",
)
def pipeline():

    @task
    def extract_inflation_task():
        extract_inflation_from_bacen_api("01/01/2020")

    @task
    def extract_unemployment_task():
        extract_unemployment_from_ibge_api(2020)

    @task
    def run_dbt_task():
        os.chdir(os.path.join(os.path.dirname(__file__), "..", "pipeline_project_2"))
        exit_code = os.system("dbt run")
        if exit_code != 0:
            raise Exception("dbt run failed")

    t1 = extract_inflation_task()
    t2 = extract_unemployment_task()
    t3 = run_dbt_task()

    [t1, t2] >> t3


pipeline()
