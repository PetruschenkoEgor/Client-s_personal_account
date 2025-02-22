transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions, currency):
    """Функция принимает на вход список словарей(транзакции) и возвращает итератор,
    который поочередноо выдает транзакции(по заданной валюте)"""
    # Если на вход поступил пустой список
    if transactions == []:
        # Обработка исключения StopIteration
        while True:
            yield "Пустой список! Введите данные!"
    # Если на вход поступил не пустой список
    else:
        # Фильтрация списка словарей по наименованию валюты
        for x in list(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)):
            yield x
        # Обработка исключения StopIteration
        while True:
            yield "Транзакции с указанной валютой отсутствуют!"


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(3):
    print(next(usd_transactions))


def transaction_descriptions(transactions):
    """Принимает на вход список словарей(транзакций) и возвращает описание каждой операции по очереди"""
    # Если на вход поступил пустой список
    if transactions == []:
        # Обработка исключения StopIteration
        while True:
            yield "Пустой список! Введите данные!"
    # Если на вход поступил не пустой список
    else:
        # Вывод назначения транзакций
        for y in list(x["description"] for x in transactions):
            yield y
        # Обработка исключения StopIteration
        while True:
            yield "Транзакции закончились!"


descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


def card_number_generator(start, stop):
    """Генерирует номера карт, принимает на вход начальное и конечное значения, выдает номер карты
    в формате ХХХХ ХХХХ ХХХХ ХХХХ"""
    # Создаем пустой номер
    new_str = "0000000000000000"
    # Если значения находятся в нужном диапазоне
    if 1 <= start <= 9999999999999999 and 1 <= stop <= 9999999999999999:
        for i in range(start, stop + 1):
            # Через range добавляем к пустому номеру цифры из заданного диапазона и подгоняем под размер номера 16 цифр
            number_str = (new_str + str(i))[-16:]
            # Выводим номер с разбивкой по 4 цифры
            yield " ".join([(number_str[i: i + 4]) for i in range(0, len(number_str), 4)])
    # Если значения выходят за нужный диапазон
    else:
        yield "Номер карты может быть в диапазоне от 1 до 9999999999999999!"


for card_number in card_number_generator(1, 5):
    print(card_number)
