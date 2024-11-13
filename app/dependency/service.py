from fastapi import Depends

from app.core import Settings
from app.repository import PostRepository, UserRepository
from app.service import PostService, UserService, AuthService
from app.dependency.repository import get_post_repo
from app.dependency.repository import get_user_repo


async def get_post_service(
    post_repo: PostRepository = Depends(get_post_repo),
) -> PostService:
    return PostService(post_repo)


async def get_user_service(
    user_repo: UserRepository = Depends(get_user_repo)
):
    return UserService(repo=user_repo)


async def get_auth_service(
    user_repo: UserRepository = Depends(get_user_repo),
):
    return AuthService(
        user_repo=user_repo,
        settings=Settings()
    )
