from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserBaseSchema(BaseModel):
    username: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserReadSchema(UserBaseSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime
