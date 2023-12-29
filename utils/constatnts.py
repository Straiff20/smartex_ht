from pathlib import Path

from tests.common_data.tools import Tools

username, password = Tools.get_creds(r'C:\Users\strai\smartex_creds.txt')  # заменить путь для Вашего файла с кредами
USERNAME: str = str(username)
PASSWORD: str = str(password)

ROOT_DIR = str(Path(__file__).parent.parent)
ARTIFACTS_DIR: str = r"artifacts"
MAIN_URL: str = "https://semiautoqatz.pcvr-stg-api.smartex-it.com"
