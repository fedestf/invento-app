from fastapi import FastAPI

app = FastAPI() #Arrancar backend : uvicorn main:app --reload y detener : CTRL + C

@app.get("/")
async def root():
    return "hola fastapi"


@app.get("/url") #probar y documentar endpoints http://127.0.0.1:8000/docs y http://127.0.0.1:8000/redocs
async def url(tipo : str):
    if tipo == "1":
        web_url='fedujas10'
    else: 
        web_url = 'dailezcano@example.com'
    return {"web_url":web_url}