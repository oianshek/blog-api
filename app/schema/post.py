from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.schema.user import UserReadSchema


class PostBaseSchema(BaseModel):
    title: str
    content: str


class PostCreateSchema(PostBaseSchema):
    pass


class PostReadSchema(PostBaseSchema):
    id: UUID
    created_at: datetime
    updated_at: datetime
    author: UserReadSchema


class PostUpdateSchema(PostCreateSchema):
    pass
