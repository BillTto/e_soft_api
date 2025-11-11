# e_soft_api

Небольшое Flask-API для загрузки и анализа CSV файлов.

---

## Требования
- Python 3.11+
- Зависимости в `requirements.txt`

---

## Установка (локально)
1. Нужно создать виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Запуск
python app.py

## Примеры запросов (curl)
curl -i http://127.0.0.1:8000/api/health
curl -i -X POST http://127.0.0.1:8000/api/upload -F "file=@test.csv"
curl -i http://127.0.0.1:8000/api/files
curl -i -X POST http://127.0.0.1:8000/api/analyze -H "Content-Type: application/json" -d '{"file_name":"test.csv"}'

##Проверить, что структура папок выглядит адекватно
e_soft_api/
│── app.py
│── analysis.py
│── routes/
│     └── api_http.md  (или api.http)
│── uploads/
│── requirements.txt
│── README.md
