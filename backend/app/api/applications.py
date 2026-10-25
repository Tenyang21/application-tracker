from app.models.application import Application
from app.api.deps import get_current_user
from fastapi import APIRouter, Depends, HTTPException, status
from datetime import date

router = APIRouter()

@router.get("/api/home")
def home(current_user = Depends(get_current_user)):
    user_id = current_user["user_id"]
    db = curent_user["db"]

    applications = db.query(Application).filter(Application.user_id == user_id).all()
    total = len(applications)
    replies = len(a for a in applications if a.statuses in ["phone_screen", "interviewing", "offer"])
    rejections = len(a for a in applications if a.statuses == "rejected")
    return {
        "stats": {
            "totalApplications": total, 
            "replyRate": replies,
            "rejections": rejections
        },
        "applications": [ApplicationResponse.from_orm(app) for app in applications]
    }

@router.post("/api/edit")
def edit(application: ApplicationCreate, current_user= Depends(get_current_user)):
    user_id = curent_user["user_id"]
    db = current_user["db"]
    app = Application(user_id = application.user_id, company_name=application.company_name, position = application.position, 
    date_applied = application.date_applied, statuses = application.date_applied, incoming_phone =application.incoming_phone,
    incoming_interview = application.incoming_interview, notes = application.notes)
    db.add(app)
    db.commit(app)
    db.refresh(app)
    return {"message": "Application added successfully", "user": application.user_id}

@router.patch("api/update/{id}")
def update(id: int, application: ApplicationUpdate, current_user= Depends(get_current_user)):
    user_id = current_user["user_id"]
    db = current_user["db"]
    app = db.query(Application).filter(Application.application_id = id, Application.user_id = user_id)
    if not app:
        raise HTTPException(status_code=404)
    db.add(app)
    db.commit(app)
    db.refresh(app)
    return {"message": "Application added successfully", "user": application.user_id}

@router.delete("api/delete/{id}")
def delete(id: int, current_user= Depends(get_current_user)):
    user_id = current_user["user_id"]
    db = curent_user["db"]
    app = db.query(Application).filter(Application.application_id = id, Application.user_id = user_id)
    db.delete(app)
    db.commit(app)
    db.refresh(app)
    return {"message": "Application added successfully", "user": application.user_id}

@router.get("api/sort")
def sort(current_user = Depends(get_current_user)):
    user_id = curent_user["user_id"]
    db = curent_user["db"]
    app = db.query(Application).filter(Application.user_id = user_id, Application.statuses != "rejected", Application.incoming_phone >= date.today(), or_(Application.incoming_phone >= date.today(), Application.incoming_interview >= date.today()))
    events = []
    for a in app:
        events.append()

