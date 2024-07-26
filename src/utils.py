import sys
from pathlib import Path
import datetime
import pandas as pd
import logging

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.config import ROOT_PATH

logger = logging.getLogger("main")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/main.log", "w")
file_formatted = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatted)
logger.addHandler(file_handler)


def read_excel(path_to_file: Path) -> list:
    """Функция чтения транзакций из excel-файла"""
    with open(path_to_file, "r", encoding="utf-8") as excel_file:
        try:
            df = pd.read_excel(
                path_to_file, dtype="object"
            )  # очищаем числовые значения от ненужной информации
            # pd.read_excel("file", dtype="object")
            transactions = []
            for i in range(0, len(df)):
                row_dict = {
                    "Дата операции": df.loc[i, "Дата операции"],
                    "Дата платежа": df.loc[i, "Дата платежа"],
                    "Номер карты": df.loc[i, "Номер карты"],
                    "Статус": df.loc[i, "Статус"],
                    "Сумма операции": df.loc[i, "Сумма операции"],
                    "Валюта операции": df.loc[i, "Валюта операции"],
                    "Валюта платежа": df.loc[i, "Валюта платежа"],
                    "Кешбэк": df.loc[i, "Кэшбэк"],
                    "Категория": df.loc[i, "Категория"],
                    "МСС": df.loc[i, "MCC"],
                    "Описание": df.loc[i, "Описание"],
                    "Бонусы (включая кешбэк)": df.loc[i, "Бонусы (включая кэшбэк)"],
                    "Округление на Инвесткопилку": df.loc[
                        i, "Округление на инвесткопилку"
                    ],
                    "Сумма операции с округлением": df.loc[
                        i, "Сумма операции с округлением"
                    ],
                }
                transactions.append(row_dict)

        except Exception as e:
            print(e)
            print("Ошибка чтения excel")
            return []
    return transactions


def greeting():
    "Функция для определения времени суток и вывода приветствия"
    current_time = datetime.datetime.now()
    logger.info("Приветствие")
    if 6 <= int(current_time.hour) < 12:
        return "Доброе утро!"
    elif 12 <= int(current_time.hour) < 18:
        return "Добрый день!"
    elif 18 <= int(current_time.hour) < 23:
        return "Добрый вечер!"
    else:
        return "Доброй ночи!"


if __name__ == "__main__":
    path_to_file = Path(ROOT_PATH, "../data/operations.xlsx")
    print(read_excel(Path(ROOT_PATH, "../data/operations.xlsx")))
    print(greeting())