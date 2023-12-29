import pytest
import allure

from tests.common_data.content_data import ContentTypes, files_for_upload
from tests.test_upload_files import upload_files
from utils.my_asserts import check_jsonschema, check_status_code


@pytest.mark.upload_file
@allure.epic("upload middle file")
class TestUploadMiddleFiles:

    def test_upload_middle_png(self, upload_files_schemas, prepare_asset):

        status_code, response = upload_files.upload_file_perform(
            asset_id=prepare_asset.pk_id,
            auth_token=prepare_asset.token,
            file_name=files_for_upload['middle_png'].name,
            file_path=files_for_upload['middle_png'].path,
            content_type=ContentTypes.image_png
        )
        check_status_code(status_code, 200, response)
        check_jsonschema(response, upload_files_schemas.get('upload_file_success'))

    def test_upload_middle_jpg(self, upload_files_schemas, prepare_asset):
        status_code, response = upload_files.upload_file_perform(
            asset_id=prepare_asset.pk_id,
            auth_token=prepare_asset.token,
            file_name=files_for_upload['middle_jpg'].name,
            file_path=files_for_upload['middle_jpg'].path,
            content_type=ContentTypes.image_jpeg
        )
        check_status_code(status_code, 200, response)
        check_jsonschema(response, upload_files_schemas.get('upload_file_success'))
