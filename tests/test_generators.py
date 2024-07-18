import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_transactions(transactions_fixture):
    """Тест на корректную фильтрацию транзакций по заданной валюте(фикстура)"""
    generator = filter_by_currency(transactions_fixture, "USD")
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_not_currency(transactions_fixture):
    """Тест на корректную фильтрацию транзакций, если валюта отстутствует"""
    generator = filter_by_currency(transactions_fixture, "US")
    assert next(generator) == "Транзакции с указанной валютой отсутствуют!"


def test_filter_by_currency_not_list():
    """Тест на корректную фильтрацию транзакций, если подается пустой список"""
    generator = filter_by_currency([], "USD")
    assert next(generator) == "Пустой список! Введите данные!"


def test_transaction_descriptions(transactions_fixture):
    """Тест на то, что функция возвращает корректные описания для каждой транзакции и не вызывает исключения,
    когда транзакции закончатся"""
    generator = transaction_descriptions(transactions_fixture)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Транзакции закончились!"


def test_transaction_descriptions_not_list():
    """Тест, если на вход подается пустой список"""
    generator = transaction_descriptions([])
    assert next(generator) == "Пустой список! Введите данные!"


@pytest.mark.parametrize(
    "start, stop, expected_result",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (9898989898989898, 9898989898989899, ["9898 9898 9898 9898", "9898 9898 9898 9899"]),
        (0, 1, ["Номер карты может быть в диапазоне от 1 до 9999999999999999!"]),
        (9999999999999999, 10000000000000000, ["Номер карты может быть в диапазоне от 1 до 9999999999999999!"]),
    ],
)
def test_card_number_generator(start, stop, expected_result):
    """Тест на правильную выдачу номеров карт в заданном диапазоне, на правильное форматирование номеров карт
    и корректную обработку крайних значений номеров"""
    generator = list(card_number_generator(start, stop))
    assert generator == expected_result
