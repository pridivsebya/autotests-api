from pydantic import BaseModel, EmailStr, Field, ConfigDict
from pydantic.alias_generators import to_camel


class UserSchema(BaseModel):
    """
    Схема, представляющая пользователя с основной информацией, включая ID и детали имени.
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class CreateUserRequestSchema(BaseModel):
    """
    Схема для запроса создания нового пользователя с email, паролем и деталями имени.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)


class CreateUserResponseSchema(BaseModel):
    """
    Схема для ответа при создании пользователя, содержащая данные созданного пользователя.
    """
    user: UserSchema

    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
