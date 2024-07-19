import csv
import sys
from pathlib import Path
from typing import List

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.config import ROOT_PATH


def read_csv(path_to_file: Path) -> List:
    """Функция чтения транзакций из csv-файла"""
    try:
        with open(path_to_file, "r", encoding="utf-8") as csv_file:
            try:
                reader = csv.reader(csv_file, delimiter=",")
                header = next(reader)
                transactions = []
                for row in reader:
                    dict_row = {
                        "Дата операции": row[header.index("Дата операции")],
                        "Дата платежа": row[header.index("Дата платежа")],
                        "Номер карты": row[header.index("Номер карты")],
                        "Статус": row[header.index("Статус")],
                        "Сумма операции": row[header.index("Сумма операции")],
                        "Валюта операции": row[header.index("Валюта операции")],
                        "Валюта платежа": row[header.index("Валюта платежа")],
                        "Кэшбэк": row[header.index("Кэшбэк")],
                        "Категория": row[header.index("Категория")],
                        "МСС": row[header.index("MCC")],
                        "Описание": row[header.index("Описание")],
                        "Бонусы (включая кэшбэк)": row[header.index("Бонусы (включая кэшбэк)")],
                        "Округление на инвесткопилку": row[header.index("Округление на инвесткопилку")],
                        "Сумма операции с округлением": row[header.index("Сумма операции с округлением")],
                    }
                    # print(f" csv _{dict_row}")
                    transactions.append(dict_row)
                # print(f" csv ___{transactions}")
                return transactions
            except Exception as e:
                print(e)
                print("Ошибка чтения csv")
                return []
    except Exception:
        print("Файл не найден")
        return []


if __name__ == "__main__":
    path_to_file = (Path(ROOT_PATH, "../data/Отчет по операциям.csv"))
    print(read_csv(Path(ROOT_PATH, "../data/Отчет по операциям.csv")))


