from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.core import get_db, NotFoundError
from db.automation import (
    Automation, AutomationCreate, AutomationUpdate,
    create_db_automation, read_db_automation, 
    update_db_automation, delete_db_automation
)

router = APIRouter(prefix="/automations", tags=["automations"])

@router.post("", response_model=Automation)
def create_automation(automation: AutomationCreate, db: Session = Depends(get_db)):
    db_automation = create_db_automation(automation, db)
    return Automation(**db_automation.__dict__)

@router.get("/{automation_id}", response_model=Automation)
def read_automation(automation_id: int, db: Session = Depends(get_db)):
    try:
        db_automation = read_db_automation(automation_id, db)
        return Automation(**db_automation.__dict__)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{automation_id}", response_model=Automation)
def update_automation(
    automation_id: int, 
    automation: AutomationUpdate, 
    db: Session = Depends(get_db)
):
    try:
        db_automation = update_db_automation(automation_id, automation, db)
        return Automation(**db_automation.__dict__)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{automation_id}", response_model=Automation)
def delete_automation(automation_id: int, db: Session = Depends(get_db)):
    try:
        db_automation = delete_db_automation(automation_id, db)
        return Automation(**db_automation.__dict__)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

