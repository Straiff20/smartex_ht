from dataclasses import dataclass

import pytest

from api.models.assets import AssetCreateModel, AssetDeleteManyModel
from tests.common_data.tools import Tools
from tests.conftest import parse_schemas_path
from tests.test_upload_files import assets


@pytest.fixture(scope='function')
def upload_files_schemas():
    schema = parse_schemas_path('upload_files')

    yield schema


@pytest.fixture(scope='function')
def prepare_asset(authorize):
    _token = authorize.token
    _asset_model = AssetCreateModel(external_id=Tools.generate_unique_uuid()).model_dump()
    _pk_id = assets.create_asset_perform(auth_token=_token, body=_asset_model)[1]['pk']

    _asset_delete_model = AssetDeleteManyModel(id__in=[_pk_id]).model_dump()

    @dataclass
    class TestData:
        pk_id = _pk_id
        token = _token

    yield TestData
    assets.delete_asset_many_perform(auth_token=_token, body=_asset_delete_model)
