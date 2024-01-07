import pytest
import allure

from tests.test_upload_files import upload_files
from tests.common_data.content_data import ContentTypes, files_for_upload
from utils.my_asserts import check_jsonschema, check_status_code, check_error_message
from tests.test_upload_files.errors import ErrorTexts


@pytest.mark.upload_file
@allure.epic("upload small file")
class TestUploadSmallFile:

    @pytest.mark.parametrize("case, file_name, content_type", [
        ("small_png", "small_png", ContentTypes.image_png),
        ("small_jpg", "small_jpg", ContentTypes.image_jpeg),
        ("small_pdf", "small_pdf", ContentTypes.application_pdf),
        ("small_mp3", "small_mp3", ContentTypes.audio_mp3),
        ("middle_png", "middle_png", ContentTypes.image_png),
        ("middle_jpg", "middle_jpg", ContentTypes.image_jpeg),
        ("middle_mp3", "middle_mp3", ContentTypes.audio_mp3),
        ("large_png", "large_png", ContentTypes.image_png),
        ("large_jpg", "large_jpg", ContentTypes.image_jpeg),
        ("large_mp3", "large_mp3", ContentTypes.audio_mp3),
        ("extra_large_png", "extra_large_png", ContentTypes.image_png),
        ("extra_large_jpg", "extra_large_jpg", ContentTypes.image_jpeg),
        ("extra_large_mp3", "extra_large_mp3", ContentTypes.audio_mp3)
    ])
    def test_upload_files(self, upload_files_schemas, prepare_asset, case, file_name, content_type):
        status_code, response = upload_files.upload_file_perform(
            asset_id=prepare_asset.pk_id,
            auth_token=prepare_asset.token,
            file_name=files_for_upload[file_name].name,
            file_path=files_for_upload[file_name].path,
            content_type=content_type
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
        check_error_message(response, ErrorTexts.not_exist_asset)

    @pytest.mark.skip(reason="Нет проверки заявленного контента с полученным. См. founded_bugs")
    def test_upload_files_with_another_content_type(self, upload_files_schemas, prepare_asset, ):
        status_code, response = upload_files.upload_file_perform(
            asset_id=prepare_asset.pk_id,
            auth_token=prepare_asset.token,
            content_type=ContentTypes.image_gif,
            file_name=files_for_upload['small_pdf'].name,
            file_path=files_for_upload['small_pdf'].path
        )

        check_status_code(status_code, 400, response)
