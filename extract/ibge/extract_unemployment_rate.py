import json
from datetime import datetime

import requests

# The API takes a parameter in the format YYYYTQ, where Y is the year and Q is the quarter

start_year = 2025
current_year = datetime.now().year
current_quarter = ((datetime.now().month - 1) // 3) + 1
current_year_quarter = (current_year * 100) + current_quarter
year_list = list(range(start_year, current_year + 1))
quarters = [1, 2, 3, 4]

period_requests_list = [
    y * 100 + q
    for y in year_list
    for q in quarters
    if y * 100 + q < current_year_quarter
]

for period in period_requests_list:
    url = f"https://servicodados.ibge.gov.br/api/v3/agregados/4099/periodos/{period}/variaveis/4099?localidades=N1[all]"

    response = requests.get(url)
    data = response.json()
    result = data[0].get("resultados", [])[0]
    series = result.get("series", [])[0]
    value = series.get("serie", {}).get(str(period), None)
