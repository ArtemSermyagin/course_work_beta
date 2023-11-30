# import os
#
import json

import requests

from settings import OPEN_JSON


# from dotenv import load_dotenv
#
# load_dotenv()




# url = "https://api.apilayer.com/exchangerates_data/timeseries/EUR,USD?start_date=2020-10-01&end_date=2020-10-10"
#
# payload = {}
# headers= {
#   "apikey": os.getenv("API_KEY_EXCHANGE")
# }
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text
# print(result)
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
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey=demo'
        r = requests.get(url)
        data = r.json()
        print(data['Global Quote']['01. symbol'], data['Global Quote']['05. price'])

def get_currencies(data_currencies):
    for currencie in data_currencies:
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey=demo'
        r = requests.get(url)
        data = r.json()

        print(data['Realtime Currency Exchange Rate']['1. From_Currency Code'], data['Realtime Currency Exchange Rate']['5. Exchange Rate'])



data_ = open_json_currencies(OPEN_JSON)
get_currencies(data_)
# data = open_json_stocks(OPEN_JSON)
# get_stocks(data)