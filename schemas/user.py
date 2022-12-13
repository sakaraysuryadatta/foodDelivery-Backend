from typing import List
from pydantic import BaseModel
from schemas import order


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
    id: int
    name: str
    email: str
    reg_no: str
    orders: List[Order]

    class Config():
        orm_mode = True
