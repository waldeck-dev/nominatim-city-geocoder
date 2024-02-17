import os
import sqlite3
from data import DataManager


def create_database(db_path):
    """
    Creates the SQLite database if it doesn't exist.
    :param db_path: Path to the database file.
    """
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        conn.close()
        print(f"Database '{db_path}' created successfully.")


if __name__ == "__main__":
    db_path = 'db.sqlite3'
    sql_file_path = 'queries/setup.sql'

    create_database(db_path)

    manager = DataManager(db_path)
    manager.execute_query_from_file(sql_file_path, fetchall=False)
