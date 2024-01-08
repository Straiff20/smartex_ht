from pathlib import Path

USERNAME: str = "semiautoqatz@tz.com"
PASSWORD: str = "Pa$$w0rd!"

ROOT_DIR = str(Path(__file__).parent.parent)
ARTIFACTS_DIR: str = rf"{ROOT_DIR}/tests/test_upload_files/artifacts"
MAIN_URL: str = "https://semiautoqatz.pcvr-stg-api.smartex-it.com"
