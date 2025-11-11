# Создание таблиц в базе (один раз запускаю).

from db import Base, engine
import models

Base.metadata.create_all(bind=engine)
print("✅ Таблицы успешно созданы!")