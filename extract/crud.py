from sqlalchemy.orm import Session
from extract.models import IPCA_Model
from datetime import datetime
from decimal import Decimal

def inserir_ipca(db: Session, ipca_lista: list):
    for item in ipca_lista:
        data_iterada = datetime.strptime(item['data'], "%d/%m/%Y")
        valor_iterado = Decimal(item['valor'].replace(',', '.'))

        existente = db.query(IPCA_Model).filter(IPCA_Model.date == data_iterada).first()

        if not existente:
            valor_inserido = IPCA_Model(date = data_iterada, ipca_value = valor_iterado)
            db.add(valor_inserido)
    
    db.commit()

