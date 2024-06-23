import masks  # type: ignore


def mask_account_card(account_card: str) -> str | None:
    """Функция маскировки номера карты или номера счета"""
    numeral = account_card[-20:]
    if numeral.isdigit():
        account = str(numeral)
        return f"{account_card[0:-20]} {masks.get_mask_account(account)}"
    else:
        card_number = str(account_card[-16:])
        return f"{account_card[0:-16]} {masks.get_mask_card_number(card_number)}"


account_card_1 = "Maestro1234567812345678"
account_card_2 = "Счет12345678901234567890"


result_3 = print(mask_account_card(account_card_1))
result_4 = print(mask_account_card(account_card_2))


def get_data(data: str) -> str | None:
    """Функция преобразования даты"""
    return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"


data = "2018-07-11T02:26:18.671407"
result_5 = print(get_data(data))
