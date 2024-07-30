import json
import logging
import os

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# Путь к файлу operations.json в директории data
PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")


def get_transactions_from_json(PATH_TO_FILE):
    """Функция принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info(f"Записываем данные в файл {PATH_TO_FILE}")
        with open(PATH_TO_FILE, encoding="utf_8") as file:
            data = json.load(file)
        return data

    # Если файл пустой или содержит не список
    except json.JSONDecodeError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []
    # Если файл не найден
    except FileNotFoundError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []


if __name__ == "__main__":
    print(get_transactions_from_json(PATH_TO_FILE))
