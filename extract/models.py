from sqlalchemy import Column, Numeric, DateTime, Integer
from extract.db import Base

class IPCA_Model(Base):
    __tablename__ = "ipca"

    id = Column(Integer, primary_key = True)
    date = Column(DateTime)
    ipca_value = Column(Numeric)
