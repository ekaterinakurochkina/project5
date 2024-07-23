import os
from src.read_excel import read_excel
from src.services import investment_bank
import sys
from pathlib import Path
import pandas as pd
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.config import ROOT_PATH
from src.date import month, limit

path_to_file = (Path(ROOT_PATH, "../data/operations.xlsx"))
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
            # Запрашиваем месяц
            # while True:
            #     month_choice = int(input(f"Введите порядковый номер месяца, например, 4 (тогда будет выбран апрель): "))
            #     if 0 < month_choice < 10:
            #         month = "2021.0" + str(month_choice)
            #         print(f"Выбран {month}")
            #         break
            #     elif 9 < month_choice < 13:
            #         month = "2021." + str(month_choice)
            #         print(f"Выбран {month}")
            #         break
            #     else:
            #         print("Ошибка. Введите число в диапазоне от 1 до 12.")
            #         continue
            # Запрашиваем лимит округления
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
            return total_investment
        elif es_no == "нет":
            print("Хорошо. До встречи!")
            break
        else:
            print("Ошибка ввода")
            continue






if __name__ == "__main__":
    main()