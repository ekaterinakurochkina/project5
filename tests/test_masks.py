import pytest

from src.masks import get_mask_account, get_mask_card_number

# Тестирование раздела masks с использованием фикстуры


@pytest.fixture
def account():
    return "01234567890123456789"


@pytest.fixture
def card_number():
    return "1234567812345678"


def test_get_mask_account(account):
    assert get_mask_account(account) == "**6789"


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "1234 56** **** 5678"
