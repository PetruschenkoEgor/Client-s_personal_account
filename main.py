from src.utils import get_transactions_from_json, PATH_TO_FILE
from src.open_csv_and_excel import get_transactions_from_csv, get_transactions_from_excel, PATH_TO_FILE_CSV, PATH_TO_FILE_EXCEL
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency


def main():
    """ Главная функция """
    # Приветствие и предложение выбрать пункт из меню(из какого файла получить информацию)
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла""")

    # Ввод пользователем данных
    input_type_file = input("Введите число от 1 до 3: ")

    # Проверка, что введены корректные данные, ответ пользователю и обработка данных
    while True:
        if input_type_file == "1":
            print("Для обработки выбран JSON-файл.")
            # Функция читает JSON-файлы
            data = get_transactions_from_json(PATH_TO_FILE)
            break
        elif input_type_file == "2":
            print("Для обработки выбран CSV-файл.")
            # Функция читает CSV-файлы
            data = get_transactions_from_csv(PATH_TO_FILE_CSV)
            break
        elif input_type_file == "3":
            print("Для обработки выбран XLSX-файл.")
            # Функция читает XLSX-файлы
            data = get_transactions_from_excel(PATH_TO_FILE_EXCEL)
            break
        else:
            print("Необходимо выбрать число от 1 до 3!")
            input_type_file = input("Введите число от 1 до 3: ")

    # Предложение выполнить фильтрацию по статусу
    print("""Введите статус, по которому необходимо выполнить фильтрацию.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

    # Ввод статуса
    input_state = input("Введите статус для фильтровки: ").upper()

    # Проверка, что введены корректные данные и ответ пользователю
    while True:
        if input_state == "EXECUTED":
            print("Операции отфильтрованы по статусу 'EXECUTED'")
            break
        elif input_state == "CANCELED":
            print("Операции отфильтрованы по статусу 'CANCELED'")
            break
        elif input_state == "PENDING":
            print("Операции отфильтрованы по статусу 'PENDING'")
            break
        else:
            print(f"Статус операции '{input_state}' недоступен.")
            print("""Введите статус, по которому необходимо выполнить фильтрацию.
                Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
            input_state = input("Введите статус для фильтровки: ").lower()
    # Функция фильтрации по ключу state
    filtering_by_state = filter_by_state(data, input_state)

    print("Отсортировать операции по дате? Да/Нет")

    input_date_sort = input("Введите Да/Нет: ").lower()

    while True:
        if input_date_sort == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            input_date_flag = input("Введите по возрастанию/по убыванию: ").lower()
            while True:
                if input_date_flag == "по возрастанию":
                    date_flag = False
                    # Функция сортировки даты
                    # sort_date = sort_by_date(data, date_flag)
                    break
                elif input_date_flag == "по убыванию":
                    date_flag = True
                    # Функция сортировки даты
                    # sort_date = sort_by_date(data, date_flag)
                    break
                else:
                    print("Введите по возрастанию или по убыванию!")
                    print("Отсортировать по возрастанию или по убыванию?")
                    input_date_flag = input("Введите по возрастанию/по убыванию: ").lower()
            break
        elif input_date_sort == "нет":
            break
        else:
            print("Введите Да или Нет!")
            print("Отсортировать операции по дате? Да/Нет")
            input_date_sort = input("Введите Да/Нет: ").lower()

    print("Выводить только рублевые транзакции? Да/Нет")

    input_currency = input("Введите Да/Нет: ").lower()

    while True:
        if input_currency == "да":
            currency = "RUB"
            # Транзаакции по заданной валюте
            # transactions_rub = filter_by_currency(transactions, currency)
            break
        elif input_currency == "нет":
            break
        else:
            print("Введите Да или Нет!")
            print("Выводить только рублевые транзакции? Да/Нет")
            input_currency = input("Введите Да/Нет: ").lower()

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")

    input_word = input("Введите Да/Нет: ").lower()

    while True:
        if input_word == "да":

            break
        elif input_word == "нет":
            break
        else:
            print("Введите Да или Нет!")
            print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
            input_word = input("Введите Да/Нет: ").lower()

    print("Распечатываю итоговый список транзакций...")

    return filtering_by_state




if __name__ == '__main__':
    main()
