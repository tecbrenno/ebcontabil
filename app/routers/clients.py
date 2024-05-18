from fastapi import APIRouter, Depends
from app.controller import ClientsController
from ..dependencies import get_token_header
from ..models.clients import Clients

router_clients = APIRouter(
    prefix="/clients",
    tags=["Clients"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}}
)


@router_clients.post("")
async def create_client(new_client: Clients):
    client = ClientsController()
    return client.insert(new_client)


@router_clients.get("")
async def get_all_clients():
    client = ClientsController()
    return client.find_all()


@router_clients.get("/{cpf_cnpj}")
async def get_client(cpf_cnpj: str):
    client = ClientsController()
    return client.find_one(cpf_cnpj=cpf_cnpj)


@router_clients.put("")
async def update_client(client_u: Clients):
    client = ClientsController()
    return client.update_client(client=client_u)


@router_clients.delete("/{cpf_cnpj}")
async def delete(cpf_cnpj: str):
    client = ClientsController()
    return client.delete_client(cpf_cnpj=cpf_cnpj)

