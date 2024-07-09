from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_card_or_account: str) -> str:
    """Функция принимает номер карты/счета и возвращает маску номера"""
    # Получаем из входной строки номер карты или счета(int)
    number_lst = []
    letter_lst = []
    for i in number_card_or_account:
        if i.isdigit():
            number_lst.append(i)
        else:
            letter_lst.append(i)

    # Используется эта маска, если принимаемый аргумент - счет
    if len(number_lst) == 20:
        result = "".join(letter_lst) + get_mask_account(int("".join(number_lst)))

    # Используется эта маска, если принимаемый аргумент не счет
    elif len(number_lst) == 16:
        result = "".join(letter_lst) + get_mask_card_number(int("".join(number_lst)))

    else:
        result = "Введены некорректные данные!"

    return result


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))


def get_date(data_time: str) -> str:
    """Функция возвращает дату"""
    # Добавляем нужную нам дату в список с помощью срезов
    date = []
    date.append(data_time[8:10])
    date.append(data_time[5:7])
    date.append(data_time[:4])

    # Проверяем нужный формат у даты
    if ("".join(date).isdigit() and 1 <= int(data_time[8:10]) <= 31 and 1 <= int(data_time[5:7]) <= 12
            and 1980 <= int(data_time[:4]) <= 2024):
        # Переделываем список с датой в нужный нам формат
        result = ".".join(date)
    else:
        result = "Некорректная дата!"

    return result


if __name__ == "__main__":
    print(get_date("2025-03-11T02:26:18.671407"))
