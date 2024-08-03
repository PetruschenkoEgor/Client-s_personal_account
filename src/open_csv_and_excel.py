import csv
import os

import pandas as pd

PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")


def get_transactions_from_csv(path_to_file: str) -> list[dict[str, int | str]]:
    """Читает транзакции из CSV-файла"""
    try:
        # Открываем файл для чтения
        with open(path_to_file, encoding="utf-8") as file_csv:
            reader = csv.DictReader(file_csv, delimiter=";")
            # Выдает список словарей с транзакциями
            transaction_list = [row for row in reader]
            # transactions = []
            # for d in transaction_list:
            #     transactions.append({k: v for k, v in d.items() if v != ""})
            # Удаляет ключи с пустыми значениями
            transactions = [{k: v for k, v in d.items() if v != ""} for d in transaction_list]

        return transactions
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    print(get_transactions_from_csv(PATH_TO_FILE_CSV))


def get_transactions_from_excel(path_to_file: str) -> list[dict]:
    """Читает транзакции из Excel-файла"""
    try:
        # Считываем Excel-файл
        transactions_excel = pd.read_excel(path_to_file)

        # Убираем значения NaN
        transactions_excel_not_nan = transactions_excel.loc[transactions_excel["from"].notnull()]

        # Преобразуем числа с плавающей точкой в int64
        transactions_excel_not_nan = transactions_excel_not_nan.astype({"id": "int64", "amount": "int64"})

        # Преобразуем полученные данные в список словарей
        transactions_list_dicts = transactions_excel_not_nan.to_dict(orient="records")

        return transactions_list_dicts
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    print(get_transactions_from_excel(PATH_TO_FILE_EXCEL))
