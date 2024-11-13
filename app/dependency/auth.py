from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.security import HTTPBearer
from fastapi.security.http import HTTPAuthorizationCredentials
from starlette import status

from app.dependency.service import get_auth_service
from app.exception import TokenExpiredException, InvalidTokenException
from app.service import AuthService


async def get_current_user(
    auth_service: AuthService = Depends(get_auth_service),
    token: HTTPAuthorizationCredentials = Depends(HTTPBearer())
):
    try:
        user_id = auth_service.get_user_id_from_token(token.credentials)
    except TokenExpiredException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.detail
        )
    except InvalidTokenException as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.detail
        )
    return user_id
