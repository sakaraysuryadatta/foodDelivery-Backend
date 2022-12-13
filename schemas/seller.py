from pydantic import BaseModel
from typing import List


class Items(BaseModel):
    name: str
    price: int
    description: str
    photo: str
    seller_id: int

    class Config():
        orm_mode = True


class Seller(BaseModel):
    id: int
    name: str
    location: str
    email: str
    photo: str
    items: List[Items] = []

    class Config():
        orm_mode = True


class GetSellers(BaseModel):
    id: int
    name: str
    location: str
    email: str
    photo: str

    class Config():
        orm_mode = True


class CreateSeller(BaseModel):
    name: str
    location: str
    email: str
    password: str
    photo: str

    class Config():
        orm_mode = True
