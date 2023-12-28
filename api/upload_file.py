from utils.base_request import BaseRequest

PATH: str = "/api/v1/content_import/assets/upload/"


class UploadFiles(BaseRequest):

    def __init__(self, path=PATH):
        self._path = path

    def upload_file_perform(
            self,
            asset_id: int,
            auth_token: str,
            file_name: str,
            content_type: str,
            file_path: str,
            content_range: str = "100-200/1000",
    ):
        """
        Загрузка изображения в раннее созданный asset
        :param asset_id: id созданного asset'а
        :param auth_token: токен пользователя
        :param content_range: сколькими частями отправлять файл, например "100-200/1000"
        :param file_name: наименования файла для отправки
        :param content_type: тип загружаемого файла (см. ContentTypes)
        :param file_path: путь, где лежат файлы для отправки
        :return: json-schema 'upload_file_success'
        """
        return self.SendRequest(
            path=f"{self._path}{asset_id}",
            method="POST",
            headers={'Authorization': f'Token {auth_token}', 'HTTP_CONTENT_RANGE': content_range},
            files=[('file', (file_name, open(file_path, 'rb'), content_type))]
        ).perform()
