import sqlite3


def connect_db():

    connection = sqlite3.connect("database.db")

    cursor = connection.cursor()

    # Players Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age TEXT,
            position TEXT,
            number TEXT,
            goals TEXT
        )
    """)

    # Matches Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            opponent TEXT,
            score TEXT,
            date TEXT
        )
    """)

    connection.commit()

    connection.close()
