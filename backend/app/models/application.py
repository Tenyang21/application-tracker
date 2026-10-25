from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db import Base

class Application(Base):
    __tablename__ = "applications"
    
    application_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    company_name = Column(String)
    position = Column(String)
    date_applied = Column(DateTime)
    statuses = Column(String)
    incoming_phone = Column(String)
    incoming_interview = Column(DateTime)
    notes = Column(String)
