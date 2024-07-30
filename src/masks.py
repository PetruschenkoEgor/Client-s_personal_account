import logging
from typing import Union


logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: Union[int, str]) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    # Переводим номер карты в строковое значение, чтобы было удобнее работать
    number_card_str = str(number_card)

    # Проверяем корректность введенного номера карты
    if len(number_card_str) != 16 or not number_card_str.isdigit():
        logger.error("Введен некорректный номер карты")
        result = "Некорректный номер карты!"
    else:
        logger.info("Создание маски номера карты")
        # Делаем маску номера, заменяем часть строки подстрокой
        card_mask = number_card_str.replace(number_card_str[6:12], "******")

        # Разбиваем номер карты по 4 символа
        n = 4
        result = " ".join([(card_mask[i: i + n]) for i in range(0, len(card_mask), n)])

    return result


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    # Переводим номер счета в строковое значение, чтобы было удобнее работать
    account_number_str = str(account_number)

    # Проверяем корректность введенного номера счета
    if len(account_number_str) != 20 or not account_number_str.isdigit():
        logger.error("Введен некорректный номер счета")
        result = "Некорректный номер счета!"
    else:
        logger.info("Создание маски номера счета")
        # Делаем маску счета, заменяем часть строки подстрокой
        account_mask_slice = account_number_str[-5:]
        result = account_mask_slice.replace(account_mask_slice[0:1], "**")

    return result


if __name__ == "__main__":
    print(get_mask_account(73654108430135874305))
