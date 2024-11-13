from uuid import UUID

from pydantic import BaseModel


class LoginSchema(BaseModel):
    username: str
    password: str


class LoginResponseSchema(BaseModel):
    user_id: UUID
    access_token: str
