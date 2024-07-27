from unittest.mock import patch
from unittest.mock import Mock
from src.utils import get_transactions_from_json


@patch('src.utils.get_transactions_from_json')
def test_get_transactions_from_json([], mock_get):
    mock_get = Mock(return_value=[])
    assert get_transactions_from_json([]) == []
    mock_get.assert_called_once_with([])
