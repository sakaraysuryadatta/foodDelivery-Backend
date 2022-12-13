from pydantic import BaseModel
from typing import List


class CreateUser(BaseModel):
    name: str
    email: str
    notification_token: str
    reg_no: str
    login_token: str


class Login_User(BaseModel):
    email: str
    notification_token: str
    login_token: str
