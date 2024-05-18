from sqlalchemy import exc
from sqlalchemy.orm import sessionmaker
from app.models.clients_type import ClientsType
from app.models.connection import engine


class ClientsTypesController:
    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def insert(self, description: str):
        try:
            new_client_type = ClientsType(description=description)
            self.session.add(new_client_type)
            self.session.commit()

            return new_client_type.__str__()
        except exc.SQLAlchemyError as e:
            print("An SQLAlchemy error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.session.close()

    def find_one(self, id_type: int):
        try:
            client_type = self.session.query(ClientsType).filter_by(id_type=id_type).first()
            return client_type
        except exc.SQLAlchemyError as e:
            print("An SQLAlchemy error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.session.close()

    def find_all(self):
        try:
            all_clients_types = self.session.query(ClientsType).all()
            return all_clients_types
        except exc.SQLAlchemyError as e:
            print("An SQLAlchemy error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.session.close()

    def update_client_type(self, id_type: int, description: str):
        found = self.find_one(id_type=id_type)
        if not found:
            return {'message': f'Client type {id_type} does not exists'}
        try:
            found.description = description
            self.session.commit()

            return found.__str__()
        except exc.SQLAlchemyError as e:
            print("An SQLAlchemy error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.session.close()

    def delete_client_type(self, id_type: int):
        found = self.find_one(id_type=id_type)
        if not found:
            return {'message': f'Client type {id_type} does not exists'}
        try:
            self.session.delete(found)
            self.session.commit()

            return found.__str__()
        except exc.SQLAlchemyError as e:
            print("An SQLAlchemy error occurred:", e)
        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.session.close()

