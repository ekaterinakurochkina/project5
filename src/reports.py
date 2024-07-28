import sys
from pathlib import Path
import pandas as pd
from datetime import datetime, timedelta
import pandas as pd
import logging
from src.utils import data_to_df

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.config import ROOT_PATH

logger = logging.getLogger("reports")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/reports.log", "w")
file_formatted = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatted)
logger.addHandler(file_handler)


def spending_by_category(
    transactions: pd.DataFrame, category: str, date: [str] = None
) -> pd.DataFrame:
    # """Функция-отчет по транзакциям в указанной категории"""
    df = transactions
    date = pd.to_datetime("31.07.2021")  #'2021-07-31'
    # # Указываем дату, от которой нужно отобрать последние три месяца
    if date == None:
        date = pd.to_datetime("31.07.2021")
    # Вычисляем дату начала периода (3 месяца назад)
    start_date = date - pd.Timedelta(days=92)

    # Фильтруем датафрейм по дате
    filtered_df = df[
        (pd.to_datetime(df["Дата операции"]) >= start_date)
        & (pd.to_datetime(df["Дата операции"]) <= date)
    ]

    # рассчитываем сумму расходов по каждой категории
    sum_price_by_category = filtered_df.groupby("Категория")["Сумма операции"].sum()

    # выводим сумму расходов в заданной категории
    result = print(
        f"Траты в категории {category} за последние 3 месяца составили {sum_price_by_category[category]} руб."
    )
    logger.info("Выдаю данные по расходам в категории")
    return result


if __name__ == "__main__":
    path_to_file = Path(ROOT_PATH, "../data/operations.xlsx")
    transactions = data_to_df(path_to_file)
    # print(transactions.head())

    spending_by_category(transactions, "Супермаркеты")
