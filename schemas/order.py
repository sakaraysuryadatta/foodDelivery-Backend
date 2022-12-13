from pydantic import BaseModel
from typing import List


class Order_items(BaseModel):
    name: str
    quantity: str
    price: float
    isveg: bool
    order_id: int


class Order(BaseModel):
    seller: str
    price: float
    tax: float
    discount: float
    total_price: float
    user_id: int
    seller_id: int
