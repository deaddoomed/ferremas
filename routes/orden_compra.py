from fastapi import APIRouter, HTTPException, status
from sqlalchemy import or_,update
from typing import List
from database import db_dependency
from models.productos import *
from models.ventas import *

router = APIRouter(prefix="/orden_compra")

@router.post("/crear", status_code=status.HTTP_201_CREATED)
async def nueva_orden(request: nueva_orden, db: db_dependency):
    if(request):
        received = Orden_Compra(**request.model_dump())
        try:
            db.add(received)
        except:
            raise HTTPException(status_code=442, detail='Orden de Compra no pudo ser creada') 
        db.commit()       
        return "Orden creada!"
    else:
        raise HTTPException(status_code=401, detail='No se ingreso orden de compra valida')

@router.get("/",status_code=status.HTTP_200_OK)
async def lista(db: db_dependency):
    productos = db.query(Orden_Compra).all() 
    return productos
    
@router.put("/metodo_despacho",status_code=status.HTTP_200_OK)
async def metodo_despacho(request: metodo_despacho, db: db_dependency):
    statement = (update(Orden_Compra).where(Orden_Compra.orden_compr_id == request.orden_compr_id)).values(metodo_despacho = request.metodo_despacho)
    db.execute(statement)
    db.commit()
    return "Metodo de despacho actualizado"

@router.put("/direccion",status_code=status.HTTP_200_OK)
async def metodo_despacho(request: direccion_despacho, db: db_dependency):
    statement = (update(Orden_Compra).where(Orden_Compra.orden_compr_id == request.orden_compr_id)).values(direccion = request.direccion)
    db.execute(statement)
    db.commit()
    return "Direccion de despacho actualizada"