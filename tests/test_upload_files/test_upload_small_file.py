import pytest
import allure

from tests.test_upload_files import upload_files
from tests.common_data.content_data import ContentTypes
from utils.my_asserts import check_jsonschema, check_status_code
from tests.test_upload_files.errors import ErrorTexts as Errors


@pytest.mark.upload_file
@allure.epic("upload small file")
class TestUploadSmallFile:

    @pytest.mark.parametrize("case, file_name, file_path, content_type", [
        ("png", "", "", ContentTypes.image_png),
        ("jpeg", "", "", ContentTypes.image_jpeg),
        ("pdf", "", "", ContentTypes.application_pdf),
        ("mp3", "", "", ContentTypes.audio_mp3)
    ])
    def test_upload_small_file_success(
            self,
            upload_files_schemas,
            prepare_upload_data,
            case,
            file_name,
            file_path,
            content_type
    ):
        files_paths = prepare_upload_data.files_paths.get(case)
        files_names = prepare_upload_data.files_names.get(case)

        status_code, response = upload_files.upload_file_perform(
            asset_id=prepare_upload_data.pk_id,
            auth_token=prepare_upload_data.token,
            file_name=files_names,
            file_path=files_paths,
            content_type=ContentTypes.image_png
        )
        check_status_code(status_code, 200, response)
        check_jsonschema(response, upload_files_schemas.get('upload_file_success'))

    @pytest.mark.parametrize("case, file_name, file_path, content_type", [
        ("png", "", "", ContentTypes.image_png),
        ("jpeg", "", "", ContentTypes.image_jpeg),
        ("pdf", "", "", ContentTypes.application_pdf),
        ("mp3", "", "", ContentTypes.audio_mp3)
    ])
    def test_upload_without_created_asset(
            self,
            prepare_upload_data,
            case,
            file_name,
            file_path,
            content_type
    ):
        files_paths = prepare_upload_data.files_paths.get(case)
        files_names = prepare_upload_data.files_names.get(case)

        status_code, response = upload_files.upload_file_perform(
            asset_id=0,
            auth_token=prepare_upload_data.token,
            content_type=content_type,
            file_name=files_names,
            file_path=files_paths
        )

        check_status_code(status_code, 400, response)
        with allure.step("Проверка текста ошибки"):
            assert response == Errors.not_exist_asset

    @pytest.mark.skip(reason="Нет проверки заявленного контента с полученным. См. founded_bugs")
    @pytest.mark.parametrize("case, file_name, file_path, content_type", [
        ("png", "", "", ContentTypes.audio_mp3),
        ("jpeg", "", "", ContentTypes.application_pdf),
        ("pdf", "", "", ContentTypes.image_jpeg),
        ("mp3", "", "", ContentTypes.image_png)
    ])
    def test_upload_png_with_another_content_type(
            self,
            upload_files_schemas,
            prepare_upload_data,
            case,
            file_name,
            file_path,
            content_type
    ):
        files_paths = prepare_upload_data.files_paths.get(case)
        files_names = prepare_upload_data.files_names.get(case)

        status_code, response = upload_files.upload_file_perform(
            asset_id=0,
            auth_token=prepare_upload_data.token,
            content_type=content_type,
            file_name=files_names,
            file_path=files_paths
        )

        check_status_code(status_code, 400, response)
