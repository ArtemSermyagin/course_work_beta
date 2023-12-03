# import json
# import os
import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.log import log_utils

# from settings import OPEN_JSON


log_1 = log_utils()
load_dotenv()
api_key_c = os.getenv("API_CURRENCIE")
api_key_s = os.getenv("API_STOCK")


def get_stocks(data_stocks: list) -> Any:
    """
    Конвертирует акции
    :param data_stocks:
    :return: Any
    """
    try:
        list_stocks = []
        for stock in data_stocks:
            url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={api_key_s}"
            data = requests.get(url).json()
            list_stocks.append(
                {
                    "stock": data["Global Quote"]["01. symbol"],
                    "price": data["Global Quote"]["05. price"],
                }
            )
        log_1.info("Из файла user_settings.json получен список акций")
        return list_stocks
    except Exception as e:
        log_1.error(f"Произошла ошибка: {e}")
        return [], []


def get_currencies(data_currencies: list) -> Any:
    """
    Конвертирует валюту
    :param data_currencies: список валют
    :return: Any
    """
    try:
        list_currencies = []
        for currencie in data_currencies:
            url = f"""https://www.alphavantage.co/query?function=
            CURRENCY_EXCHANGE_RATE&from_currency={currencie}&to_currency=RUB&apikey={api_key_c}"""
            data = requests.get(url).json()
            list_currencies.append(
                {
                    "currency": data["Realtime Currency Exchange Rate"][
                        "1. From_Currency Code"
                    ],
                    "rate": data["Realtime Currency Exchange Rate"]["5. Exchange Rate"],
                }
            )
        log_1.info("Из файла user_settings.json получен список валют")
        return list_currencies
    except Exception as e:
        log_1.error(f"Произошла ошибка: {e}")
        return [], []
