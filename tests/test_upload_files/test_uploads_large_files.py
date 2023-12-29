import allure
import pytest

from tests.common_data.content_data import ContentTypes, files_for_upload
from tests.test_upload_files import upload_files
from utils.my_asserts import check_jsonschema, check_status_code


@pytest.mark.upload_file
@allure.epic("upload large file")
class TestUploadLargeFiles:

    def test_upload_large_png_by_chunks(self, upload_files_schemas, prepare_asset):
        status_code, response = upload_files.upload_file_perform(
            asset_id=prepare_asset.pk_id,
            auth_token=prepare_asset.token,
            file_name=files_for_upload['large_png'].name,
            file_path=files_for_upload['large_png'].path,
            content_type=ContentTypes.image_png
        )
        check_status_code(status_code, 200, response)
        check_jsonschema(response, upload_files_schemas.get('upload_file_success'))

    def test_upload_extra_large_png_by_chunks(self, upload_files_schemas, prepare_asset):
        status_code, response = upload_files.upload_file_perform(
            asset_id=prepare_asset.pk_id,
            auth_token=prepare_asset.token,
            file_name=files_for_upload['extra_large_png'].name,
            file_path=files_for_upload['extra_large_png'].path,
            content_type=ContentTypes.image_png
        )
        check_status_code(status_code, 200, response)
        check_jsonschema(response, upload_files_schemas.get('upload_file_success'))
