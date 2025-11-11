# ⬇️ Одноразовый локальный тест без сервера. Проверяю, что Pandas считает всё как надо.

from pprint import pprint
from analysis import compute_basic_stats

if __name__ == "__main__":
    result = compute_basic_stats("uploads/test.csv")  # беру файл, который уже загрузили
    pprint(result)