from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["users"]) #Arrancar backend : uvicorn main:app --reload y detener : CTRL + C

#Entidad usuario
class User(BaseModel):
    id : int
    name : str
    surname : str
    age : int

users_list = [User(id = 1, name = "Fede", surname = "Lopez", age = 20), #Instancio los usuarios en una lista
              User(id = 2, name = "Raul", surname = "Lopetegui", age = 21),
              User(id = 3, name = "Dai", surname = "Lezcano", age = 22)]

@router.get("/users", status_code = 200)
async def users():
    return users_list

#Busqueda por Path
@router.get("/users/{id}",status_code = 200)
async def user_path(id : int):
    return search_user(id)


#Retornar informacion por query
@router.get("/userquery/",status_code = 200)
async def user_query(id : int):
    return search_user(id)


@router.post("/new-user",response_model= User, status_code = 201)
async def new_user(user : User):
    
    if type(search_user(user.id)) == User:
       raise HTTPException(status_code = 204, detail = "El usuario ya existe")

    
    users_list.append(user)
    return user

@router.put("/modify-user",status_code = 200) # para todo el registro se usa PUT y para alguna parte del dato #PATCH
async def modify_user(user : User):
    
    found = False
    if type(search_user(user.id)) == User:
        for index,saved_user in enumerate(users_list):
            if saved_user.id == user.id :
                users_list[index] = user
                found = True
    
    if found == False:
        raise HTTPException(status_code = 204, detail = "El usuario no se ha encontrado")        
    
    return user

@router.delete("/delete-user/{id}", status_code = 200)
async def delete_user(id : int):
    deleted = False  
    for index,saved_user in enumerate(users_list):
            if saved_user.id == id :
                del users_list[index]
                deleted = True
    
    if deleted == False:
        raise HTTPException(status_code = 204, detail = "El usuario no se ha encontrado")


def search_user(id : int):
    try :
       users = filter(lambda user: user.id == id, users_list)
       return list(users)[0] 
    except : 
        return {"Error":f"El usuario con id {id} no se encuentra en la lista"}
    
