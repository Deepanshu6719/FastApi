from sqlalchemy import create_engine,text
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
    
with engine.connect() as connection:
    result=connection.execute(text("SELECT 1"))
    print(result.scalar())