import glob
import json
import sys
import pytest

from dataclasses import dataclass

from api.authorization import Authorization
from api.models.authorization import AuthModel
from utils.constatnts import PASSWORD, ROOT_DIR, USERNAME

schemas_path = f'{ROOT_DIR}/api/schemas/'


def parse_schemas_path(folder: str):
    """
    Обрабатываем путь до файла с json-схемой
    """
    paths = glob.glob(schemas_path + folder + "/*.json")
    names = [i.split('\\' if sys.platform == 'win32' else '/')[-1].split('.json')[0] for i in paths]
    schemas = {k: json.load(open(v, encoding='utf-8')) for k, v in zip(names, paths)}
    return schemas


@pytest.fixture(scope='session')
def authorize():
    _auth = Authorization()
    _auth_body = AuthModel(username=USERNAME, password=PASSWORD).model_dump()
    _token = _auth.auth_perform(body=_auth_body)[1]['token']

    @dataclass
    class TestData:
        token = _token

    yield TestData
