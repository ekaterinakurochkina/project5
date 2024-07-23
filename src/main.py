import json
import os
from src.read_excel import read_excel
from src.services import investment_bank
import sys
import logging
from pathlib import Path
import pandas as pd
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.config import ROOT_PATH
from src.date import month, limit

path_to_file = (Path(ROOT_PATH, "../data/operations.xlsx"))

logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/main.log", "w")
file_formatted = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatted)
logger.addHandler(file_handler)
def main():
    """Функция упраления проектом"""
    print("""Добро пожаловать в раздел 'Сервис'
    Предлагаем ознакомиться с возможностями Инвест-копилки.
    Хотите знать, сколько денег Вы могли бы отложить в Инвест-копилку за месяц?
    """)
    while True:
        es_no = input("Введите 'да' или 'нет': ").lower()
        if es_no == "да":
            # Читаем данные из excel-файла
            transactions = read_excel(path_to_file)
            while True:
                limit = int(input(
                    "Выберите комфортную Вам сумму округления остатка для инвесткопилки.Введите число 10, 50 или 100: "))
                if limit == 10 or limit == 50 or limit == 100:
                    print(f"Выбрано округление до {limit} рублей")
                    break
                else:
                    print("Ошибка ввода")
                    continue
            total_investment = investment_bank(month, transactions, limit)
            logger.info(f"Производим расчет сумм для инвесткопилки")
            # создаем json-строку
            data = {"total_investment" : total_investment}
            json_data =json.dumps((data))
            print(f"Json-ответ: {json_data}")
            return json_data
        elif es_no == "нет":
            print("Хорошо. До встречи!")
            break
        else:
            logger.error("Ошибка")
            print("Ошибка ввода")
            continue


if __name__ == "__main__":
    main()
