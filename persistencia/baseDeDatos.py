import sqlite3
from sqlite3 import Connection

class BaseDeDatos:
    _instance = None

    def __new__(cls):
        # Singleton, creo
        if cls._instance is None:
            cls._instance = super(BaseDeDatos, cls).__new__(cls)
            cls._instance._connection = None
        return cls._instance

    def connect(self, db_name: str) -> Connection:
        if self._connection is None:
            self._connection = sqlite3.connect(db_name)
        return self._connection

    def close(self):
        if self._connection:
            self._connection.close()
            self._connection = None