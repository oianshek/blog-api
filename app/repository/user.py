from app.core.database import session_handler
from app.model import User
from app.repository.base import BaseRepository

from sqlalchemy import exists, select


class UserRepository(BaseRepository):
    model = User

    async def get_by_username(self, username: str) -> User | None:
        query = select(self.model).where(self.model.username == username)  # type: ignore
        async with session_handler(self.db_session) as session:
            return (await session.execute(query)).scalar_one_or_none()
