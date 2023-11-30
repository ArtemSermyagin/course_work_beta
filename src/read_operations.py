import json
import math
import numpy as np
import pandas as pd

from settings import OPEN_XLS

def transactions_xlsx_open(path):
    """
    Функция считывает файлы excel
    :param path: path
    :return: dict
    """
    try:
        transactions_excel = pd.read_excel(path).head(10)
        return transactions_excel.to_dict("records")
    except ValueError:
        return "Ошибка чтения файла excel"


def get_last_digits(trans_dict):
    list_card = []
    for number in trans_dict:
        if type(number['Номер карты']) != float:
            # print(number)
            card = (number['Номер карты'][-4:])
            # print(card)
            list_card.append(card)
        else:
            continue
    print(list(set(list_card)))

def get_top_transactions(transactions):
    sorted_transactions = sorted(transactions, key=lambda t: t["Сумма платежа"], reverse=True)
    top_transactions = sorted_transactions
    return top_transactions



trans_dict = transactions_xlsx_open(OPEN_XLS)
get_last_digits(trans_dict)
print(get_top_transactions(trans_dict))



# print(transactions_xlsx_open(OPEN_XLS))
