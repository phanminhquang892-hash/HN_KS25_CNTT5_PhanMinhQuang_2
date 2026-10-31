from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQL_ALCHEMY_URL = 'mysql+pymysql://root:123456@localhost:3306/phone_store_db'
engine = create_engine(SQL_ALCHEMY_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
