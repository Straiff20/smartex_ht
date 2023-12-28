import random

import pytest

from api.authorization import Authorization
from api.models.assets import AssetCreateModel, AssetDeleteManyModel
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
def prepare_upload_data():
    _format_png = "png"
    _format_jpeg = "jpeg"
    _format_pdf = "pdf"
    _format_mp3 = "mp3"

    _small_png_name, _small_png_path = FileGenerator().generate_file(random.uniform(0.1, 0.9), _format_png)
    _small_pdf_name, _small_pdf_path = FileGenerator().generate_file(random.uniform(0.1, 0.9), _format_pdf)
    _small_mp3_name, _small_mp3_path = FileGenerator().generate_file(random.uniform(0.1, 0.9), _format_mp3)
    _small_jpeg_name, _small_jpeg_path = FileGenerator().generate_file(random.uniform(0.1, 0.9), _format_jpeg)

    _auth = Authorization()
    _auth_body = AuthModel(username=USERNAME, password=PASSWORD).model_dump()
    _token = _auth.auth_perform(body=_auth_body)[1]['token']

    _asset_model = AssetCreateModel().model_dump()
    _pk_id = assets.create_asset_perform(auth_token=_token, body=_asset_model)[1]['pk']
    _asset_delete_model = AssetDeleteManyModel(id__in=[_pk_id]).model_dump()

    _files_paths = {
        "png": _small_png_path,
        "jpeg": _small_jpeg_path,
        "pdf": _small_pdf_path,
        "mp3": _small_mp3_path
    }

    _files_names = {
        "png": _small_pdf_name,
        "jpeg": _small_jpeg_name,
        "pdf": _small_pdf_name,
        "mp3": _small_mp3_name
    }

    @dataclass
    class TestData:
        token = _token
        small_png_name = _small_png_name
        small_png_path = _small_png_path
        files_paths = _files_paths
        files_names = _files_names
        pk_id = _pk_id

    yield TestData

    assets.delete_asset_many_perform(auth_token=_token, body=_asset_delete_model)
    Tools.delete_file(_small_png_path)
