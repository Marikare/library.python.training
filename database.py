import sqlite3
conn = sqlite3.connect("./library.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    birth_date TEXT NOT NULL,
    nationality TEXT NOT NULL,
    description TEXT)""")
conn.commit()
conn.close()