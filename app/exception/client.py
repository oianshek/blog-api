from typing import Any


class EntityNotFoundException(Exception):
    def __init__(self, entity_name: str, entity_attr_name: str, entity_attr_value: Any):
        self.detail = f"{entity_name} entity with {entity_attr_name}: {entity_attr_value} not found."
        super().__init__(self.detail)


class InvalidCredentialsException(Exception):
    def __init__(self):
        self.detail = "Incorrect username or password."
        super().__init__(self.detail)


class InvalidTokenException(Exception):
    def __init__(self):
        self.detail = "Invalid token."
        super().__init__(self.detail)


class TokenExpiredException(Exception):
    def __init__(self):
        self.detail = "Token has expired."
        super().__init__(self.detail)


class EntityAlreadyExistsException(Exception):
    def __init__(self, entity_name: str, entity_attr_name: str, entity_attr_value: Any):
        self.detail = f"{entity_name} entity with {entity_attr_name}: {entity_attr_value} already exists."
        super().__init__(self.detail)
