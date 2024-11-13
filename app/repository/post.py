from uuid import UUID

from sqlalchemy import select, func

from app.core.database import session_handler
from app.model import Post
from app.repository.base import BaseRepository


class PostRepository(BaseRepository):
    model = Post

    async def search(self, query: str):
        if not query:
            return []
        search_query = f"%{query}%"
        stmt = select(Post).where(
            (Post.title.ilike(search_query)) | (Post.content.ilike(search_query))
        )
        async with session_handler(self.db_session) as session:
            return (await session.execute(stmt)).scalars().all()

    async def get_average_posts_per_month(self, user_id: UUID):
        query = select(
            func.count(Post.id),
            func.min(Post.created_at),
            func.max(Post.created_at)
        ).where(Post.author_id == user_id) # type: ignore

        async with session_handler(self.db_session) as session:
            total_posts, first_post_date, last_post_date = (await self.db_session.execute(query)).scalar_one_or_none()

        if total_posts == 0 or not first_post_date or not last_post_date:
            return 0.0

        months = (last_post_date.year - first_post_date.year) * 12 + (last_post_date.month - first_post_date.month) + 1

        average_posts_per_month = total_posts / months
        return average_posts_per_month
