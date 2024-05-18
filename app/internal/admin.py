from fastapi import APIRouter, Depends

from ..dependencies import get_token_header

router_admin = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}}
)


@router_admin.get("")
def adm():
    return {"description": "Admin Page"}
