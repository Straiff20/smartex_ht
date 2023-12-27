import allure
import pytest

from api.authorization import Authorization
from api.models.authorization import AuthModel
from utils.constatnts import USERNAME, PASSWORD
from utils.my_asserts import check_jsonschema, check_status_code
from tests.common_data.content_types import ContentTypes as CT


@pytest.mark.auth
@allure.epic('Authorization')
class TestAuthCase:

    @pytest.mark.parametrize("case, username, pwd, content_type, exp_code, exp_schema_path", [
        ("default", USERNAME, PASSWORD, CT.APPLICATION_JSON, 200, "auth_success"),
        ("empty_content", USERNAME, PASSWORD, "", 415, "unsupported_media_type"),
        ("text_content", USERNAME, PASSWORD, CT.TEXT_PLAIN, 415, "unsupported_media_type"),
        ("image_content", USERNAME, PASSWORD, CT.IMAGE_JPEG, 415, "unsupported_media_type"),
        ("gif_content", USERNAME, PASSWORD, CT.IMAGE_GIF, 415, "unsupported_media_type"),
        ("empty_pwd", USERNAME, "", CT.IMAGE_JPEG, 415, "unsupported_media_type"),
        ("wrong_pwd", USERNAME, "wrong_pass", CT.APPLICATION_JSON, 400, "wrong_creds"),
        ("unknown_user", "unknown", PASSWORD, CT.APPLICATION_JSON, 400, "wrong_creds")
    ])
    def test_auth(self, auth_schemas, case, username, pwd, content_type, exp_code, exp_schema_path):
        auth = Authorization()

        body = AuthModel(username=username, password=pwd)

        status_code, response = auth.auth_perform(body=body.model_dump(), content_type=content_type)
        check_status_code(status_code, exp_code, response)
        check_jsonschema(response, auth_schemas.get(exp_schema_path))
