from datetime import datetime
from decimal import Decimal

from sqlalchemy.orm import Session

from db.bacen.models import IPCA_Model


def insert_ipca_rate_in_postgres(db: Session, ipca_list: list):
    for item in ipca_list:
        iterated_date = datetime.strptime(item["data"], "%d/%m/%Y")
        iterated_value = Decimal(item["valor"].replace(",", "."))

        existing_record = (
            db.query(IPCA_Model).filter(IPCA_Model.date == iterated_date).first()
        )

        if not existing_record:
            new_record = IPCA_Model(date=iterated_date, ipca_value=iterated_value)
            db.add(new_record)

    db.commit()
