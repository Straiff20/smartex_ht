import os

from utils.constatnts import ARTIFACTS_DIR


class FileGenerator:
    def __init__(self, base_dir=ARTIFACTS_DIR):
        self.base_dir = base_dir

    def generate_file(self, file_volume: float, format_file: str) -> tuple[str, str]:

        if format_file not in ['png', 'jpeg', 'mp3', 'pdf']:
            raise ValueError(f"Invalid format: {format_file}")

        file_name = self._generate_file_name(file_volume=file_volume, format_file=format_file)
        file_path = os.path.join(f"{self.base_dir}/{file_name}.{format_file}")

        if os.path.exists(file_path):
            os.remove(file_path)

        size_bytes = file_volume * 1024 * 1024

        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

        with open(file_path, 'xb') as file:
            file.write(os.urandom(int(size_bytes)))

        return file_name, file_path

    def _generate_file_name(self, file_volume: float, format_file) -> str:

        name = ""
        if file_volume < 1.0:
            name = "small"
        elif 1.0 > file_volume < 4.99:
            name = "middle"
        elif 5.0 > file_volume < 9.99:
            name = "large"
        elif 10.0 > file_volume:
            name = "extra_large"

        return f"{name}_{format_file}"
