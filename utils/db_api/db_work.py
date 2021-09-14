import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

def user_set_setting_lang(user_id):
    try:
        sql_select_query = """select * from users where userid = ?"""
        cursor.execute(sql_select_query, (user_id,))
        records = cursor.fetchall()
        return records
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
