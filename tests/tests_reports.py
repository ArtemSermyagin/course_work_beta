import json

import pytest
import pandas as pd

from src.reports import spending_by_category



# @pytest.mark.parametrize("dataFrame, category, date, expected_result", [
#     ("dataFrame",'31.12.2021', "Фастфуд")])

# def test_spending_by_category():
dataFrame = pd.read_excel("test_operations.xls")
category = 'Фастфуд'
date = '31.12.2021'
with open('my_data.json', 'r') as file:
    expected_result = json.load(file)
    print(expected_result)
assert spending_by_category(dataFrame, category, date) == [{'Дата операции': 1640794928000, 'Дата платежа': '29.12.2021', 'Номер карты': '*5091', 'Статус': 'OK', 'Сумма операции': -120.0, 'Валюта операции': 'RUB', 'Сумма платежа': -120.0, 'Валюта платежа': 'RUB', 'Кэшбэк': None, 'Категория': 'Фастфуд', 'MCC': 5814.0, 'Описание': 'Mouse Tail', 'Бонусы (включая кэшбэк)': 1, 'Округление на инвесткопилку': 0, 'Сумма операции с округлением': 120.0}]
