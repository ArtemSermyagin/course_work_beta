import pandas as pd
import json

from settings import OPEN_XLS


# df = pd.read_excel(OPEN_XLS)
#
# data = {
#   "greeting": "Добрый день",
#   "cards": [],
#   "top_transactions": []
# }
# df = df.dropna(subset=['Номер карты'])
# for card_num in df['Номер карты'].unique():
#     # Инициализируйте переменные для подсчета суммы платежей и кэшбэка для текущей карты:
#     total_spent = 0
#     cashback = 0
#
#     # Фильтруйте данные по номеру карты:
#     card_data = df[df['Номер карты'] == card_num]
#
#     # Пройдитесь по каждой операции и обновите значения суммы платежей и кэшбэка:
#     for index, row in card_data.iterrows():
#         total_spent += row['Сумма платежа']
#         cashback += row['Сумма платежа'] // 100  # Расчет кэшбэка
#
#     # Добавьте информацию о текущей карте в список карт:
#     data['cards'].append({
#         "last_digits": card_num[-4:],  # Последние 4 цифры номера карты
#         "total_spent": total_spent,
#         "cashback": cashback
#     })
#
#
# top_transactions = df.sort_values(by='Дата операции').nlargest(5, 'Сумма платежа')
# for index, row in top_transactions.iterrows():
#     data['top_transactions'].append({
#         "date": row['Дата операции'],  # Форматирование даты в требуемом формате
#         "amount": float(row['Сумма платежа']),
#         "category": row['Категория'],
#         "description": row['Описание']
#     })
#
# json_data = json.dumps(data, indent=4, ensure_ascii=False)
# print(json_data)

# 2018-05-21 00:00:00

def process_data(start_date):
    df = pd.read_excel(OPEN_XLS)

    data = {
        "greeting": "Добрый день",
        "cards": [],
        "top_transactions": []
    }

    df = df.dropna(subset=['Номер карты'])

    df['Дата операции'] = pd.to_datetime(df['Дата операции'], format='%d.%m.%Y %H:%M:%S')
    df = df[df['Дата операции'] >= start_date]

    card_nums = df['Номер карты'].unique()

    for card_num in card_nums:
        card_data = df[df['Номер карты'] == card_num]
        total_spent = card_data['Сумма платежа'].sum()
        cashback = total_spent // 100

        data['cards'].append({
            "last_digits": card_num[-4:],
            "total_spent": total_spent,
            "cashback": cashback
        })

        top_transactions = card_data.nlargest(5, 'Сумма платежа')
        for index, row in top_transactions.iterrows():
            transaction = {
                'card_num': card_num,
                'date': row['Дата операции'],
                'amount': row['Сумма платежа']
            }
            data['top_transactions'].append(transaction)

    return json.dumps(data, indent=4, ensure_ascii=False)


input_date = input("Введите дату и время в формате YYYY-MM-DD HH:MM:SS: ")
start_date = pd.to_datetime(input_date)

response = process_data(start_date)
print(response)

# def process_data(start_date):
#     df = pd.read_excel(OPEN_XLS)
#
#     data = {
#         "greeting": "Добрый день",
#         "cards": [],
#         "top_transactions": []
#     }
#
#     df = df.dropna(subset=['Номер карты'])
#
#     df['Дата операции'] = pd.to_datetime(df['Дата операции'], format='%d.%m.%Y %H:%M:%S')
#     df = df[df['Дата операции'] >= start_date]
#
#     card_nums = df['Номер карты'].unique()
#
#     for card_num in card_nums:
#         card_data = df[df['Номер карты'] == card_num]
#         total_spent = card_data['Сумма платежа'].sum()
#         cashback = total_spent // 100
#
#         data['cards'].append({
#             "last_digits": card_num[-4:],
#             "total_spent": total_spent,
#             "cashback": cashback
#         })
#
        # top_transactions = card_data.nlargest(5, 'Сумма платежа')
        # for index, row in top_transactions.iterrows():
        #     transaction = {
        #         'card_num': card_num,
        #         'date': row['Дата операции'],
        #         'amount': row['Сумма платежа']
        #     }
        #     data['top_transactions'].append(transaction)
#
#     return json.dumps(data, indent=4, ensure_ascii=False)
#
#
# input_date = input("Введите дату и время в формате YYYY-MM-DD HH:MM:SS: ")
# start_date = pd.to_datetime(input_date)
#
# response = process_data(start_date)
# print(response)