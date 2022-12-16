from typing import List

import database, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from schemas import items,user

router = APIRouter(
    prefix="/home",
    tags=['Home']
)

get_db = database.get_db


@router.get('/items', response_model=user.HomePage)
async def home_Items(db: Session = Depends(get_db)):
    sellers = db.query(models.Seller).all()
    items = db.query(models.Items).all()
    home = {
        "sellers": sellers,
        "items":items
    }
    return home
