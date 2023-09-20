import sqlite3


class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
        self._connection = sqlite3.connect(db_name)

