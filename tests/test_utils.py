# import unittest
import pandas as pd
import pytest
from freezegun import freeze_time
from src.utils import get_greeting, transactions_xlsx_open, collect_response

# from src.views import get_stocks


@pytest.mark.parametrize(
    "hour, expected_greeting",
    [
        (6, "Доброе утро!"),
        (14, "Добрый день!"),
        (19, "Добрый вечер!"),
        (2, "Доброй ночи!"),
    ],
)
@freeze_time("2022-01-01")
def test_greetings(hour, expected_greeting):
    with freeze_time(f"2022-01-01 {hour}:00:00"):
        actual_greeting = get_greeting()
        assert actual_greeting == expected_greeting


def test_transactions_xlsx_open_valid_file():
    expected_output = transactions_xlsx_open()

    result = transactions_xlsx_open()

    assert isinstance(result, pd.DataFrame)
    assert result.equals(expected_output)


def test_collect_response():
    assert collect_response()["cards"] == [
        {"last_digits": "7197", "total_spent": -2212734.539999989, "cashback": 25305.0},
        {"last_digits": "5091", "total_spent": -14918.16, "cashback": 226.0},
        {"last_digits": "4556", "total_spent": 951174.6699999992, "cashback": 7730.0},
        {"last_digits": "1112", "total_spent": -16207.080000000002, "cashback": 164.0},
        {"last_digits": "5507", "total_spent": -84000.0, "cashback": 840.0},
        {"last_digits": "6002", "total_spent": -69200.0, "cashback": 692.0},
        {"last_digits": "5441", "total_spent": -1000.0, "cashback": 10.0},
    ]
    assert collect_response()["top_transactions"] == [
        {
            "date": "21.03.2019 17:01:38",
            "amount": 190044.51,
            "category": "Переводы",
            "description": "Перевод Кредитная карта." " ТП 10.2 RUR",
        },
        {
            "date": "23.10.2018 12:26:15",
            "amount": 177506.03,
            "category": "Переводы",
            "description": "Перевод Кредитная карта. ТП 10.2 RUR",
        },
        {
            "date": "30.12.2021 17:50:17",
            "amount": 174000.0,
            "category": "Пополнения",
            "description": "Пополнение через Газпромбанк",
        },
        {
            "date": "14.09.2021 14:57:42",
            "amount": 150000.0,
            "category": "Пополнения",
            "description": "Перевод с карты",
        },
        {
            "date": "23.10.2018 12:24:54",
            "amount": 150000.0,
            "category": "Переводы",
            "description": "Пополнение счета",
        },
    ]
