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
def filtered_operations():
    """Функция страницы Главная, выводит номера карт, топ-5 трат и кэшбэк 1 руб. на каждые 100 руб."""
    # path_to_file = Path(ROOT_PATH, "../data/operations.xlsx")
    path_to_file = "../data/operations.xlsx"
    transactions = read_excel(path_to_file)
    operations = []
    card_numbers = []
    counter_amount = 0
    # отсортировываем транзакции за месяц 07.2021
    for transaction in transactions:
        date_excel = transaction["Дата операции"]
        operation_data = datetime.strptime(date_excel, "%d.%m.%Y %H:%M:%S")
        format_date = operation_data.strftime("%Y.%m.%d")
        transaction["Дата платежа"] = format_date
        if "2021.07" in transaction["Дата платежа"]:
            operations.append(transaction)
            counter_amount += abs(transaction["Сумма операции"])
            # записываем номера карт
            if (
                transaction["Номер карты"] not in card_numbers
                and transaction["Номер карты"]
            ):
                card_numbers.append(transaction["Номер карты"])

    # Отсортируем словарь по величине суммы транзакции в порядке убывания
    sorted_operations = sorted(
        operations, key=lambda x: abs(x["Сумма операции"]), reverse=True
    )

    # Выберем первые 5 элементов из отсортированного списка
    top_5_transactions = sorted_operations[:5]
    result = []
    count = 0
    for top in top_5_transactions:
        count += 1
        result.append(f"{count}. {top["Описание"]} : {top["Сумма операции"]}")
    print("Топ-5 транзакций:")
    for transaction in result:
        print(transaction)
    print("В июле 2021 года операции совершались со следующих банковсих карт:")
    for number in card_numbers:
        print(number)
    # рассчитываем кешбэк
    cashback = round(counter_amount / 100, 2)
    print(f"Сумма расходов за июль 2021 года составляет: {counter_amount} руб.")
    print(f"Сумма кешбэка за июль 2021 года составляет: {cashback} руб.")
    # print(operations)
    return operations


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
    # currency_rate("USD")
    # currency_rate("EUR")
    # price_stocks("GOOGL")
    # price_stocks("TSLA")
    # price_stocks("AMZN")
    # price_stocks("AAPL")
    # price_stocks("MSFT")
    filtered_operations()
