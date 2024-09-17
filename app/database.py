from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://victus:NMMHWlAFIuIA9FyTkuH3naH2xYYrFA91@dpg-crkg81ogph6c73c9ofcg-a.oregon-postgres.render.com/restaraunt')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

connection = engine.connect()
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

