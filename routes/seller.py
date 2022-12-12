
import  database ,models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status

router = APIRouter(
    prefix="/seller",
    tags=['Seller']
)

get_db = database.get_db


@router.post('/',)
async def create_user():
    return "user.create(request, db)"
