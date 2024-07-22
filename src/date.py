import datetime



def month(month_choice: int)-> str:
    """Функция преобразования выбранного месяца"""
#Запрашиваем месяц
    while True:
        month_choice = int(input(f"Введите порядковый номер месяца, например, 4 (тогда будет выбран апрель): "))
        if 0 < month_choice < 10:
            month = "2021.0" + str(month_choice)
            print(f"Выбран {month}")
            break
        elif 9 < month_choice < 13:
            month = "2021." + str(month_choice)
            print(f"Выбран {month}")
            break
        else:
            print("Ошибка. Введите число в диапазоне от 1 до 12.")
            continue
    return month

# def limit(user_limit: int) -> int:
#     """Функция выбора лимита округления"""
#     while True:
#         limit = int(input(
#             "Выберите комфортную Вам сумму округления остатка для инвесткопилки.Введите число 10, 50 или 100: "))
#         if limit == 10 or limit == 50 or limit == 100:
#             print(f"Выбрано округление до {limit} рублей")
#             break
#         else:
#             print("Ошибка ввода")
#             continue






# if __name__ == "__main__":
    # month(1)
    # limit(1)
