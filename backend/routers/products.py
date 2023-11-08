from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix = "/products",
                   tags = ["products"],
                   responses= {404 : {"message":"No encontrado"}}) #Router para las entidades interiores de la api
                                         #Prefijo que se utiliza para no escribri product a cada rato

products_list = ["Producto 1","Producto 2"]

@router.get("/", status_code = 200)
async def products():
    return products_list

@router.get("/{id}", status_code = 200)
async def products(id : int):
    return products_list[id]