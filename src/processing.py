from typing import List, Union


def filter_by_state(list_dict: List, state: str = "EXECUTED") -> Union[List, str]:
    """Функция фильтрует список словарей по ключу state и возвращает новый список словарей"""

    # С помощью листа понимания создаем новый список
    # и добавляем в него словари с нужным нам значением кдюча state
    # return [i for i in list_dict if i["state"] == state]
    result = []
    for i in list_dict:
        if state == i["state"]:
            result.append(i)

    if result == []:
        return "Отсутствует нужное значение!"

    return result


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
            "CANCELED",
        )
    )


def sort_by_date(list_dict: List, sort_order: bool = True) -> Union[List, str]:
    """Функция сортирует список словарей по дате"""
    try:
        for i in list_dict:
            data = i["date"]
            if int(data[:4]) and int(data[5:7]) and int(data[8:10]):
                # Сортируем список словарей по ключу date
                result = sorted(list_dict, key=lambda x: x["date"], reverse=sort_order)

    except ValueError:
        # При неправильной дате выводится сообщение
        return "Некорректная дата!"

    return result


if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-04T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-08-03T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
            ]
        )
    )
