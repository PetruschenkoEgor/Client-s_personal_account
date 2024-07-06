def get_mask_card_number(number_card: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    # Переводим номер карты в строковое значение, чтобы было удобнее работать
    number_card_str = str(number_card)
    # Делаем маску номера, заменяем часть строки подстрокой
    card_mask = number_card_str.replace(number_card_str[6:12], "******")

    # Разбиваем номер карты по 4 символа
    n = 4
    number_card_mask = " ".join([(card_mask[i: i + n]) for i in range(0, len(card_mask), n)])

    return number_card_mask


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    # Переводим номер счета в строковое значение, чтобы было удобнее работать
    account_number_str = str(account_number)

    # Делаем маску счета, заменяем часть строки подстрокой
    account_mask_slice = account_number_str[-5:]
    account_mask = account_mask_slice.replace(account_mask_slice[0:1], "**")

    return account_mask


if __name__ == "__main__":
    print(get_mask_account(73654108430135874305))
