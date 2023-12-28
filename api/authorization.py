from utils.base_request import BaseRequest
from tests.common_data.content_types import ContentTypes

PATH: str = "/api-token-auth/"


class Authorization(BaseRequest):

    def __init__(self, path=PATH):
        self._path = path

    def auth_perform(self, body: dict, content_type: str = ContentTypes.application_json):
        return self.SendRequest(
            path=self._path,
            method="POST",
            json=body,
            headers={'Content-Type': content_type}
        ).perform()
