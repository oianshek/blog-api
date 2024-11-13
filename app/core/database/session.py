from asyncpg import InvalidCatalogNameError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from contextlib import asynccontextmanager

from app.core import settings
from app.exception import DatabaseErrorException

engine = create_async_engine(
    url=settings.db_url,
    future=True,
    echo=True,
    pool_pre_ping=True,
)

AsyncSessionFactory = async_sessionmaker(
    engine,
    autoflush=False,
    expire_on_commit=False
)


async def get_db_session() -> AsyncSession:
    async with AsyncSessionFactory() as session:
        yield session


@asynccontextmanager
async def session_handler(db_session: AsyncSession):
    async with db_session as session:
        try:
            yield session
            await session.commit()
        except InvalidCatalogNameError as e:
            await session.rollback()
            raise DatabaseErrorException(error=str(e))
        except SQLAlchemyError as e:
            await session.rollback()
            raise DatabaseErrorException(error=str(e))
