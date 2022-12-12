
import  database ,models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from schemas import order

router = APIRouter(
    prefix="/order",
    tags=['Order']
)

get_db = database.get_db

@router.post('/create',)
async def create_order(request:order.Order,db: Session = Depends(database.get_db)):
    new_order = models.Order(seller=request.seller,price=request.price,tax=request.tax,discount=request.discount,total_price=request.total_price,user_id=request.user_id)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order