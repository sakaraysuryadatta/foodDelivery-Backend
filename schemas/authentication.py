from pydantic import BaseModel
from typing import List, Optional


class AuthUser(BaseModel):
    name: Optional[str] = "unavailable"
    email: Optional[str] = "unavailable"
    notification_token: Optional[str] = "unavailable"
    reg_no: Optional[str] = "unavailable"
    login_token: Optional[str] = "unavailable"


# class Login_User(BaseModel):
#     email: str
#     notification_token: str
#     login_token: str
