from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
import models

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

get_db = database.get_db


@router.post("/clearall")
async def clear_records(password: str, db: Session = Depends(get_db)):
    if password == "romioisno1":
        users = db.query(models.User).delete()
        sellers = db.query(models.Seller).delete()
        orders = db.query(models.Order).delete()
        order_items = db.query(models.OrderItem).delete()
        items = db.query(models.Items).delete()
        db.commit()
        return "Done"
    else:
        return "Wrong Password"
