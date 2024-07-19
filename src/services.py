import json
from typing import Dict, List, Any


def investment_bank(month: str, transactions: List[Dict[str,Any]], limit:int):
    """Функция, возвращающая сумму, которую можно было бы отложить в Инвесткопилку
    в заданном месяце года при заданном округлении"""



    # Округляю до 10, 50, 100 руб.
    # a = float(input("Введите число: "))
    # a_round = int(a * -1 // 10 * -1 * 10)
    # print(f"{a} округляю до 10: {a_round}")
    #
    # b_round = int(a * -1 // 50 * -1 * 50)
    # print(f"{a} округляю до 50: {b_round}")
    #
    # c_round = int(a * -1 // 100 * -1 * 100)
    # print(f"{a} округляю до 100: {c_round}")