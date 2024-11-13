from uuid import UUID
from typing import Any, List, TypeVar, Union, Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete, insert

from app.core.database import Base, session_handler

ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository:

    model: Any = ModelType

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create(self, new_obj: dict) -> model:
        """
        :param new_obj:
        :return: created_entity of created entity
        """
        query = insert(self.model).returning(self.model)
        async with session_handler(self.db_session) as session:
            created_entity = (await session.execute(query, new_obj)).scalar()
            await session.flush()
            return created_entity

    async def get_one(self, entity_id: UUID) -> Union[model, None]:
        """
        :param entity_id:
        :return: entity with provided id
        """
        query = select(self.model).where(self.model.id == entity_id)
        async with session_handler(self.db_session) as session:
            return (await session.execute(query)).scalar_one_or_none()

    async def get_multi(self, skip: int = 0, limit: int = 100) -> List[model]:
        """
        :param skip: Number of records to skip (for pagination)
        :param limit: Maximum number of records to return
        :return: List of models from the table
        """
        query = select(self.model).offset(skip).limit(limit)
        async with session_handler(self.db_session) as session:
            result = await session.execute(query)
            return result.scalars().all()  # type: ignore

    async def update(self, entity_id: UUID, update_data: Dict[str, Any]) -> Union[model, None]:
        """
        :param entity_id: UUID of the entity to update.
        :param update_data: Dictionary with fields to update.
        :return: The updated entity if found and updated, otherwise None.
        """
        query = (
            update(self.model)
            .where(self.model.id == entity_id)
            .values(update_data)
            .returning(self.model)
        )
        async with session_handler(self.db_session) as session:
            result = await session.execute(query)
            await session.flush()
            return result.scalar_one_or_none()

    async def delete(self, entity_id: UUID) -> bool:
        """
        :param entity_id: UUID of the entity to delete.
        :return: True if the entity was deleted, otherwise False.
        """
        query = delete(self.model).where(self.model.id == entity_id)
        async with session_handler(self.db_session) as session:
            result = await session.execute(query)
            await session.flush()
            return result.rowcount > 0
