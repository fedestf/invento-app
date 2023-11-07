from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() #Arrancar backend : uvicorn main:app --reload y detener : CTRL + C

#Entidad usuario
class User(BaseModel):
    id : int
    name : str
    surname : str
    age : int

users_list = [User(id = 1, name = "Fede", surname = "Lopez", age = 20), #Instancio los usuarios en una lista
              User(id = 2, name = "Raul", surname = "Lopetegui", age = 21),
              User(id = 3, name = "Dai", surname = "Lezcano", age = 22)]

@app.get("/users")
async def users():
    return users_list

#Busqueda por Path
@app.get("/users/{id}")
async def user_path(id : int):
    return search_user(id)


#Retornar informacion por query
@app.get("/userquery/")
async def user_query(id : int):
    return search_user(id)

def search_user(id : int):
    try :
       users = filter(lambda user: user.id == id, users_list)
       return list(users)[0] 
    except : 
        return {"Error":f"El usuario con id {id} no se encuentra en la lista"}