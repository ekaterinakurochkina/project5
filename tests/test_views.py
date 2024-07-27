from unittest.mock import patch
from src.views import currency_rate


@patch("requests.get")
def test_currency_rate(mock_get):
    mock_get.return_value.json.return_value = {"result": 73.15}
    assert currency_rate("USD") == 73.15


# курс валют на 2021-07-01
