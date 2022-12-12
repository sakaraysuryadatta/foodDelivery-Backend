
import  database ,models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from schemas import authentication

router = APIRouter(
    prefix="/auth",
    tags=['Authentication']
)

get_db = database.get_db


@router.post('/create',)
async def create_user(db: Session = Depends(database.get_db) ,name: str= "", email: str = "", password:str=""):
    new_user = models.User(name=name,email=email,password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
