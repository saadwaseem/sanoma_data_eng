from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import inspect

database_url = os.getenv("DATABASE_URL", "sqlite:///./db/test.db")
engine = create_engine(database_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    inspector = inspect(engine)
    if not inspector.has_table("users"):
        print("Initializing database schema...")
        Base.metadata.create_all(bind=engine)
    else:
        print("Database already initialized.")
