import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Создать таблицу при запуске приложения

def create_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
       userid INT PRIMARY KEY,
       name TEXT,
       privileges INT DEFAULT 0,
       language STRING DEFAULT RU,
       currencies STRING DEFAULT USD,
       fraction INT DEFAULT 100);
    """)
    conn.commit()

# Добавить данные в таблицу командой "@Обновить БД" из admin_command

def upgrade_table_user_db():
    cursor.execute("""ALTER TABLE users ADD COLUMN language STRING DEFAULT RU;""")
    cursor.execute("""ALTER TABLE users ADD COLUMN currencies STRING DEFAULT USD;""")
    cursor.execute("""ALTER TABLE users ADD COLUMN fraction INT DEFAULT 100;""")
    conn.commit()