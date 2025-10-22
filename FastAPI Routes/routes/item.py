from fastapi import APIRouter, HTTPException, Request, Depends
from sqlalchemy.orm import Session
from db.core import get_db, NotFoundError
from db.items import (
    Item, ItemCreate, Update_item,
    create_db_item, read_db_item, update_db_item, delete_db_item,
    read_db_automations_for_item,get_all_db_item,search_db_items,
    create_bulk_item
    
)
from db.automation import Automation
from .limiter import limiter
from typing import List
from fastapi import status

#route initilization
router = APIRouter(prefix="/items", tags=["items"])

@router.post('/bulk',response_model=List[Item],status_code=status.HTTP_201_CREATED)
@limiter.limit("10/minute")
def create_items_bulk(request:Request, items: List[ItemCreate],db:Session = Depends(get_db)) -> List[Item]:
    db_items = create_bulk_item(items = items,session=db)
    return [Item(**item.__dict__) for item in db_items]

@router.post('/',response_model=Item)
@limiter.limit('10/minutes')
def create_item(request: Request, item: ItemCreate, db: Session = Depends(get_db)):
    db_item  = create_db_item(item, db) # orm response
    return Item(**db_item.__dict__) # json response

@router.get('/search',response_model=List[Item])
@limiter.limit("30/minute")
def search_items(request: Request, q: str, db: Session = Depends(get_db)):
    db_items = search_db_items(query= q,  session=db)
    return [Item(**item.__dict__) for item in db_items]


@router.get('/{item_id}',response_model=Item)
@limiter.limit("10/minute")
def read_item(request: Request, item_id: int, db: Session = Depends(get_db)):
    try:
        db_item = read_db_item(item_id, db)
        return Item(**db_item.__dict__)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.get("/{item_id}/automations", response_model=list[Automation])
@limiter.limit("30/minute")
def read_item_automations(request: Request, item_id: int, db: Session = Depends(get_db)):
    try:
        automations = read_db_automations_for_item(item_id, db)
        return [Automation(**auto.__dict__) for auto in automations]
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.get("/", response_model=List[Item])
@limiter.limit("30/minute")
def get_all_items(request: Request, db: Session = Depends(get_db)):
    db_item = get_all_db_item(session= db)  
    return [Item(**item.__dict__) for item in db_item]


    
@router.put("/{item_id}",response_model=Item)
@limiter.limit("10/minute")
def update_item(request: Request, item_id: int, item: Update_item,db:Session =Depends(get_db)):
    try:
        db_item  = update_db_item(item_id, item,db)
        return Item(**db_item.__dict__)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    

@router.delete("/{item_id}", response_model=Item)
@limiter.limit("10/minute")
def delete_item(request: Request, item_id: int, db: Session = Depends(get_db)):
    try:
        db_item = delete_db_item(item_id, db)
        return Item(**db_item.__dict__)
    except NotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
