import json
import math
from datetime import datetime

import pandas as pd
from mypy.build import Any
from settings import OPEN_JSON, OPEN_XLS

from src.log import log_utils
from src.views import get_currencies, get_stocks

log_1 = log_utils()


def get_greeting():
    """
    Функция приветствует пользователя
    :return: Приветствие в виде "str"
    """
    current_hour = datetime.now().hour
    log_1.info("Дата запуска get_greeting()")
    if current_hour >= 0 and current_hour <= 4:
        return "Доброй ночи!"
    elif current_hour > 4 and current_hour <= 12:
        return "Доброе утро!"
    elif current_hour > 12 and current_hour <= 16:
        return "Добрый день!"
    else:
        return "Добрый вечер!"


def transactions_xlsx_open() -> Any:
    """
    Функция считывает файлы excel
    :param path: path
    :return: dict or Any
    """
    try:
        return pd.read_excel(OPEN_XLS)
    except ValueError:
        log_1.error("Ошибка чтения operations.xls")
        return "Ошибка чтения файла excel"


def process_data(start: str) -> list[dict]:
    """
    Функция обрабатывает данные их .xls файла для выдачи
    4 цифры номера карты, и по каждой карте сумму расходов,
     и кешбека
    :param start: дата
    :return: список со словарем по каждой карте
    """
    start_date = pd.to_datetime(start)
    df = transactions_xlsx_open()
    data = []
    # Исключаем пустые строки в данных о картах
    df = df.dropna(subset=["Номер карты"])
    # Фильтруем данные с начала месяца до введенной даты
    df["Дата операции"] = pd.to_datetime(
        df["Дата операции"], format="%d.%m.%Y %H:%M:%S"
    )
    df = df[df["Дата операции"] >= start_date]
    for card_num in df["Номер карты"].unique():
        # Инициализируйте переменные для подсчета суммы платежей и кэшбэка для текущей карты:
        total_spent = 0
        cashback = 0.0
        # Фильтруйте данные по номеру карты:
        card_data = df[df["Номер карты"] == card_num]
        # Пройдитесь по каждой операции и обновите значения суммы платежей и кэшбэка:
        for index, row in card_data.iterrows():
            total_spent += row["Сумма платежа"]
            if total_spent < 0:
                cashback += math.fabs(row["Сумма платежа"] // 100)  # Расчет кэшбэка изменил на float, чтобы не ругался mypy
            cashback += row.get("Кэшбэк") if not math.isnan(row.get("Кэшбэк")) else 0
        # Добавьте информацию о текущей карте в список карт:
        data.append(
            {
                "last_digits": card_num[-4:],  # Последние 4 цифры номера карты
                "total_spent": round(abs(total_spent), 2),
                "cashback": cashback,
            }
        )
    log_1.info("Функция process_data() отработала")
    return data


def top_transactions(transactions: pd.DataFrame) -> list[dict]:
    """
    Функция выдает топ 5 платежей
    :param transactions: транзакции
    :return: топ 5 платежей
    """
    top_transactions = transactions.sort_values(by="Дата операции").nlargest(
        5, "Сумма платежа"
    )
    top = []
    for index, row in top_transactions.iterrows():
        top.append(
            {
                "date": row["Дата операции"],  # Форматирование даты в требуемом формате
                "amount": float(row["Сумма платежа"]),
                "category": row["Категория"],
                "description": row["Описание"],
            }
        )
    log_1.info("Функция top_transactions() отработала")
    return top


def open_json(path, key):
    """
    Открывает json файл
    :param path: путь к файлу
    :param key: ключ словаря в json
    :return: список валют
    """
    with open(path, "r") as fcc_file:
        log_1.info("Файл json прочитан")
        return json.load(fcc_file)[key]


def collect_response() -> dict:
    """
    Функция собирает данные
    :return: словарь с необходимыми данными
    """

    return {
        "greeting": get_greeting(),
        "cards": process_data("2018-05-21 00:00:00"),
        "top_transactions": top_transactions(transactions_xlsx_open()),
        "currency_rates": get_currencies(open_json(OPEN_JSON, "user_currencies")),
        "stock_prices": get_stocks(open_json(OPEN_JSON, "user_stocks")),
    }


result = collect_response()
print(json.dumps(result, indent=4, ensure_ascii=False))
