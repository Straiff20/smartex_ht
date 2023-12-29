from utils.base_request import BaseRequest

ASSET_FIND_PATH: str = "/api/v1/mutual_integration/find_assets/search/"
ASSETS_IMPORT_PATH: str = "/api/v1/content_import/assets"
ASSETS_DELETE_MANY_PATH: str = "/api/v1/content/assets/delete_many/"


class AssetsRequests(BaseRequest):
    def __init__(self, path=ASSETS_IMPORT_PATH):
        self._asset_create = path
        self._asset_find = ASSET_FIND_PATH
        self._asset_delete = ASSETS_DELETE_MANY_PATH

    def find_asset_perform(self, token: str):
        return self.SendRequest(
            path=self._asset_find,
            headers={"Authorization": f"Token {token}"}
        ).perform()

    def create_asset_perform(self, auth_token: str, body: dict):
        return self.SendRequest(
            path=f"{self._asset_create}/create",
            method="POST",
            json=body,
            headers={"Authorization": f"Token {auth_token}"}
        ).perform()

    def delete_asset_many_perform(self, auth_token: str, body: dict):
        return self.SendRequest(
            path=self._asset_delete,
            method="POST",
            json=body,
            headers={"Authorization": f"Token {auth_token}"}
        ).perform()
