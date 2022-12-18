from typing import List
from pydantic import BaseModel
from schemas import items, seller
from schemas.items import HomeItems


class OrderItem(BaseModel):
    name: str
    price: float
    quantity: int
    isveg: bool

    class Config():
        orm_mode = True


class Order(BaseModel):
    seller: str
    price: float
    tax: float
    discount: float
    total_price: float
    user_id: int
    items: List[OrderItem]

    class Config():
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    notification_token: str
    login_token: str

    class Config():
        orm_mode = True


class login(BaseModel):
    notification_token: str
    login_token: str

    class Config():
        orm_mode = True


class ShowUser(BaseModel):
    index: int
    name: str
    email: str
    reg_no: str
    orders: List[Order]

    class Config():
        orm_mode = True
class ShowOrders(BaseModel):
    orders: List[Order]

    class Config():
        orm_mode = True

class HomePage(BaseModel):
    sellers: List[seller.GetSellers]
    items: List[items.HomeItems]

    class Config():
        orm_mode = True

class Items(BaseModel):
    name: str
    price: int
    description: str
    photo: str
    seller_id: int

    class Config():
        orm_mode = True
class Search(BaseModel):
    results: List[Items]

    class Config():
        orm_mode = True