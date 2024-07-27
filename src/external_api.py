import os
from dotenv import load_dotenv
import json
import requests


def get_amount_in_rub(transaction):
    """ Функция принимает транзакцию и возвращает сумму транзакций в рублях """
    # Загрузка переменных из файла .env
    load_dotenv()

    # Получение значения переменной API_KEY из .env-файла
    api_key = os.getenv("API_KEY")
    currency = transaction[0]["operationAmount"]["currency"]["code"]

    try:
        # Если валюта USD или EUR, необходимо запросить текущий курс валюты
        if currency in ("USD", "EUR"):
            to_currency = "RUB"
            from_currency = currency
            amount = transaction[0]["operationAmount"]["amount"]
            url = f"https://api.apilayer.com/exchangerates_data/convert"
            params = {
                "amount": amount,
                "from": from_currency,
                "to": to_currency
            }
            headers = {
                "apikey": api_key
            }

            # Запрос курса валют по API
            response = requests.get(url, headers=headers, params=params)
            status_code = response.status_code
            return response.json()

            # Проверяем, успешный ли запрос
            if status_code == 200:
                # Получение общей суммы и округление до 2-х цифр после запятой
                response_amount = round(response.json().get('result'), 2)
                return f"Сумма транзакции: {response_amount}."

            # Если запрос неуспешный, выводим статус-код и причину
            else:
                return f"Неверный статус-код: {response.status_code}! {response.reason}!"

        # Если валюта RUB, то выводим сумму транзакции
        else:
            transaction_ = transaction[0]["operationAmount"]["amount"]
            return f"Сумма транзакции: {transaction_}."

    except requests.exceptions.RequestException as e:
        return e


if __name__ == "__main__":
    print(get_amount_in_rub([{
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }]))
