import pandas as pd
import json

from settings import OPEN_XLS
from src.log import log_utils

log_1 = log_utils()


def search_transactions(file_path, query):
    df = pd.read_excel(file_path)  # Загрузка файла Excel в DataFrame

    filtered_df = df[
        df["Описание"].str.contains(query, case=False, na=False)
    ]  # Фильтрация DataFrame по запросу в колонке "Описание"

    result = filtered_df.to_dict(
        orient="records"
    )  # Преобразование фильтрованного DataFrame в список словарей
    log_1.info("Преобразование фильтрованного DataFrame в список словарей")
    return json.dumps(
        result, indent=4, ensure_ascii=False
    )  # Преобразование списка в JSON


# Пример использования функции
file_path = OPEN_XLS  # Путь к файлу Excel
query = "Перевод"  # Строка запроса
result = search_transactions(file_path, query)
print(result)
