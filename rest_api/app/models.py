from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String, nullable=True)
    email = Column(String, unique=True)
    gender = Column(String, nullable=True)
    ip_address = Column(String, nullable=True)
    country_code = Column(String, nullable=True)
