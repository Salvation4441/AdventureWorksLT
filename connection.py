import sqlite3

def connect_to_db(db_path='adventureworks.db'):
    try:
        conn = sqlite3.connect(db_path)
        print(f"Connected to database: {db_path}")
        return conn
    except sqlite3.Error as e:
        print(f"Failed to connect to database: {e}")
        return None

conn = connect_to_db()
 