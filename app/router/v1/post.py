from typing import Annotated, List
from uuid import UUID

from fastapi import APIRouter
from fastapi.params import Depends

from app.model import User
from app.schema import PostCreateSchema
from app.service import PostService
from app.dependency import get_post_service, paginator, get_current_user


router = APIRouter(
    prefix="/posts",
    tags=["Posts"],
    dependencies=[Depends(get_current_user)]
)


@router.get
async def get_multi(
    service: Annotated[PostService, Depends(get_post_service)],
    pagination_params: dict = Depends(paginator)
):
    return await service.get_multi(skip=pagination_params["skip"], limit=pagination_params["limit"])


@router.get("/{id}", response_model=List[None])
async def get_one(
    id: UUID,
    service: Annotated[PostService, Depends(get_post_service)],
):
    return await service.get_by_id(id=id)


@router.post
async def create(
    body: PostCreateSchema,
    service: Annotated[PostService, Depends(get_post_service)],
    current_user: User = Depends(get_current_user)
):
    return await service.create(
        body=body,
        current_user=current_user
    )

@router.get("/search")
async def search(
    query: str,
    service: Annotated[PostService, Depends(get_post_service)]
):
    return await service.search(query=query)


@router.get("/statistics/{user_id}")
async def get_statistics(
    user_id: UUID,
    service: Annotated[PostService, Depends(get_post_service)]
):
    return await service.get_average_posts_per_month(user_id=user_id)
