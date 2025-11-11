# Подключение к базе PostgreSQL через SQLAlchemy.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import BaseConfig

# Создаю объект движка — соединение с БД
engine = create_engine(BaseConfig.DATABASE_URL)

# Фабрика сессий — так буду работать с БД
SessionLocal = sessionmaker(bind=engine)

# Базовый класс для моделей
Base = declarative_base()