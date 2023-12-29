import pytest
import allure

from tests.test_upload_files import upload_files
from tests.common_data.content_data import ContentTypes, files_for_upload
from utils.my_asserts import check_jsonschema, check_status_code
from tests.test_upload_files.errors import ErrorTexts


@pytest.mark.upload_file
@allure.epic("upload small file")
class TestUploadSmallFile:

    def test_small_png(self, upload_files_schemas, prepare_asset):
        status_code, response = upload_files.upload_file_perform(
            asset_id=prepare_asset.pk_id,
            auth_token=prepare_asset.token,
            file_name=files_for_upload['small_png'].name,
            file_path=files_for_upload['small_png'].path,
            content_type=ContentTypes.image_png
        )
        check_status_code(status_code, 200, response)
        check_jsonschema(response, upload_files_schemas.get('upload_file_success'))

    def test_small_jpg(self, upload_files_schemas, prepare_asset):
        status_code, response = upload_files.upload_file_perform(
            asset_id=prepare_asset.pk_id,
            auth_token=prepare_asset.token,
            file_name=files_for_upload['small_jpg'].name,
            file_path=files_for_upload['small_jpg'].path,
            content_type=ContentTypes.image_jpeg
        )
        check_status_code(status_code, 200, response)
        check_jsonschema(response, upload_files_schemas.get('upload_file_success'))

    def test_small_pdf(self, upload_files_schemas, prepare_asset):
        status_code, response = upload_files.upload_file_perform(
            asset_id=prepare_asset.pk_id,
            auth_token=prepare_asset.token,
            file_name=files_for_upload['small_pdf'].name,
            file_path=files_for_upload['small_pdf'].path,
            content_type=ContentTypes.application_pdf
        )
        check_status_code(status_code, 200, response)
        check_jsonschema(response, upload_files_schemas.get('upload_file_success'))

    def test_upload_without_created_asset(self, prepare_asset):

        status_code, response = upload_files.upload_file_perform(
            asset_id=0,
            auth_token=prepare_asset.token,
            content_type=ContentTypes.image_png,
            file_name=files_for_upload['small_png'].name,
            file_path=files_for_upload['small_png'].path
        )

        check_status_code(status_code, 400, response)
        with allure.step("Проверка текста ошибки"):
            assert response == ErrorTexts.not_exist_asset

    @pytest.mark.skip(reason="Нет проверки заявленного контента с полученным. См. founded_bugs")
    def test_upload_files_with_another_content_type(self, upload_files_schemas, prepare_asset,):

        status_code, response = upload_files.upload_file_perform(
            asset_id=prepare_asset.pk_id,
            auth_token=prepare_asset.token,
            content_type=ContentTypes.image_gif,
            file_name=files_for_upload['small_pdf'].name,
            file_path=files_for_upload['small_pdf'].path
        )

        check_status_code(status_code, 400, response)
