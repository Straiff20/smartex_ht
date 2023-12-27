import pytest

from tests.conftest import parse_schemas_path


@pytest.fixture(scope='function')
def auth_schemas():
    schema = parse_schemas_path('auth')

    yield schema
