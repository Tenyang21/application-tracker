from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class ApplicationCreate(BaseModel):
    company_name: str
    position: str
    date_applied: Optional[date] = None
    statuses: Optional[str] = None
    incoming_phone: Optional[str] = None
    incoming_interview: Optional[date] = None
    notes: Optional[str] = None

class ApplicationUpdate(BaseModel):
    company_name: str
    position: str
    date_applied: Optional[date] = None
    statuses: Optional[str] = None
    incoming_phone: Optional[str] = None
    incoming_interview: Optional[date] = None
    notes: Optional[str] = None

class ApplicationResponse(BaseModel):
    _id: int = Field(alias="application_id")
    user_id: int
    company_name: str
    position: str
    date_applied: Optional[date] = None
    statuses: Optional[str] = None
    incoming_phone: Optional[str] = None
    incoming_interview: Optional[date] = None
    notes: Optional[str] = None