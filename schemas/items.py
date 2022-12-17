from pydantic import BaseModel


class HomeSeller(BaseModel):
    index: int
    name: str
    location: str
    photo: str

    class Config():
        orm_mode = True


class HomeItems(BaseModel):
    name: str
    price: int
    description: str
    photo: str
    seller: HomeSeller

    class Config():
        orm_mode = True
