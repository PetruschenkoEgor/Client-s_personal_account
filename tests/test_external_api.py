from unittest.mock import patch

from src.external_api import get_amount_in_rub


@patch("src.external_api.requests.get")
def test_get_amount_in_rub(mock_get):
    """Тест, транзакции с валютой USD"""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1722098644, "rate": 85.972867},
        "date": "2024-07-27",
        "result": 706814.749568,
    }
    usd_transaction = [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        }
    ]
    result = get_amount_in_rub(usd_transaction)
    assert result == "Сумма транзакции: 706814.75."
    mock_get.assert_called()
