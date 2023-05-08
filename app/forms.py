from pydantic import BaseModel
from typing import Optional


class UserLoginForm(BaseModel): # обрабатывает то, что нам пришлет клиент в логин
    email: str
    password: str


class UserCreateForm(BaseModel):
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    nick_name: Optional[str] = None
