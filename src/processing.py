from typing import List


def filter_by_state(list_dict: List, state: str = "EXECUTED") -> List:
    """Функция фильтрует список словарей по ключу state и возвращает новый список словарей"""

    # С помощью листа понимания создаем новый список
    # и добавляем в него словари с нужным нам значением кдюча state
    return [i for i in list_dict if i["state"] == state]


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )


def sort_by_date(list_dict: List, sort_order: bool = True) -> List:
    """Функция сортирует список словарей по дате"""
    # Сортируем список словарей по ключу date
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=sort_order)

    return sorted_list


if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )
