from utils.base_request import BaseRequest

ASSETS_IMPORT_PATH: str = "/api/v1/content_import/assets"
ASSETS_DELETE_MANY_PATH: str = "/api/v1/content/assets/delete_many/"


class CreateAssets(BaseRequest):
    def __init__(self, path=ASSETS_IMPORT_PATH):
        self._path = path
        self.delete_path = ASSETS_DELETE_MANY_PATH

    def create_asset_perform(self, auth_token: str, body: dict):
        return self.SendRequest(
            path=f"{self._path}/create",
            method="POST",
            json=body,
            headers={"Authorization": f"Token {auth_token}"}
        ).perform()

    def delete_asset_many_perform(self, auth_token: str, body: dict):
        return self.SendRequest(
            path=self.delete_path,
            method="POST",
            json=body,
            headers={"Authorization": f"Token {auth_token}"}
        ).perform()
