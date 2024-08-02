import csv
import pandas as pd
import os


PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")
PATH_TO_FILE_EXCEL = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions_excel.xlsx")

def get_transactions_from_csv(path_to_file: str) -> None:
    """ Читает транзакции из CSV-файла """
    # Открываем файл для чтения
    with open(path_to_file, encoding="utf_8") as file_csv:
        reader = csv.DictReader(file_csv, delimiter=';')
        # Читаем файл построчно
        for row in reader:
            print(row)


if __name__ == "__main__":
    get_transactions_from_csv(PATH_TO_FILE_CSV)

def get_transactions_from_excel(path_to_file: str) -> None:
    """ Читает транзакции из Excel-файла """
    excel_data = pd.read_excel(path_to_file)

    print(excel_data)


if __name__ == "__main__":
    get_transactions_from_excel(PATH_TO_FILE_EXCEL)
