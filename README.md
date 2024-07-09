# Проект Client's personal account

## Описание:
Проект Client's personal account - это серверная часть виджета банковских операций. Виджет отображает операции клиента, создает маску номера карты и счета, показывает дату операции, сортирует операции по дате по возрастанию и убыванию.

## Установка:
1. Клонируйте репозиторий:
```
git clone https://github.com/username/Client's personal account.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```

## Использование:
1. Войдите в свой аккаунт или создайте новый и войдите в него.
2. Введите свой номер банковской карты или счета

## Тестирование модулей:
В проекте добавлено тестирование модулей:
1. В модуле masks тестируются две функции:
   - В функции get_mask_card_number тестируется на правильность маскировки номера карты различными входными форматами 
номеров карт, в том числе некорректными и пустыми значениями.
   - В функции get_mask_account тестируется на правильность маскировки номера счета различными входными форматами 
номеров счета, в том числе некорректными и пустыми значениями.
2. В модуле widget тестируются две функции:
   - В функции mask_account_card тестируется на корректное распознавание номера счета или карты и правильное применение 
маскировки при различных входных форматах номеров карт и счетов, в том числе некорректных и пустых значениях.
   - В функции get_data тестируется на правильность преобразования даты на различных входных форматах даты, в том числе 
некорректных данных и пустых строках.
3. В модуле processing тестируются две функции:
   - В функции filter_by_state тестируется правильная фильтрация словарей по ключу state с различными значениями, 
в том числе если этого ключа нет.
   - В функции sort_by_date тестируется сортировка словарей по датам в порядке возрастания и убывания, в том числе с 
одинаковыми и некорректными датами.

## Документация:
Дополнительную информацию о структуре проекта можно найти в [документации](README.md).

## Лицензия:
Проект распространяется под лицензией SkyPro.