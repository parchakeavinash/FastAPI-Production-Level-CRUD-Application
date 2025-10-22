from typing import Optional,List
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .core import DBItem, DBAutomation, NotFoundError
from datetime import datetime

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None

class Update_item(BaseModel):
    name: Optional[str] = None
    description : Optional[str] = None


def create_bulk_item(items:List[ItemCreate],session: Session) ->List[DBItem]:
    db_items = [DBItem(**item.model_dump(exclude_none=True)) for item in items]
    session.add_all(db_items)
    session.commit()
    for db_item in db_items:
        session.refresh(db_item)
    return db_items

def create_db_item(item: ItemCreate, session: Session) ->DBItem:
    db_items = DBItem(**item.model_dump(exclude_none=True))
    session.add(db_items)
    session.commit()
    session.refresh(db_items)
    return db_items

def read_db_item(item_id: int,  session : Session) ->DBItem:
    db_item = session.query(DBItem).filter(DBItem.id == item_id).first()
    if not db_item:
        raise NotFoundError(f"Item {item_id} not found")
    return db_item

def get_all_db_item(session: Session):
    return session.query(DBItem).all()

def update_db_item(item_id: int, item: Update_item, session : Session) ->DBItem:
    db_item = read_db_item(item_id, session)
    for key, value in item.model_dump(exclude_none=True).items():
        setattr(db_item,key,value)
    session.commit()
    session.refresh(db_item)
    return db_item


def delete_db_item(item_id : int, session : Session) ->DBItem:
    db_item = read_db_item(item_id, session)
    session.delete(db_item)
    session.commit()
    return db_item

def read_db_automations_for_item(item_id: int, session: Session):
    item = read_db_item(item_id, session)  # Verify item exists
    return session.query(DBAutomation).filter(DBAutomation.item_id == item_id).all()

def search_db_items(query: str, session: Session):
    return session.query(DBItem).filter(DBItem.name.ilike(f"%{query}%")).all()


