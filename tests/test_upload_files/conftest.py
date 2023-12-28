import pytest

from api.authorization import Authorization
from api.models.authorization import AuthModel
from tests.conftest import parse_schemas_path
from tests.test_upload_files import assets
from utils.constatnts import USERNAME, PASSWORD
from dataclasses import dataclass
from tests.common_data.file_generator import FileGenerator
from tests.common_data.tools import Tools


@pytest.fixture(scope='function')
def upload_files_schemas():
    schema = parse_schemas_path('upload_files')

    yield schema


@pytest.fixture(scope="class")
def create_asset_data():
    _format_file = "png"
    _small_png_name, _small_png_path = FileGenerator().generate_file(0.2, _format_file)
    _auth = Authorization()
    _auth_body = AuthModel(username=USERNAME, password=PASSWORD).model_dump()
    _token = _auth.auth_perform(body=_auth_body)[1]['token']

    asset_model = assets.model.model_dump()
    _pk_id = assets.create_asset_perform(auth_token=_token, body=asset_model)[1]['pk']

    @dataclass
    class TestData:
        token = _token
        small_png_name = _small_png_name
        small_png_path = _small_png_path
        pk_id = _pk_id

    yield TestData

    # assets.delete_asset(auth_token=_token, pk_id=_pk_id)
    Tools.delete_file(_small_png_path)
