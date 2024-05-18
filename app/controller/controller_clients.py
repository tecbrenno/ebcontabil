from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker
from app.models.clients import ClientsModel, Clients
from app.models.connection import engine


class ClientsController:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def insert(self, new_client: Clients):
        try:
            client = Clients(cpf_cnpj=new_client.cpf_cnpj, name=new_client.name, fk_type_client=new_client.fk_type_client)
            self.session.add(client)
            self.session.commit()

            return client
        except exc.SQLAlchemyError as e:
            print("An SQLAlchemy error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.session.close()

    def find_one(self, cpf_cnpj: str):
        try:
            client = self.session.query(Clients).filter_by(cpf_cnpj=cpf_cnpj).first()
            return client
        except exc.SQLAlchemyError as e:
            print("An SQLAlchemy error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.session.close()

    def find_all(self):
        try:
            all_clients_types = self.session.query(ClientsModel).all()
            return all_clients_types
        except exc.SQLAlchemyError as e:
            print("An SQLAlchemy error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.session.close()

    def update_client(self, client: Clients):
        found = self.find_one(cpf_cnpj=client.cpf_cnpj)
        if not found:
            return {'message': f'Client type {client.cpf_cnpj} does not exists'}
        try:
            found.name = client.name
            found.fk_type_client = client.fk_type_client
            self.session.commit()

            return found
        except exc.SQLAlchemyError as e:
            print("An SQLAlchemy error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.session.close()

    def delete_client(self, cpf_cnpj: str):
        found = self.find_one(cpf_cnpj=cpf_cnpj)
        if not found:
            return {'message': f'Client type {cpf_cnpj} does not exists'}
        try:
            self.session.delete(found)
            self.session.commit()

            return found
        except exc.SQLAlchemyError as e:
            print("An SQLAlchemy error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.session.close()

