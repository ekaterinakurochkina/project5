import os

from src.date import date_format, month_format
from src.read_excel import read_excel

def main():
    """Функция упраления проектом"""
    print("""Добро пожаловать в раздел 'Сервис'
    Предлагаем ознакомиться с возможностями Инвест-копилки.
    Хотите знать, сколько денег Вы могли бы отложить в Инвест-копилку за месяц?
    """)
    while True:
        es_no = input("Введите 'да' или 'нет': ").lower()
        if es_no == "да":
            while True:
                month_choice = int(input(f"Введите порядковый номер месяца, например, 4 (тогда будет выбран апрель): "))
                if 0 < month_choice <10:
                    month = "0" + str(month_choice)
                    print(f"Выбран {month}")
                    break
                elif 9 < month_choice < 13:
                    month = month_choice
                    print(f"Выбран {month}")
                    break
                else:
                    print("Ошибка. Введите число в диапазоне от 1 до 12.")
                    break
            break
        else:
            if es_no == "нет":
                print("Хорошо. До встречи!")
                break


# if __name__ == "__main__":
#     main()