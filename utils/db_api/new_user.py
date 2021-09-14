from utils.db_api.db_view import *
from data.config import ADMINS

connect = sqlite3.connect('database.db')
cursor = connect.cursor()

def user_check(id, name):
    privileges = 0
    if str(id) == ADMINS:
        privileges = 1
    if get_user_info(id):
        privileges = 0
    else:
        print(f'Добавлен пользователь {id}, под именем {name}')
        cursor.execute(f"""INSERT INTO users (userid, name, privileges) VALUES('{id}', '{name}', '{privileges}');""")
        connect.commit()