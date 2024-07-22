from typing import List, Dict

import os


def sort_by_month(operations: List[Dict], month: str) -> List[Dict]:
    transactions = []
    for operation in operations:
        date = operation.get("Дата платежа")
        if operation.get("Дата платежа") == None|"nan":
            continue
        sort_month = date[3:5]
        print(sort_month)
        if sort_month == month:
            transactions.append(operation)
        else:
            print(f"В заданном месяце {month} транзакции не найдены")
    print(transactions)
    return transactions





if __name__ == "__main__":
    month = "01"
    operations = [{'Дата операции': '01.01.2018 20:27:51', 'Дата платежа': '04.01.2018', 'Номер карты': '*7197', 'Статус': 'OK', 'Сумма операции': -316, 'Валюта операции': 'RUB', 'Валюта платежа': 'RUB', 'Кешбэк': nan, 'Категория': 'Красота', 'МСС': 5977, 'Описание': 'OOO Balid', 'Бонусы (включая кешбэк)': 6, 'Округление на Инвесткопилку': 0, 'Сумма операции с округлением': 316}, {'Дата операции': '01.01.2018 12:49:53', 'Дата платежа': '01.01.2018', 'Номер карты': nan, 'Статус': 'OK', 'Сумма операции': -3000, 'Валюта операции': 'RUB', 'Валюта платежа': 'RUB', 'Кешбэк': nan, 'Категория': 'Переводы', 'МСС': nan, 'Описание': 'Линзомат ТЦ Юность', 'Бонусы (включая кешбэк)': 0, 'Округление на Инвесткопилку': 0, 'Сумма операции с округлением': 3000}]

    print(sort_by_month(operations, month))
