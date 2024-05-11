from pydantic import BaseModel
import app


class ClientsType(BaseModel):
    description: str


@app.post("/clients/type")
def create_type(new_type: ClientsType):
    return {"type_client": new_type.description}


@app.get("/clients/type")
def get_all_type():
    # TO DO GET FROM DATABASE
    return {"type_client": ['PF', 'PJ']}


@app.get("/clients/type/{client_type}")
def get_type(search_type: str):
    # TO DO GET FROM DATABASE
    return {"type_client": search_type}


@app.put("/clients/type/{client_type}")
def update_type(client_type: str):
    # TO DO GET FROM DATABASE
    return {"type_client": client_type}


@app.delete("/clients/type/{client_type}")
def read_item(client_type: str):
    # TO DO GET FROM DATABASE
    return {"type_client": client_type}
