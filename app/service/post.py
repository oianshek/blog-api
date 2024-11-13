from dataclasses import dataclass
from typing import List
from uuid import UUID

from app.repository import PostRepository
from app.model import Post, User
from app.exception import EntityNotFoundException
from app.schema import PostCreateSchema, PostUpdateSchema


@dataclass
class PostService:
    repo: PostRepository

    async def create(self, body: PostCreateSchema, current_user: User) -> UUID:
        body = dict(body)
        body["author_id"] = current_user.id
        created_obj = await self.repo.create(new_obj=dict(body))
        return created_obj.id

    async def delete(self, id: UUID) -> bool:
        post = await self.repo.get_one(entity_id=id)
        if not post:
            raise EntityNotFoundException(entity_name="Post", entity_attr_name="id", entity_attr_value=id)
        return await self.repo.delete(entity_id=id)

    async def get_multi(self, skip: int, limit: int) -> List[Post]:
        return await self.repo.get_multi(skip=skip, limit=limit)

    async def get_by_id(self, id: UUID) -> Post:
        task = await self.repo.get_one(entity_id=id)
        if not task:
            raise EntityNotFoundException(entity_name="Post", entity_attr_name="id", entity_attr_value=id)
        return task

    async def update(self, id: UUID, body: PostUpdateSchema) -> Post:
        return await self.repo.update(
            entity_id=id,
            update_data=dict(body),
        )

    async def search(self, query: str) -> List[Post]:
        return await self.repo.search(query=query)

    async def get_average_posts_per_month(self, user_id: UUID):
        return await self.repo.get_average_posts_per_month(user_id=user_id)
