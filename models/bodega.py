from database import mysql_database
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel

#------------Pedidos y despachos------------
Pedido = mysql_database.classes.pedidos
Despacho = mysql_database.classes.despachos

class despacho_filtro(BaseModel):
    despacho_id: int
    pedido_id: int
    fecha: datetime

class pedidos_filtro(BaseModel):
    pedido_id: int
    orden_compra_id: int
    sku: str
