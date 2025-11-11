# Модель UploadedFile описывает таблицу в PostgreSQL.
#Эта модель описывает таблицу uploaded_files
#SQLAlchemy сам создаст её в базе.

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db import Base

class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    # ID файла (уникальный)
    id = Column(Integer, primary_key=True, index=True)

    # Имя файла, как было загружено
    filename = Column(String, nullable=False)

    # Где он лежит у нас локально
    path = Column(String, nullable=False)

    # Когда был загружен
    uploaded_at = Column(DateTime(timezone=True), default=func.now())