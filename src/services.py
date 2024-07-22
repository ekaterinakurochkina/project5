import json
from typing import Dict, List, Any
# from src.date import limit, month
from src.read_excel import read_excel

def investment_bank(month: str, transactions: List[Dict[str,Any]], limit:int):
    """Функция, возвращающая сумму, которую можно было бы отложить в Инвесткопилку
    в заданном месяце года при заданном округлении"""
    operations = sorted(transactions, key=lambda transactions: month in transactions["Дата операции"])
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
    print(f"Итого за {month} в инвесткопилку была бы отложена сумма {total_investment} руб.")
    return total_investment

