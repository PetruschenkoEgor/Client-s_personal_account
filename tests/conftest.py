import pytest

# @pytest.fixture
# def state_enter_value_1():
# """ Для test_filter_by_state """
# return [
# {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
# {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
# {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
# {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]


# @pytest.fixture
# def state_expected_result_1():
# """ Для test_filter_by_state """
# return [
# {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
# {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
# ]


# @pytest.fixture
# def state_enter_value_2():
# """ Для test_filter_by_state """
# return [
# {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
# {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]


# @pytest.fixture
# def state_expected_result_2():
# """ Для test_filter_by_state """
# return "Отсутствует нужное значение!"


@pytest.fixture
def sort_by_date_reverse():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sort_by_date_incorrect():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "lkjj-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-04T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-08-03T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
    ]
