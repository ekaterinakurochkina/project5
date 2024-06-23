from typing import List, Dict


def filter_by_state(list_dict: List[Dict], key_dict: str = "EXECUTED") -> List[Dict]:
    """Функция фильтрации операций по ключу"""
    filtered_list = []
    for i in range(len(list_dict)):
        if list_dict[i].get("state") == key_dict:
            filtered_list.append(list_dict[i])
    return filtered_list


"""Проверка работы кода"""
list_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
key_dict = "EXECUTED"
# key_dict = 'CANCELED'
print(filter_by_state(list_dict, key_dict))


def sort_by_date(list_dict: list[Dict], ascending: bool = True) -> list[Dict]:
    """Функция сортировки операций по убыванию даты"""
    for current_dict in list_dict:
        if current_dict.get("date") is None:
            return list_dict
        else:
            sort_dict = sorted(list_dict, key=lambda x: x["date"], reverse=ascending)
    return sort_dict


"""Проверка работы кода"""
list_dict = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(sort_by_date(list_dict))

