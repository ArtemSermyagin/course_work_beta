import json
from datetime import datetime, timedelta
import pandas as pd
from settings import OPEN_XLS


def get_greeting():
    current_hour = datetime.now().hour
    if current_hour < 6:
        return "Доброй ночи"
    elif current_hour < 12:
        return "Доброе утро"
    elif current_hour < 18:
        return "Добрый день"
    else:
        return "Добрый вечер"

def transactions_xlsx_open():
    """
    Функция считывает файлы excel
    :param path: path
    :return: dict
    """
    try:
        return pd.read_excel(OPEN_XLS)
    except ValueError:
        return "Ошибка чтения файла excel"

def process_data(start):
    start_date = pd.to_datetime(start)
    df = transactions_xlsx_open()

    data = []

    # Исключаем пустые строки в данных о картах
    df = df.dropna(subset=['Номер карты'])

    # Фильтруем данные с начала месяца до введенной даты
    df['Дата операции'] = pd.to_datetime(df['Дата операции'], format='%d.%m.%Y %H:%M:%S')
    df = df[df['Дата операции'] >= start_date]

    for card_num in df['Номер карты'].unique():
        # Инициализируйте переменные для подсчета суммы платежей и кэшбэка для текущей карты:
        total_spent = 0
        cashback = 0

        # Фильтруйте данные по номеру карты:
        card_data = df[df['Номер карты'] == card_num]

        # Пройдитесь по каждой операции и обновите значения суммы платежей и кэшбэка:
        for index, row in card_data.iterrows():
            total_spent += row['Сумма платежа']
            cashback += row['Сумма платежа'] // 100  # Расчет кэшбэка

        # Добавьте информацию о текущей карте в список карт:
        data.append({
            "last_digits": card_num[-4:],  # Последние 4 цифры номера карты
            "total_spent": total_spent,
            "cashback": cashback
        })

    return data

def top_transactions(transactions):
    top_transactions = transactions.sort_values(by='Дата операции').nlargest(5, 'Сумма платежа')
    top = []
    for index, row in top_transactions.iterrows():
        top.append({
            "date": row['Дата операции'],  # Форматирование даты в требуемом формате
            "amount": float(row['Сумма платежа']),
            "category": row['Категория'],
            "description": row['Описание']
        })
    return top

# input_date = input("Введите дату и время в формате YYYY-MM-DD HH:MM:SS: ")
# start_date = pd.to_datetime(input_date)
#
# response = process_data(start_date)
# print(response)

data_file = transactions_xlsx_open()
# print(top_transactions(data_file))

print({
    "greeting": get_greeting(),
    "cards": process_data("2018-05-21 00:00:00"),
    "top_transactions": top_transactions(data_file)
})
