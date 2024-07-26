from pydantic import BaseModel

class User(BaseModel):
    name:str
    email: str
    password: str
    is_employee:bool

users_model : list[User]=[
    User(name="andre",email="andre@bionutri.com", password="123", is_employee=True)
]

