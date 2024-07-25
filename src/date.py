# import datetime
def limit(user_limit: int) -> int:
    """Функция выбора лимита округления"""
    while True:
        limit = int(
            input(
                """Выберите комфортную Вам сумму округления остатка для инвесткопилки.
                Введите число 10, 50 или 100: """
            )
        )
        if limit == 10 or limit == 50 or limit == 100:
            print(f"Выбрано округление до {limit} рублей")
            break
        else:
            print("Ошибка ввода")
    #             continue
    return limit


# if __name__ == "__main__":

# Перенесено в main
# def month(month_choice: int) -> str:
#     """Функция преобразования выбранного месяца"""
#     # Запрашиваем месяц
#     while True:
#         month = int(
#             input(
#                 f"Для расчета возьмём 2021 год.
#                 Введите порядковый номер месяца от 1 до 12: "
#             )
#         )
#         if 0 < month < 10:
#             month_choice = "2021-0" + str(month)
#             break
#         elif 9 < month_choice < 13:
#             month_choice = "2021-" + str(month)
#             break
#         else:
#             print("Ошибка. Введите число в диапазоне от 1 до 12.")
#             continue
#
#     return month_choice
