import database, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from schemas import authentication

router = APIRouter(
    prefix="/auth",
    tags=['Authentication']
)

get_db = database.get_db


@router.post('')
async def auth_user(request: authentication.AuthUser = Depends(), db: Session = Depends(get_db)):
    check_user = db.query(models.User).filter(models.User.email == request.email).first()
    if not check_user:
        user_object = {
            "name": request.name,
            "email": request.email,
            "reg_no": request.reg_no,
            "notification_token": request.notification_token,
            "login_token": request.login_token
        }
        new_user = models.User(**user_object)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"result":"Account created"}

    else:
        check_user = db.query(models.User).filter(models.User.email == request.email)
        update_model = {
            "login_token": request.login_token,
            "notification_token": request.notification_token
        }
        check_user.update(update_model)
        db.commit()
        return {"result":"Account updated"}

# @router.put("/login")
# async def login(request: authentication.Login_User = Depends(), db: Session = Depends(get_db)):
#     login = db.query(models.User).filter(models.User.email == request.email)
#     update_model = {
#         "login_token": request.login_token,
#         "notification_token": request.notification_token
#     }
#     login.update(update_model)
#     db.commit()
#     return "Successfully Login"