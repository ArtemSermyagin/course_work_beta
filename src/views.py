# import os
#
import json
import os

import requests

from settings import OPEN_JSON


from dotenv import load_dotenv

load_dotenv()


def open_json_currencies(path):
    """
    Открывает json файл
    :param path: путь к файлу
    :return: список валют
    """
    with open(path, 'r') as fcc_file:
        fcc_data = json.load(fcc_file)
        return fcc_data["user_currencies"]


def open_json_stocks(path):
    """
    Открывает json файл
    :param path: путь к файлу
    :return: список акций
    """
    with open(path, 'r') as fcc_file:
        fcc_data = json.load(fcc_file)
        return fcc_data["user_stocks"]


def get_stocks(data_stocks):
    for stock in data_stocks:
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey=N64DYQB2WV5QR1WW'
        r = requests.get(url)
        data = r.json()
        print(data['Global Quote']['01. symbol'], data['Global Quote']['05. price'])

def get_currencies(data_currencies):
    for currencie in data_currencies:
        url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currencie}&to_currency=RUB&apikey=N64DYQB2WV5QR1WW'
        r = requests.get(url)
        data = r.json()
        print(data)



# data_ = open_json_currencies(OPEN_JSON)
# get_currencies(data_)
data = open_json_stocks(OPEN_JSON)
get_stocks(data)