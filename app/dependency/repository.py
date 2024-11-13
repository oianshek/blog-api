from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.repository import PostRepository, UserRepository
from app.core.database import get_db_session


async def get_post_repo(
    session: AsyncSession = Depends(get_db_session)
) -> PostRepository:
    return PostRepository(session)


async def get_user_repo(
    session: AsyncSession = Depends(get_db_session)
) -> UserRepository:
    return UserRepository(session)
