class MyTools:
    @staticmethod
    def get_creds(file_path: str) -> tuple[str, str]:
        """
        Получить логин и пароль для авторизации из текстового файла вне проекта
        :param file_path: путь до файла с кредами
        :return: username, password
        """
        with open(file_path, 'r') as file:
            lines = file.readlines()
            username = lines[0].strip()
            password = lines[1].strip()

        return username, password
