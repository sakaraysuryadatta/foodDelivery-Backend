from pydantic import BaseModel
from typing import List


class SignUp(BaseModel):
    name :str
    email :str
    password :str