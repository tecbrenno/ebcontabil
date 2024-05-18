from fastapi import FastAPI
from .routers import router_clients_type, router_clients

app = FastAPI()


app.include_router(router_clients_type)
app.include_router(router_clients)
