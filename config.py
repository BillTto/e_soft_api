# Здесь хранятся настройки приложения, в том числе подключение к базе.

import os
from dotenv import load_dotenv

# Загружаю переменные из .env (создадим позже)
load_dotenv()

class BaseConfig:
    # URL для подключения к базе
    # Позже поменяю на реальные значения
    DATABASE_URL = os.getenv("DATABASE_URL")