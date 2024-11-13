from dataclasses import dataclass

from app.repository import UserRepository


@dataclass
class UserService:
    repo: UserRepository
