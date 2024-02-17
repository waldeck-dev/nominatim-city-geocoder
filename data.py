import sqlite3


class DataManager:

    def __init__(self, db_path):
        self.db_path = db_path

    def execute_query_from_file(self, sql_file_path,
                                params=tuple(), fetchall=True):
        """Executes an SQL query from a specified file"""
        rows = []
        try:
            with open(sql_file_path, 'r') as sql_file:
                query = sql_file.read()
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                if fetchall:
                    cursor.execute(query, params)
                    rows = cursor.fetchall()
                else:
                    cursor.executescript(query)
                conn.commit()
                conn.close()
                print("Query executed successfully.")
        except FileNotFoundError:
            print(f"Error: '{sql_file_path}' file not found.")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
        finally:
            return rows
