from pathlib import Path

from utils.my_tools import MyTools

username, password = MyTools.get_creds(r'C:\Users\strai\smartex_creds.txt')  # заменить путь для Вашего файла с кредами
USERNAME: str = str(username)
PASSWORD: str = str(password)

ROOT_DIR = str(Path(__file__).parent.parent)
MAIN_URL: str = "https://semiautoqatz.pcvr-stg-api.smartex-it.com"
