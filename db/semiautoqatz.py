import sqlite3

from db.sql import semiautoqatz


class SemiautoqatzDB:
    """
    Подключение к db и выполнение запросов
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SemiautoqatzDB, cls).__new__(cls)
            cls._instance.connection = sqlite3.connect('semiautoqatz.db')
        return cls._instance

    def execute_select_query(self, query_script: str):
        """
        Выполнение select-запроса к db
        :param query_script: запрос к db
        :return: полученные данные
        """
        cursor = self.connection.cursor()
        cursor.execute(query_script)
        rows = cursor.fetchall()
        return rows

# Пример использования
# db_connect = DatabaseConnect()
# query = semiautoqatz.select_semiautoqatz
# result = db_connect.execute_select_query(query)
