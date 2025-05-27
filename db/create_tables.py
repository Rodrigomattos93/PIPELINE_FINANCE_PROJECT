import db.bacen.models
import db.ibge.models
from db.db import Base, engine

Base.metadata.create_all(bind=engine)
