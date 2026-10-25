from sqlalchemy import Column, Integer, String, DateTime
from app.db import Base

# this class represents a db table
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)