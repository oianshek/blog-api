from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends

from app.schema import LoginSchema, UserCreateSchema
from app.service import AuthService
from app.dependency import get_auth_service


router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/login")
async def login(
    body: LoginSchema,
    service: Annotated[AuthService, Depends(get_auth_service)]
):
    return await service.login(body=body)


@router.post("/register")
async def register(
    body: UserCreateSchema,
    service: Annotated[AuthService, Depends(get_auth_service)]
):
    return await service.register(body=body)
