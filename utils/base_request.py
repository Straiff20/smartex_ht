import sys
import allure

from utils.constatnts import MAIN_URL
from collections import namedtuple
from requests import Request, Session
from requests.exceptions import ReadTimeout


class BaseRequest:
    """
    Базовые настройки для отправки и обработки api-запросов
    """

    class SendRequest(Request):
        def __init__(self, path, url=MAIN_URL, method='GET', **kwargs):
            self._url = url
            self._path = path
            self._full_url = self._url + self._path
            super().__init__(url=self._full_url, method=method, **kwargs)

            self.prepared_request = self.prepare()
            self.session = Session()
            self.response = None

        def perform(self, timeout=100):

            try:
                self.response = self.session.send(self.prepared_request, timeout=timeout)
            except ReadTimeout as e:
                raise e

            with allure.step(f"Отправить запрос {self.method} {self.response.request.path_url}"):

                self.response.decoded_body = ''
                if len(self.response.content) > 0:
                    try:
                        self.response.decoded_body = self.response.json()
                    except Exception:
                        self.response.decoded_body = self.response.content.decode('UTF-8')

                allure.attach(
                    repr(self.prepared_request.headers),
                    name="{} {} request headers".format(self.method, self.url),
                    attachment_type=allure.attachment_type.JSON
                )
                allure.attach(
                    repr(self.prepared_request.body),
                    name="{} {} request body".format(self.method, self.url),
                    attachment_type=allure.attachment_type.JSON
                )
                if self.params:
                    allure.attach(
                        repr(self.params),
                        name="{} {} request params".format(self.method, self.url),
                        attachment_type=allure.attachment_type.JSON
                    )

                allure.attach(
                    repr(self.response.headers),
                    name="{} {} raw response headers".format(self.method, self.url),
                    attachment_type=allure.attachment_type.JSON
                )
                if self.response.decoded_body:
                    if sys.getsizeof(self.response.decoded_body) < 159582:
                        allure.attach(
                            repr(self.response.decoded_body),
                            name="{} {} raw response text".format(self.method, self.url),
                            attachment_type=allure.attachment_type.JSON
                        )
                    else:
                        allure.attach(
                            repr('{"Ошибка": "Не смог прикрепить файл из-за размера"}'),
                            name="{} {} raw response text".format(self.method, self.url),
                            attachment_type=allure.attachment_type.JSON
                        )

                    Response = namedtuple('Response', 'status_code, body')
                    return Response(self.response.status_code, self.response.decoded_body)
