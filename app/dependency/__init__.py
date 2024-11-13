from app.dependency.service import (get_post_service,
                                    get_auth_service,
                                    get_user_service)

from app.dependency.auth import get_current_user


def paginator(
        skip: int = 0,
        limit: int = 100
):
    return {
        "skip": skip,
        "limit": limit,
    }
