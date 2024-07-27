import json
import os


# Путь к файлу operations.json в директории data
PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")

def get_transactions_from_json(PATH_TO_FILE):
    """ Функция принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях """
    try:
        with open(PATH_TO_FILE, encoding='utf_8') as file:
            data = json.load(file)
        return data

    # Если файл пустой или содержит не список
    except json.JSONDecodeError:
        print([])
    # Если файл не найден
    except FileNotFoundError:
        print([])

if __name__ == "__main__":
    print(get_transactions_from_json(PATH_TO_FILE))
