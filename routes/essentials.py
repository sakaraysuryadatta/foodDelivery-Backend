from typing import List

import database, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from schemas import items

router = APIRouter(
    prefix="/home",
    tags=['Home']
)

get_db = database.get_db


@router.get('/items', response_model=List[items.HomeItems])
async def home_Items(db: Session = Depends(get_db)):
    items = db.query(models.Items).all()
    return items
