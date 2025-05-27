from sqlalchemy import Column, Integer, Numeric, String

from db.db import Base


class Unemployment_Model(Base):
    __tablename__ = "unemployment"

    id = Column(Integer, primary_key=True)
    quarter_year = Column(String)
    unemployment_value = Column(Numeric)
