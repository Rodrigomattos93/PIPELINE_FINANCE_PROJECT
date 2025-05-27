from datetime import datetime
from decimal import Decimal

from sqlalchemy.orm import Session

from db.ibge.models import Unemployment_Model


def insert_unployment_rate_in_postgres(
    db: Session, unemployment_list: list, period: int
):
    result = unemployment_list[0].get("resultados", [])[0]
    series = result.get("series", [])[0]
    value = series.get("serie", {}).get(str(period), None)

    existing_record = (
        db.query(Unemployment_Model)
        .filter(Unemployment_Model.quarter_year == period)
        .first()
    )

    if value and not existing_record:
        new_record = Unemployment_Model(quarter_year=period, unemployment_value=value)
        db.add(new_record)

    db.commit()
