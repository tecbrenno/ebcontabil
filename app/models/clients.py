from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.common.utils import cnpj_format, cpf_format, ClientsEnum, ClientsTypePK
from app.controller import ClientsTypesController

Base = declarative_base()


class Clients(BaseModel):
    cpf_cnpj: str | None = None
    name: str
    fk_type_client: int



class ClientsModel(Base):
    __tablename__ = 'clients'
    cpf_cnpj = Column(String, primary_key=True)
    name = Column(String)
    fk_type_client = Column(Integer)

    def __str__(self):
        data = self.format_return()
        data.update({
            "name": self.name
        })
        return data

    def __repr__(self):
        return self.__str__()

    def format_return(self):
        client_type = self.verify_client_type()
        key_data_client = ClientsTypePK.CNPJ if client_type == ClientsEnum.PJ else ClientsTypePK.CPF
        return {
            key_data_client: cnpj_format(self.cpf_cnpj) if client_type == ClientsEnum.PJ else cpf_format(self.cpf_cnpj),
            "client_type": client_type
        }

    def verify_client_type(self):
        client_type = ClientsTypesController()
        client_type_found = client_type.find_one(self.fk_type_client)

        return client_type_found.description
