import allure
import pytest

from api.models.authorization import AuthModel
from utils.constatnts import USERNAME, PASSWORD
from utils.my_asserts import check_jsonschema, check_status_code
from tests.common_data.content_types import ContentTypes as CT
from tests.test_auth import auth


@pytest.mark.authorization
@allure.epic('Authorization')
class TestAuthCase:

    @allure.story("Auth by credentials")
    @pytest.mark.parametrize("case, username, pwd, content_type, exp_code, exp_schema_path", [
        ("default", USERNAME, PASSWORD, CT.application_json, 200, "auth_success"),
        ("empty_content", USERNAME, PASSWORD, "", 415, "unsupported_media_type"),
        ("text_content", USERNAME, PASSWORD, CT.text_plain, 415, "unsupported_media_type"),
        ("image_content", USERNAME, PASSWORD, CT.image_jpeg, 415, "unsupported_media_type"),
        ("gif_content", USERNAME, PASSWORD, CT.image_gif, 415, "unsupported_media_type"),
        ("empty_pwd", USERNAME, "", CT.image_jpeg, 415, "unsupported_media_type"),
        ("wrong_pwd", USERNAME, "wrong_pass", CT.application_json, 400, "wrong_creds"),
        ("unknown_user", "unknown", PASSWORD, CT.application_json, 400, "wrong_creds")
    ])
    def test_auth(self, auth_schemas, case, username, pwd, content_type, exp_code, exp_schema_path):
        body = AuthModel(username=username, password=pwd).model_dump()

        status_code, response = auth.auth_perform(body=body, content_type=content_type)
        check_status_code(status_code, exp_code, response)

        pattern = f"Unsupported media type \"{content_type}\" in request\."
        exp_schema = auth_schemas.get(exp_schema_path)
        if exp_schema_path == "unsupported_media_type":
            exp_schema["definitions"]["UnsupportedMediaType"]["properties"]["detail"]["pattern"] = pattern
        check_jsonschema(response, exp_schema)
