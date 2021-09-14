from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = 469415168  # Тут у нас будет список из админов
IP = str("https://axiehelp.herokuapp.com")  # Тоже str, но для айпи адреса хоста

