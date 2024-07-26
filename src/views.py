from fastapi import APIRouter, Response
import controllers 
import models
import dtos

router = APIRouter()

@router.post("/users")
def registrar_usuario (body:dtos.Register):
    users = controllers.register_user(body)
    return {"status": "sucess"}

@router.post("/login")
def user_login(credentials:dtos.UserLogin, response:Response):
    return controllers.user_login(
        email = credentials.email, 
        password = credentials.password, 
        response=response
    )