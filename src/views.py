import os
from pathlib import Path
from typing import Any, Dict, List
import json
import requests
from dotenv import load_dotenv
import logging
from datetime import datetime
import src.utils
import pandas as pd
# import yfinance as yf
from src.utils import read_excel

# from src.сonfig import ROOT_PATH

# Загрузка переменных из .env-файла
load_dotenv()

api_key = os.getenv("API_KEY")

ROOT_PATH = Path(__file__).resolve().parent.parent

logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/main.log", "w")
file_formatted = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatted)
logger.addHandler(file_handler)



def load_user_settings(file_path="src.user_settings.json"): # Пока не применяю
    """Загрузка пользовательских настроек"""
    with open(file_path, "r", encoding="utf-8") as file:
        settings = json.load(file)
        logging.error("Файл не найден")
    # print(settings)   # выведет: {'user_currencies': ['EUR', 'USD'], 'user_stocks': ['GOOGL', 'TSLA', 'AMZN', 'AAPL', 'MSFT']}
    return settings

# Мне не нравится этот вариант получения 5 последних транзакций! Нужен топ-5 по сумме
# def get_top_transactions(
#         date_transactions["Дата операции"] = pd.to_datetime(date_transactions["Дата операции"],
#         format="%Y-%m-%d %H:%M:%S").dt.strftime("%Y-%m-%d %H:%M:%S")
#         top_transactions = date_transactions.nlargest(top_n, "Сумма операции: ")
#         logging.info("Получение 5 последних транзакций")
#         return top_transactions.to_dict(orient="records")


def transaction_amount(currency):
    """функция, которая принимает транзакцию и возвращает сумму транзакции"""
    # currency = "USD"
    amount = 1
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}"
    headers = {"apikey": api_key}
    response = requests.request("GET", url, headers=headers)
    result = response.json() # {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 1}, 'info': {'timestamp': 1722058575, 'rate': 85.972867}, 'date': '2024-07-27', 'result': 85.972867}
    date = result['date']
    from_currency = result['query']['from']
    to_currency = result['query']['to']
    rate = result['info']['rate']

    print(f"Дата: {date}; Валюта: {currency}; Курс: {rate}")
    return result

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
if __name__ == "__main__":
    transaction_amount("USD")
    transaction_amount("EUR")