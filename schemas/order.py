from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    name: str
    price: float
    description: str
    photo: str


class Order(BaseModel):
    seller: str
    price: float
    tax: float
    discount: float
    total_price: float
    user_id :int

