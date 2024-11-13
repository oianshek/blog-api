from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import BaseModel


class User(BaseModel):

    __tablename__ = "users"

    username: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()

    posts = relationship("Post", back_populates="author")
