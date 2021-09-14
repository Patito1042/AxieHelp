import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def create_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
       userid INT PRIMARY KEY,
       name TEXT,
       privileges INT);
    """)
    conn.commit()