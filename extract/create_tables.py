from extract.db import engine, Base
import extract.models

Base.metadata.create_all(bind=engine)