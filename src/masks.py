def get_mask_card_number(card_number: str) -> str | None:
    """Функция маскировки номера карты"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return None


def get_mask_account(account: str) -> str | None:
    """Функция маскировки номера счета"""
    if account.isdigit() and len(account) == 20:
        return f"**{account[-4::]}"
    else:
        return None


# Проверка выполнения кода
# mask_card_number = print(get_mask_card_number(str(1234567812345678)))
# mask_account = print(get_mask_account(str(12345678901234567890)))
