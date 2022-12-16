from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import seller
import database
import models

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

get_db = database.get_db

@router.post('/create')
async def create_seller(password: str,request: seller.CreateSeller = Depends(), db: Session = Depends(get_db)):
    if password == "romioisno1":
        seller = {
            "name": request.name,
            "location": request.location,
            "email": request.email,
            "password": request.password,
            "photo": request.photo
        }
        new_seller = models.Seller(**seller)
        db.add(new_seller)
        db.commit()
        db.refresh(new_seller)
        return "Seller created"
    else:
        return "Wrong Password"

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
