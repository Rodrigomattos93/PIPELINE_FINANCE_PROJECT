from datetime import datetime

import requests

from extract.crud import inserir_ipca
from extract.db import SessionLocal

codigo_serie = 433
dataInicial = "01/01/2024"
dataFinal = datetime.today().strftime("%d/%m/%Y")
url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={dataInicial}&dataFinal={dataFinal}"
response = requests.get(url)
lista_ipca = response.json()

db = SessionLocal()
inserir_ipca(db, lista_ipca)
