from unittest.mock import patch
from src.views import currency_rate


@patch("requests.get")
def test_currency_rate(mock_get):
    mock_get.return_value.json.return_value = {"result": 85.976}
    assert currency_rate("USD") == 85.97
    # на момент написания кода тест проходит, в другой день нужно будет ввести текущий курс?