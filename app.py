# Точка входа в приложение. Регистрирую blueprint + запускаю сервер.
# Позже добавлю остальные endpoints.

from flask import Flask
from routes import bp as api_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix="/api")
    return app


if __name__ == "__main__":
    app = create_app()
    # Запускаю сервер на localhost:8000
    app.run(host="0.0.0.0", port=8000, debug=True)