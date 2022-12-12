from typing import List

import database, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status
from schemas import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db


@router.get('/getuser/{user_id}',response_model=user.ShowUser)
async def get_user_by(user_id:int,db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id==user_id).first()
    return user

@router.get('/getusers',response_model=List[user.ShowUser])
async def get_users(db: Session = Depends(database.get_db)):
    user = db.query(models.User).all()
    return user