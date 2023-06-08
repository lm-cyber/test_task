import psycopg2
import os


class DatabaseConnection:
    _instance = None

    @staticmethod
    def get_connection():
        conn = psycopg2.connect(host=os.getenv("HOST_TEST"),
                                database=os.getenv("DB_NAME_TEST"),
                                user=os.getenv("DB_USER_TEST"),
                                password=os.getenv("DB_PASSWORD_TEST"))
        return conn

    @staticmethod
    def get_instance():
        if DatabaseConnection._instance is None:
            DatabaseConnection._instance.connection =\
                DatabaseConnection.get_connection()
        return DatabaseConnection._instance

    @staticmethod
    def close_connection():
        if DatabaseConnection._instance is not None:
            DatabaseConnection._instance.close()
            DatabaseConnection._instance = None
