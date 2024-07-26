from fastapi import Response
import models
import dtos

def register_user(infos:dtos.Register):
    new_user = models.User(**infos._dict_, is_employee=False)
    models.users_model.append(new_user)
    return {"status": "sucess"}

def user_login (email:str,password:str,response:Response):
    for usr in models.users_model:
        if (usr.email == email and usr.password == password):
            response.status_code = 200
            return{
                "status":"sucess", 
                "message": "Usuario loggado com sucesso!", 
                "is_employee":usr.is_employee
            }    
    response.status_code = 404
    return {
                "status":"error", 
                "message":"Usuario não encontrado"
            }