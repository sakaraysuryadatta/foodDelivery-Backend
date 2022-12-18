from typing import List

import database, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from schemas import seller

router = APIRouter(
    prefix="/seller",
    tags=['Seller']
)

get_db = database.get_db





@router.post('/create/item')
async def create_item(request: seller.Items = Depends(),
                      db: Session = Depends(get_db)):
    item_obejct = {
        "name": request.name,
        "price": request.price,
        "description": request.description,
        "photo": request.photo,
        "seller_id": request.seller_id
    }
    new_item = models.Items(**item_obejct)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return "item created"


@router.get("/getseller/{id}",response_model = seller.Seller)
async def get_Seller_by_id(id: int, db: Session = Depends(get_db)):
    seller = db.query(models.Seller).filter(models.Seller.index == id).first()
    return seller


@router.get("/getsellers", response_model=List[seller.GetSellers])
async def get_Sellers(db: Session = Depends(get_db)):
    sellers = db.query(models.Seller).all()
    return sellers
