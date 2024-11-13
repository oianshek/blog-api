from uuid import UUID

from sqlalchemy import Text, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import BaseModel


class Post(BaseModel):

    __tablename__ = "posts"

    title: Mapped[str] = mapped_column()
    content: Mapped[str] = mapped_column(Text)
    author_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)

    author = relationship("User", back_populates="posts")

    __table_args__ = (
        Index("ix_post_title", title, postgresql_using="gin"),
        Index("ix_post_content", content, postgresql_using="gin"),
    )
