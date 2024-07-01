import masks


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
    if "Счет" in number_card_or_account:
        result = "Счет" + " " + masks.get_mask_account(int("".join(number_lst)))

    # Используется эта маска, если принимаемый аргумент не счет
    else:
        result = "".join(letter_lst) + " " + masks.get_mask_card_number(int("".join(number_lst)))

    return result


print(mask_account_card("Счет 35383033474447895560"))


def get_data(data_time: str) -> str:
    """Функция возвращает дату"""
    # Добавляем нужную нам дату в список с помощью срезов
    date = []
    date.append(data_time[8:10])
    date.append(data_time[5:7])
    date.append(data_time[:4])

    # Переделываем список с датов в нужный нам формат
    data = ".".join(date)

    return data


print(get_data("2018-07-11T02:26:18.671407"))
