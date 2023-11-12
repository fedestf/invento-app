from fastapi import FastAPI, Depends , HTTPException , status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

app = FastAPI()

oauth2= OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username : str
    full_name : str
    email: str
    disable : bool

class UserDB(User):
    password : str
    
users_bd = {
    "Federico":{"username":"Federico",
               "full_name":"Federico Lopez",
               "email":"fede@example.com",
               "disable":True,
               "password":"123456"},
    
    "Federico2":{"username":"Federico2",
               "full_name":"Federico Lopez2",
               "email":"fede@example.com2",
               "disable":False,
               "password":"154232"}
}
    

def search_user (username : str):
    if username in users_bd:
        return UserDB(**users_bd[username])
    
async def current_user(token : str = Depends(oauth2)):
    
    user = search_user(token)
    if not user :
        raise HTTPException (status_code = status.HTTP_401_UNAUTHORIZED,
                             detail = "Credenciales invalidas",
                             headers={"WWWW-Authenticate":"bearer"})
    
    return user
    

@app.post("/login")
async def login(form : OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException (status_code= 400 ,detail= "Usuario no es correcto")
    
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException (status_code= 400 ,detail= "Contraseña incorrecta")
    
    return {"access_token" : user.username , "token_type": "bearer"}

@app.get("/users/me")
async def me(user : User = Depends(current_user)):
    
    return user     
