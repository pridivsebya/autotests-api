from typing import TypedDict

from httpx import Response

from ..api_client import APIClient


class CreateUserRequest(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """
    email: str
    password: str
    first_name: str
    last_name: str
    middle_name: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с методами, не требующими авторизации для /api/v1/users.
    """

    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Метод создает пользователя.

        :param request: Словарь с данными пользователя.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)