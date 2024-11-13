import datetime as dt
from dataclasses import dataclass
from datetime import timedelta
from uuid import UUID

from jose import jwt, JWTError

from app.core import Settings
from app.exception import InvalidCredentialsException, InvalidTokenException, TokenExpiredException, \
    EntityAlreadyExistsException
from app.model import User
from app.repository import UserRepository
from app.schema import LoginSchema, LoginResponseSchema, UserCreateSchema
from app.utils import verify_password, hash_password


@dataclass
class AuthService:
    user_repo: UserRepository
    settings: Settings

    async def login(self, body: LoginSchema):
        user = await self.user_repo.get_by_username(body.username)
        if not verify_password(body.password, user.password):
            raise InvalidCredentialsException
        access_token = self._generate_access_token(str(user.id))
        return LoginResponseSchema(
            user_id=user.id,
            access_token=access_token
        )

    def _generate_access_token(self, user_id: str) -> str:
        payload = {
            "user_id": user_id,
            "expire": (dt.datetime.now(tz=dt.UTC) + timedelta(days=7)).timestamp()
        }
        encoded_jwt = jwt.encode(payload, self.settings.JWT_SECRET_KEY, algorithm=self.settings.JWT_ENCODE_ALGORITHM)
        return encoded_jwt

    def get_user_id_from_token(self, token: str) -> UUID:
        try:
            payload = jwt.decode(
                token=token,
                key=self.settings.JWT_SECRET_KEY,
                algorithms=[self.settings.JWT_ENCODE_ALGORITHM]
            )
        except JWTError:
            raise InvalidTokenException
        if payload["expire"] < dt.datetime.utcnow().timestamp():
            raise TokenExpiredException
        return UUID(payload["user_id"])

    async def register(self, body: UserCreateSchema) -> User:
        user = self.user_repo.get_by_username(body.username)
        if user:
            raise EntityAlreadyExistsException(
                entity_name="User",
                entity_attr_name="username",
                entity_attr_value=body.username
            )
        user_data = dict(body)
        user_data["password"] = hash_password(body.password)
        return await self.user_repo.create(new_obj=user_data)
