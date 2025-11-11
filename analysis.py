# analysis.py
# Универсальные функции для базового анализа CSV.

from __future__ import annotations
from typing import Dict, Any, List
import pandas as pd


def _read_csv_safely(path: str) -> pd.DataFrame:
    """
    Надёжное чтение CSV с явным разделителем и обработкой «склеенного» заголовка.
    """
    df = pd.read_csv(
        path,
        sep=",",              # явно указываем запятую
        quotechar='"',        # кавычки как в стандартном CSV
        skipinitialspace=True # игнор пробелов после запятой
    )
    # подчистим заголовки от случайных пробелов
    df.columns = [c.strip() for c in df.columns]

    # Если по какой-то причине весь файл прочитался одной колонкой с заголовком вида "col1,col2,..."
    if df.shape[1] == 1 and "," in df.columns[0]:
        header = [c.strip() for c in df.columns[0].split(",")]
        df = df.iloc[:, 0].astype(str).str.split(",", expand=True)
        df.columns = header

    return df


def _coerce_numeric(df: pd.DataFrame) -> List[str]:
    """
    Пытаемся привести столбцы к числовому типу. Возвращаем список реально числовых колонок.
    """
    numeric_cols: List[str] = []
    for col in df.columns:
        converted = pd.to_numeric(df[col], errors="coerce")
        # если получилось извлечь хотя бы какие-то числовые значения — сохраняем преобразование
        if converted.notna().any():
            df[col] = converted
        if pd.api.types.is_numeric_dtype(df[col]):
            numeric_cols.append(col)
    return numeric_cols


def compute_basic_stats(path: str) -> Dict[str, Any]:
    """
    Считает базовую статистику по CSV:
    - список колонок
    - count по всем колонкам
    - mean/median по числовым
    - список числовых колонок
    - форму датасета (rows, columns)
    """
    df = _read_csv_safely(path)
    numeric_cols = _coerce_numeric(df)

    result: Dict[str, Any] = {
        "columns": df.columns.tolist(),
        "count": df.count().to_dict(),
        "mean": df[numeric_cols].mean(numeric_only=True).to_dict() if numeric_cols else {},
        "median": df[numeric_cols].median(numeric_only=True).to_dict() if numeric_cols else {},
        "numeric_columns": numeric_cols,
        "shape": {"columns": df.shape[1], "rows": df.shape[0]},
    }
    return result