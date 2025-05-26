import extract.models
from extract.db import Base, engine

Base.metadata.create_all(bind=engine)
