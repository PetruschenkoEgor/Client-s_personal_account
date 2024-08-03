from unittest.mock import patch
import os

from src.open_csv_and_excel import get_transactions_from_csv

PATH_TO_FILE_CSV = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")


@patch("src.open_csv_and_excel.csv.DictReader")
@patch("src.open_csv_and_excel.open")
def test_get_transactions_from_csv(mock_open, mock_dict_reader, transactions_csv_excel):
    """ Тест открытия файла с транзакциями CSV """
    mock_dict_reader.return_value = transactions_csv_excel
    assert get_transactions_from_csv(PATH_TO_FILE_CSV)[:2] == [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'}, {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643', 'description': 'Перевод с карты на карту'}]
    mock_open.assert_called_once_with(PATH_TO_FILE_CSV, encoding='utf-8')
