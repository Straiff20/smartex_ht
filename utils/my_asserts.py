import allure
import jsonschema


def check_jsonschema(response, schema):
    with allure.step("Проверить json-схему"):
        try:
            jsonschema.validate(response, schema)
        except Exception as e:
            assert False, e


def check_status_code(status_code, exp_code, response):
    with allure.step("Проверить статус ответа"):
        assert status_code == exp_code, f"Ожидается: {exp_code}\nПришел: {status_code}\n Полный ответ: {response}"
