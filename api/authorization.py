from api.models.authorization import AuthModel
from utils.base_request import BaseRequest

PATH: str = "/api-token-auth/"


class Authorization(BaseRequest):

    def __init__(self, path=PATH):
        self._path = path
        self.models = AuthModel()

    def auth_perform(self, body: dict, content_type: str):
        response = self.SendRequest(
            path=self._path,
            method="POST",
            json=body,
            headers={'Content-Type': content_type}
        ).perform()
        return response
