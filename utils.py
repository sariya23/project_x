import sqlite3


def get_db_connection(file_name: str):
    """
    Открывает соединение с файлом базы данных,
    а затем устанавливает атрибут row_factory в sqlite3.
    Row, чтобы получить доступ к столбцам на основе имен.
    Это означает, что подключение к базе данных будет возвращать строки,
    которые ведут себя как обычные словари Python.
    :return: Объект подключения conn, который вы будете использовать для доступа к базе данных.
    """
    connect = sqlite3.connect(file_name)
    connect.row_factory = sqlite3.Row
    return connect
