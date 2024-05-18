from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.controller import ClientsTypesController

from ..dependencies import get_token_header

router_clients_type = APIRouter(
    prefix="/clients/type",
    tags=["clients Type"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}}
)


class ClientsType(BaseModel):
    id_type: int | None = None
    description: str


@router_clients_type.post("")
async def create_type(new_type: ClientsType):
    new_clients_type = ClientsTypesController()
    return new_clients_type.insert(description=new_type.description)


@router_clients_type.get("")
async def get_all_type():
    clients_type = ClientsTypesController()
    return clients_type.find_all()


@router_clients_type.get("/{id_type}")
async def get_type(id_type: int):
    clients_type = ClientsTypesController()
    return clients_type.find_one(id_type=id_type)


@router_clients_type.put("/{id_type}")
async def update_type(id_type: int, description: str):
    clients_type = ClientsTypesController()
    return clients_type.update_client_type(id_type=id_type, description=description)


@router_clients_type.delete("/{id_type}")
async def delete_type(id_type: int):
    clients_type = ClientsTypesController()
    return clients_type.delete_client_type(id_type=id_type)

