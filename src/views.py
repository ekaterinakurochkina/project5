import os
from pathlib import Path
from typing import Any, Dict

import requests
from dotenv import load_dotenv

import src.utils

# from src.сonfig import ROOT_PATH

# Загрузка переменных из .env-файла
load_dotenv()
api_key = os.getenv("API_KEY")


def get_currency_rate(date, currency_code):
    url = f"https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Failed to get currency rate for date {date}")
    data = response.json()
    currency_data = data["Valute"].get(currency_code)
    if not currency_data:
        raise ValueError(f"No data for currency {currency_code}")
    print(f"date: {date},currency_code: {currency_code},rate: {currency_data["Value"]}")
    return {
        "date": date,
        "currency_code": currency_code,
        "rate": currency_data["Value"],
    }

# def transaction_amount(transaction: Dict) -> float | Any:
#     """функция, которая принимает транзакцию и возвращает сумму транзакции"""
#     currency = transaction["operationAmount"]["currency"]["code"]
#     amount = transaction["operationAmount"]["amount"]
#     url = f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}"
#     headers = {"apikey": api_key}
#     response = requests.request("GET", url, headers=headers)
#     result: Any = response.json()
#     return result["result"]


# # Проверка работы кода
# transactions = src.utils.get_transactions(Path(ROOT_PATH, "../data/operations.json"))
#
# transaction = {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589",
# }
# print(transaction_amount(transaction))
