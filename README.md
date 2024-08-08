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

## Возможности приложения:
1. Создание маски номера карты
2. Создание маски номера счета
3. Автоматическое определение номер карты или номер счета и применение соответствующей маски номера
4. Преобразование даты в стандартный формат ДД.ММ.ГГГГ
5. Фильтрация по нужному ключу
6. Сортировка по дате(по убыванию и по возрастанию)
7. Поочередноя выдача транзакций с нужной валютой
8. Выдача описания каждой операции по очереди из списка
9. Генерация номеров банковских карт в заданном диапазоне
10. Считывание json-файлов с транзакциями
11. Считывание csv-файлов с транзакциями и приведение их к необходимому виду
12. Считывание Excel-файлов с транзакциями и приведение их к необходимому виду
13. Получение актуального курса валют по API
14. Логирование действий и ошибок в модулях masks и utils
15. Поиск в транзакциях по заданному слову
16. Подсчет количества операций по категориям

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
4. В модуле generators тестируются три функции:
   - В функции filter_by_currency тестируется на корректную фильтрацию транзакций в заданной валюте, если данная валюта отсутствует и если на вход подается пустой список.
   - В функции transaction_descriptions тестируется корректное возвращение описания для каждой транзакции, так же не вызывается исключение StopIteration, когда транзакции закончатся, и функция корректно работает при подаче на вход пустого словаря.
   - В генераторе card_number_generator тестируется правильная выдача номеров карт в заданном диапазоне, правильное форматирование номеров карт и корректная обработка крайних значений номеров.
5. В модуле decorators тестируется декоратор:
   - В декораторе log тестируется корректная работа функции.
6. В модуле external_api тестируется функция:
   - В функции get_amount_in_rub тестируется возвращаемая сумма транзакции
7. В модуле open_csv_and_excel тестируется функция:
   - В функции get_transactions_from_csv тестируется правильное открытие файла и с нужными аргументами

## Логирование:
Производится логирование для модулей:
- masks
- utils

## Главная функция main:
- В главной функции main реализовано взаимодействие с пользователем.

## Документация:
Дополнительную информацию о структуре проекта можно найти в [документации](README.md).

## Лицензия:
Проект распространяется под лицензией SkyPro.
