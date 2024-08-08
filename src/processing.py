from typing import List, Union
import re
from collections import Counter


def filter_by_state(list_dict: List, state: str = "EXECUTED") -> Union[List, str]:
    """Функция фильтрует список словарей по ключу state и возвращает новый список словарей"""

    # С помощью листа понимания создаем новый список
    # и добавляем в него словари с нужным нам значением кдюча state
    # return [i for i in list_dict if i["state"] == state]
    result = []
    for i in list_dict:
        if state == i.get("state"):
            result.append(i)

    if result == []:
        return "Отсутствует нужное значение!"

    return result


# if __name__ == "__main__":
#     print(
#         filter_by_state(
#             [
#                 {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#                 {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#                 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             ],
#             "CANCELED",
#         )
#     )


def sort_by_date(list_dict: List, sort_order: bool = True) -> Union[List, str]:
    """Функция сортирует список словарей по дате"""
    try:
        for i in list_dict:
            data = i.get("date")
            if int(data[:4]) and int(data[5:7]) and int(data[8:10]):
                # Сортируем список словарей по ключу date
                result = sorted(list_dict, key=lambda x: x.get("date"), reverse=sort_order)

    except ValueError:
        # При неправильной дате выводится сообщение
        return "Некорректная дата!"
    return result


# if __name__ == "__main__":
#     print(
#         sort_by_date(
#             [
#                 {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#                 {"id": 939719570, "state": "EXECUTED", "date": "2019-07-04T02:08:58.425572"},
#                 {"id": 594226727, "state": "CANCELED", "date": "2019-08-03T21:27:25.241689"},
#                 {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
#             ]
#         )
#     )


def search_in_operations(list_operations: list[dict], search_str: str) -> list[dict]:
    """Принимает список словарей с банковскими операциями и строку поиска, возращает список словарей,
    в которых есть данная строка"""
    if search_str == "" or search_str == " ":
        result = []
    else:
        # С помощью re выбираем из списка нужные банковские операции
        result = [
            operation
            for operation in list_operations
            if re.search(search_str, operation.get("description"), flags=re.IGNORECASE)
        ]

    return result


if __name__ == "__main__":
    print(
        search_in_operations(
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                },
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "to": "Счет 35383033474447895560",
                },
                {
                    "id": 587085106,
                    "state": "EXECUTED",
                    "date": "2018-03-23T10:45:06.972075",
                    "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 41421565395219882431",
                },
                {
                    "id": 743278119,
                    "state": "EXECUTED",
                    "date": "2018-10-15T08:05:34.061711",
                    "operationAmount": {"amount": "51203.12", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "MasterCard 1435442169918409",
                    "to": "Maestro 7452400219469235",
                },
            ],
            "Перевод организации",
        )
    )


def get_operations_info(list_operations: list[dict], list_categories: list) -> dict:
    """Принимает список словарей с банковскими операциями и список категорий операций,
    возвращает словарь {категория: кол-во операций}"""
    # Список со всеми операциями
    type_operations = [operation.get("description") for operation in list_operations]

    # Подсчитываем количество каждого типа операций
    counted_type_operations = Counter(type_operations)

    return counted_type_operations


# if __name__ == '__main__':
#     print(get_operations_info([
#   {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },
#         {
#             "id": 41428829,
#             "state": "EXECUTED",
#             "date": "2019-07-03T18:35:29.512364",
#             "operationAmount": {
#                 "amount": "8221.37",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "MasterCard 7158300734726758",
#             "to": "Счет 35383033474447895560"
#         },
#         {
#             "id": 587085106,
#             "state": "EXECUTED",
#             "date": "2018-03-23T10:45:06.972075",
#             "operationAmount": {
#                 "amount": "48223.05",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Открытие вклада",
#             "to": "Счет 41421565395219882431"
#         }
#     ], ["Перевод организации", "Открытие вклада", "Перевод со счета на счет", "Перевод с карты на карту",
#     "Перевод с карты на счет"]))
