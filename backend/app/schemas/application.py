from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date, datetime
from app.models.application import ApplicationStatus
from typing import Literal

Status = Literal["applied", "interviewing", "offer", "rejected"]

class ApplicationCreate(BaseModel):
    company_name: str
    position: str
    date_applied: Optional[date] = None
    status: Status = "applied"
    incoming_phone: Optional[str] = None
    incoming_interview: Optional[date] = None
    notes: Optional[str] = None

class ApplicationUpdate(BaseModel):
    company_name: Optional[str] = None
    position: Optional[str] = None
    date_applied: Optional[date] = None
    status: Optional[str] = None
    incoming_phone: Optional[str] = None
    incoming_interview: Optional[date] = None
    notes: Optional[str] = None

class ApplicationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True) # can read from a SQLAlchemy Application object
    id: int
    company_name: str
    position: str
    date_applied: Optional[date] = None
    status: Status
    incoming_phone: Optional[str] = None
    incoming_interview: Optional[date] = None
    notes: Optional[str] = None
    created_at = datetime