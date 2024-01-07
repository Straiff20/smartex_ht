import allure
import jsonschema


def check_jsonschema(response, schema):
    with allure.step("Проверить json-схему"):
        try:
            jsonschema.validate(response, schema)
            allure.attach(
                repr(response),
                name="{} response".format(response),
                attachment_type=allure.attachment_type.JSON
            )
        except Exception as e:
            assert False, e


def check_status_code(status_code, exp_code, response):
    with allure.step("Проверить статус ответа"):
        assert status_code == exp_code, f"Ожидается: {exp_code}\nПришел: {status_code}\n Полный ответ: {response}"
        allure.attach(
            repr(status_code),
            name="status_codes: {} exp_code: {}".format(status_code, exp_code),
            attachment_type=allure.attachment_type.JSON
        )


def check_error_message(response, exp_error_message):
    with (allure.step("Проверка текста ошибки")):
        assert response == exp_error_message, \
            f"Ошибка! Текст ошибки не совпадает.\n Response: {response} \n exp_error: {exp_error_message}"
        allure.attach(
            repr(response),
            name="response: {},\n exp_error: {}".format(response, exp_error_message),
            attachment_type=allure.attachment_type.JSON
        )
