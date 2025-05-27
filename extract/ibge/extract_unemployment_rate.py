from datetime import datetime

import requests

from db.db import SessionLocal
from db.ibge.crud import insert_unployment_rate_in_postgres

# The API takes a parameter in the format YYYYTQ, where Y is the year and Q is the quarter

START_YEAR = 2020
current_year = datetime.now().year
current_quarter = ((datetime.now().month - 1) // 3) + 1
current_year_quarter = (current_year * 100) + current_quarter
year_list = list(range(START_YEAR, current_year + 1))
QUARTERS = [1, 2, 3, 4]

period_requests_list = [
    y * 100 + q
    for y in year_list
    for q in QUARTERS
    if y * 100 + q < current_year_quarter
]

for period in period_requests_list:
    url = f"https://servicodados.ibge.gov.br/api/v3/agregados/4099/periodos/{period}/variaveis/4099?localidades=N1[all]"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data_list = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from API: {e}")
        data_list = []

    if data_list:
        db = SessionLocal()
        insert_unployment_rate_in_postgres(db, data_list, period)
    else:
        print("No data to insert.")
