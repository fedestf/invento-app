from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter() #Router para las entidades interiores de la api


@router.get("/products", status_code = 200)
async def products():
    return ["Producto 1","Producto 2"]