import os
from math import nan
from pathlib import Path
import json
import requests
from dotenv import load_dotenv
import logging
from datetime import datetime

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

# В таком виде представлены данные:
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
        # date_excel = transaction["Дата_операции"]
        # operation_data = datetime.strptime(date_excel, "%d.%m.%Y %H:%M:%S")
        # format_date = operation_data.strftime("%Y.%m.%d")
        # transaction["Дата_платежа"] = format_date
        if "07.2021" in str(transaction["Дата_платежа"]):
            operations.append(transaction)
            counter_amount += abs(transaction["Сумма операции"])
            # записываем номера карт
            if (
                transaction["Номер карты"] not in card_numbers
                and transaction["Номер карты"] != nan
            ):
                card_numbers.append(transaction["Номер карты"])
    # print(operations)
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
        result.append(f"{count}. {top["Категория"]} : {top["Сумма операции"]}")
    logger.info("Производится расчет топ-5 транзакций по сумме операций")
    print("Топ-5 транзакций:")
    for transaction in result:
        print(transaction)
    print("В июле 2021 года операции совершались со следующих банковсих карт:")
    for number in card_numbers:
        print(number)
    # рассчитываем кешбэк
    logger.info("Рассчитываем кешбэк")
    cashback = round(counter_amount / 100, 2)
    print(
        f"Сумма расходов за июль 2021 года составляет: {round(counter_amount,2)} руб."
    )
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


def currency_rate(currency):
    """функция, которая принимает код валюты и возвращает ее курс на дату 31.07.2021"""
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
    logging.info("Передаю данные о курсе валют")
    print(f"Дата: {date}; Валюта: {currency}; Курс: {round(rate,2)}")
    return rate


# фондовый рынок:
def price_stocks(symbol):
    """Функция, принимающая код акции и возвращающая ее стоимость на дату 01.07.2024"""
    apikey = os.getenv("APIKEY")
    date = "2024-07-01"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={apikey}"
    # Отправка запроса
    response = requests.get(url)
    data = response.json()
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=60min&apikey=apikey&month=2024-07&outputsize=1&adjusted=false"
    for day, prices in data["Time Series (Daily)"].items():
        if day == date:
            price = float(prices["1. open"])
            break
    else:
        print(f"Не удалось найти данные для акции на {date}")
    logger.info("Передаю данные о стоимости акций")
    result = f"Дата: {date}, стоимость акции {symbol} составляет {price}"
    print(result)
    return price


# if __name__ == "__main__":
# currency_rate("USD")
# currency_rate("EUR")
# price_stocks("GOOGL")
# price_stocks("TSLA")
# price_stocks("AMZN")
# price_stocks("AAPL")
# price_stocks("MSFT")
# filtered_operations()
