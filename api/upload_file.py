import os

from utils.base_request import BaseRequest

PATH: str = "/api/v1/content_import/assets/upload/"


class UploadFiles(BaseRequest):

    def __init__(self, path=PATH):
        self._path = path

    def upload_file_perform(
            self,
            asset_id: int,
            file_name: str,
            content_type: str,
            file_path: str,
            auth_token: str = None,
            headers: dict = None,
            max_chunk_size_mb: int = 5
    ):
        headers = {} if headers is None else headers
        headers['Authorization'] = f'Token {auth_token if auth_token is not None else ""}'

        chunk_size = max_chunk_size_mb * 1024 * 1024
        with open(file_path, 'rb') as file:
            chunks = []
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                chunks.append(chunk)

        response = None
        for i, chunk in enumerate(chunks):
            headers['Content-Type'] = content_type

            if i == 0:
                headers['Content-Length'] = str(os.path.getsize(file_path))
                headers['Content-Disposition'] = f'attachment; filename="{file_name}"'

            response = self.SendRequest(
                path=f"{self._path}{asset_id}",
                method="POST",
                headers=headers,
                files=[('file', (file_name, chunk, content_type))],
            ).perform()

        return response
