import json

from settings import OPEN_XLS
from src.reports import spending_by_category
from src.services import search_transactions
from src.utils import collect_response, transactions_xlsx_open

if __name__ == "__main__":
    result = collect_response()
    print(json.dumps(result, indent=4, ensure_ascii=False))

    dataFrame = transactions_xlsx_open()
    result_reposts = spending_by_category(dataFrame, 'Фастфуд', '25.03.2018')
    print(result_reposts)

    file_path = OPEN_XLS  # Путь к файлу Excel
    query = "Перевод"  # Строка запроса
    result = search_transactions(file_path, query)
    print(result)
