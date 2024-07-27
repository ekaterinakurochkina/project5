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

logger = logging.getLogger("views")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/views.log", "w")
file_formatted = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatted)
logger.addHandler(file_handler)

# *7197 Номер карты
# -160.89 Сумма платежа, отрицательное число
# 31.12.2021
# def filtered_operations():
# operations = []
#     for transaction in transactions:
#         date_excel = transaction["Дата операции"]
#         operation_data = datetime.datetime.strptime(date_excel, "%d.%m.%Y %H:%M:%S")
#         format_date = operation_data.strftime("%Y-%m-%d %H:%M:%S")
#         transaction["Дата операции"] = format_date
#         if month in transaction["Дата операции"]:
#             operations.append(transaction)



def load_user_settings(file_path="src.user_settings.json"):  # Пока не применяю
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


def currency_rate(currency):
    """функция, которая принимает транзакцию и возвращает сумму транзакции"""
    # currency = "USD"
    amount = 1
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={currency}&amount={amount}&date=2021-07-31"
    headers = {"apikey": api_key}
    response = requests.request("GET", url, headers=headers)
    result = response.json()
    date = "2021-07-31"
    from_currency = result["query"]["from"]
    to_currency = result["query"]["to"]
    rate = result["info"]["rate"]
    logging.info("Передаю данные о стоимости акций")
    print(f"Дата: {date}; Валюта: {currency}; Курс: {round(rate,2)}")
    return round(rate, 2)


# Дата: 2024-07-27; Валюта: USD; Курс: 85.97
# Дата: 2024-07-27; Валюта: EUR; Курс: 93.47


# фондовый рынок:
def price_stocks(symbol):
    apikey = os.getenv("APIKEY")
    # symbol = "IBM"
    date = "2021-07-31"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={apikey}"
    # Отправка запроса
    response = requests.get(url)
    data = response.json()
    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=60min&apikey=apikey&month=2024-07&outputsize=1&adjusted=false'
    for day, prices in data["Time Series (Daily)"].items():
        if day == date:
            price = float(prices["1. open"])
            break
    else:
        print(f"Не удалось найти данные для акции на {date}")
    result = f"Дата: {date}, стоимость акции {symbol} составляет {price}"
    print(result)
    return result


if __name__ == "__main__":
    currency_rate("USD")
    currency_rate("EUR")
    # price_stocks("GOOGL")
    # price_stocks("TSLA")
    # price_stocks("AMZN")
    # price_stocks("AAPL")
    # price_stocks("MSFT")
