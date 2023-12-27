from pydantic.main import BaseModel


class AuthModel(BaseModel):
    username: str = ""
    password: str = ""
