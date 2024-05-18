from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class ClientsType(Base):
    __tablename__ = 'clients_type'
    id = Column(Integer, primary_key=True)
    description = Column(String)

    def __str__(self):
        return {
            "id": self.id,
            "description": self.description
        }
