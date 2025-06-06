from datetime import datetime

import requests

from db.bacen.crud import insert_ipca_rate_in_postgres
from db.db import SessionLocal


def extract_inflation_from_bacen_api(start_date: str):
    """the string input of start_date must be in format dd/mm/yyyy"""
    series_code = 433
    end_date = datetime.today().strftime("%d/%m/%Y")
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{series_code}/dados?formato=json&dataInicial={start_date}&dataFinal={end_date}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        ipca_list = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        ipca_list = []

    if ipca_list:
        db = SessionLocal()
        insert_ipca_rate_in_postgres(db, ipca_list)
    else:
        print("No data to insert.")
