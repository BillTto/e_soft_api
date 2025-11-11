# Простой тест — пробую создать соединение с БД.

from db import engine

try:
    conn = engine.connect()
    print("✅ Подключение к PostgreSQL успешно!")
    conn.close()
except Exception as e:
    print("❌ Ошибка подключения:", e)