from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url="postgresql+psycopg2://postgres:Deep%402000@localhost:5432/bookstore_db"

engine=create_engine(url)
SessionLocal=sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)
def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()

    