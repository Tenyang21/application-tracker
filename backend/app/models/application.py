from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db import Base

class Application(Base):
    __tablename__ = "applications"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    company_name = Column(String, nullable=False)
    position = Column(String)
    date_applied = Column(Date)
    status = Column(String, nullable=False)
    incoming_phone = Column(String)
    incoming_interview = Column(DateTime)
    notes = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
