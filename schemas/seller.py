from pydantic import BaseModel
from typing import List


class Items(BaseModel):
    name: str
    price: int
    description: str
    photo: str


class Seller(BaseModel):
    name: str
    location: str
    email: str
    password: str
    photo: str
    items = List[Items] = []

    class Config():
        orm_mode = True
