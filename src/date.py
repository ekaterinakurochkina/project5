import datetime


def date_format(date: str)-> str:
    """Функция преобразования даты операции"""
    operation_data = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return operation_data.strftime("%Y-%m-%d")

def month_format(date: str)-> str:
    """Функция преобразования выбранного месяца"""
    month = datetime.strptime(date, "%m")
    return month.strftime("%Y-%m")
