import pytest
import allure

from tests.test_upload_files import upload_files
from tests.common_data.content_types import ContentTypes
from utils.my_asserts import check_jsonschema, check_status_code
from tests.test_upload_files.errors import ErrorTexts as Errors


@pytest.mark.upload_file
@allure.epic("upload small file")
class TestUploadSmallFile:

    def test_upload_small_png_success(self, upload_files_schemas, create_asset_data):
        status_code, response = upload_files.upload_file_perform(
            asset_id=create_asset_data.pk_id,
            auth_token=create_asset_data.token,
            content_type=ContentTypes.image_png,
            file_name=create_asset_data.small_png_name,
            file_path=create_asset_data.small_png_path
        )
        check_status_code(status_code, 200, response)
        check_jsonschema(response, upload_files_schemas.get('upload_file_success'))

    def test_upload_without_created_asset(self, create_asset_data):
        status_code, response = upload_files.upload_file_perform(
            asset_id=0,
            auth_token=create_asset_data.token,
            content_type=ContentTypes.image_jpeg,
            file_name=create_asset_data.small_png_name,
            file_path=create_asset_data.small_png_path
        )
        check_status_code(status_code, 400, response)
        with allure.step("Проверка текста ошибки"):
            assert response == Errors.not_exist_asset
