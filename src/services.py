import json
import datetime

from typing import Dict, List, Any
# from src.date import month
from src.read_excel import read_excel


# transactions = [
#     {'Дата операции': '01.01.2019 20:27:51',
#      'Дата платежа': '04.01.2018',
#      'Номер карты': '*7197',
#      'Статус': 'OK',
#      'Сумма операции': -316,
#      'Валюта операции': 'RUB',
#      'Валюта платежа': 'RUB',
#      'Кешбэк': 0,
#      'Категория': 'Красота',
#      'МСС': 5977,
#      'Описание': 'OOO Balid',
#      'Бонусы (включая кешбэк)': 6,
#      'Округление на Инвесткопилку': 0,
#      'Сумма операции с округлением': 316},
#     {'Дата операции': '01.01.2018 12:49:53',
#      'Дата платежа': '01.01.2018',
#      'Номер карты': 0,
#      'Статус': 'OK',
#      'Сумма операции': -3000,
#      'Валюта операции': 'RUB',
#      'Валюта платежа': 'RUB',
#      'Кешбэк': 0,
#      'Категория': 'Переводы',
#      'МСС': 0,
#      'Описание': 'Линзомат ТЦ Юность',
#      'Бонусы (включая кешбэк)': 0,
#      'Округление на Инвесткопилку': 0,
#      'Сумма операции с округлением': 3000}
#     ]
# month ="2018-01"
# limit = 100
def investment_bank(month: str, transactions: List[Dict[str,Any]], limit:int):
    """Функция, возвращающая сумму, которую можно было бы отложить в Инвесткопилку
    в заданном месяце года при заданном округлении"""
    month_choice = month(0)
    operations = []
    for transaction in transactions:
        date_excel = transaction["Дата операции"]
        operation_data = datetime.datetime.strptime(date_excel, "%d.%m.%Y %H:%M:%S")
        format_date = operation_data.strftime("%Y-%m-%d %H:%M:%S")
        transaction["Дата операции"] = format_date
        if month_choice in transaction["Дата операции"]:
            operations.append(transaction)
    # print(operations)
    total_investment = 0
    for operation in operations:
        amount = operation["Сумма операции"]
        ceshback = amount * -1 // limit * -1 * limit
        investment = ceshback - amount
        operation["Кэшбэк"] = investment  # заполняем в словаре значение кешбэка
    # суммируем кэшбэк за указанный месяц
        total_investment += investment
        total_investment = round(total_investment,2)

    print(f"Итого за {month_choice} в инвесткопилку была бы отложена сумма {total_investment} руб.")
    return total_investment

# if __name__ == "__main__":
#     investment_bank()
