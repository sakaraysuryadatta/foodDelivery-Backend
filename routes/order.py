import database, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from schemas import order

router = APIRouter(
    prefix="/order",
    tags=['Order']
)

get_db = database.get_db


@router.post('/create')
async def create_order(request: order.Order = Depends(), db: Session = Depends(get_db)):
    order_oject = {
        "seller": request.seller,
        "price": request.price,
        "tax": request.tax,
        "discount": request.discount,
        "total_price": request.total_price,
        "user_id": request.user_id,
        "seller_id": request.seller_id
    }
    new_order = models.Order(**order_oject)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return {"order_id": new_order.id}


@router.post('/create/item')
async def create_order_item(request: order.Order_items = Depends(), db: Session = Depends(get_db)):
    order_item_oject = {
        "name": request.name,
        "price": request.price,
        "quantity": request.quantity,
        "isveg": request.isveg,
        "order_id": request.order_id,
    }
    new_order_item = models.OrderItem(**order_item_oject)
    db.add(new_order_item)
    db.commit()
    db.refresh(new_order_item)
    return "Order item created"
