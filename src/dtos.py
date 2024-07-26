from pydantic import BaseModel

class UserLogin(BaseModel):
    email:str
    password:str

class Register(BaseModel):
    name:str
    email: str
    password: str
