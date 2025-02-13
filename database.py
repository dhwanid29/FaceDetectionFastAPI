from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import exc  # Import the exception module if not already imported

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/poc_bulk_image_upload"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost/poc_bulk_image_upload"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
