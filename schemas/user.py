from typing import List
from pydantic import BaseModel
from schemas import order

class OrderItem(BaseModel):
    name: str
    price: float
    quantity:int
    isveg:bool
    class Config():
        orm_mode = True

class Order(BaseModel):
    seller: str
    price: float
    tax: float
    discount: float
    total_price: float
    user_id :int
    items:List[OrderItem]
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name: str
    email: str
    orders : List[Order]

    class Config():
        orm_mode = True
