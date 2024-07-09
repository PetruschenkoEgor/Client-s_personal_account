import pytest

from src.processing import filter_by_state, sort_by_date

# from tests.conftest import state_enter_value_1, state_expected_result_1, state_enter_value_2, state_expected_result_2


@pytest.mark.parametrize(
    "enter_value, expected_result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "Отсутствует нужное значение!",
        ),
    ],
)
#@pytest.mark.parametrize(
    #"enter_value, expected_result",
    #[(state_enter_value_1, state_expected_result_1), (state_enter_value_2, state_expected_result_2)],
#)
def test_filter_by_state(enter_value, expected_result):
    """Тест фильтрации по ключу state и если он отсутствует"""
    assert filter_by_state(enter_value) == expected_result


@pytest.mark.parametrize(
    "enter_value, state, expected_result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        )
    ],
)
def test_filter_by_state_key(enter_value, state, expected_result):
    """Тест фильтрации с другим ключом state"""
    assert filter_by_state(enter_value, state) == expected_result


@pytest.mark.parametrize(
    "enter_value, expected_result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
            ],
            [
                {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
            ],
        ),
    ],
)
def test_sort_by_date(enter_value, expected_result):
    """Тест сортировки по убыванию и с одинаковыми датами"""
    assert sort_by_date(enter_value) == expected_result


def test_sort_by_date_reverse(sort_by_date_reverse):
    """Тест сортировки по возрастанию"""
    assert sort_by_date(sort_by_date_reverse, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_incorrect(sort_by_date_incorrect):
    """Тесст сортировки с неправильной датой"""
    assert sort_by_date(sort_by_date_incorrect) == "Некорректная дата!"
