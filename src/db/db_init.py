import os
from dotenv import load_dotenv

from peewee import PostgresqlDatabase

load_dotenv()

# Настройки подключения к базе данных
db = PostgresqlDatabase(
    os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host='localhost',
    port=5432
)

# Функция для подключения
def initialize_db():
    db.connect()
    print("Подключение к базе данных успешно!")

# Функция для закрытия соединения
def close_db():
    db.close()
    print("Соединение с базой данных закрыто.")