import datetime
import json
from typing import Any, Dict, List

# from src.date import month
from src.utils import read_excel


def investment_bank(month: str, transactions: List[Dict[str, Any]], limit: int):
    """Функция, возвращающая сумму, которую можно было бы отложить в Инвесткопилку
    в заданном месяце года при заданном округлении"""
    # month_choice = month(0)

    operations = []
    for transaction in transactions:
        date_excel = transaction["Дата_операции"]
        operation_data = datetime.datetime.strptime(date_excel, "%d.%m.%Y %H:%M:%S")
        format_date = operation_data.strftime("%Y-%m-%d %H:%M:%S")
        transaction["Дата_операции"] = format_date
        if month in transaction["Дата_операции"]:
            operations.append(transaction)
    # print(operations)
    total_investment = 0
    for operation in operations:
        amount = operation["Сумма операции"]

        ceshback = abs(amount) * -1 // limit * -1 * limit
        investment = ceshback - abs(amount)
        operation["Кэшбэк"] = investment  # заполняем в словаре значение кешбэка
        # суммируем кэшбэк за указанный месяц
        total_investment += investment
        total_investment = round(total_investment, 2)

    print(
        f"Итого за {month} в инвесткопилку была бы отложена сумма {total_investment} руб."
    )
    return total_investment


if __name__ == "__main__":
    investment_bank()
