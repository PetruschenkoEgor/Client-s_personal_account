import json


def get_transactions_json():
    """ Функция принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях """
    data = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    with open('operations.json', 'w') as f:
        json.dump(data, f)