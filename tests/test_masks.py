import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "enter_value, expected_result",
    [
        (7000792289606361, "7000 79** **** 6361"),
        ("7000792289606361", "7000 79** **** 6361"),
        (70007922896063611, "Некорректный номер карты!"),
        (700079228960636, "Некорректный номер карты!"),
        ("", "Некорректный номер карты!"),
        (" ", "Некорректный номер карты!"),
        ("jhgfdsaeyudhfydt", "Некорректный номер карты!"),
    ],
)
def test_get_mask_card_number_parametrize(enter_value, expected_result):
    """Проверяем работу функции на различных входных форматах номеров карт"""
    assert get_mask_card_number(enter_value) == expected_result


@pytest.mark.parametrize(
    "enter_value, expected_result",
    [
        (73654108430135874305, "**4305"),
        ("73654108430135874305", "**4305"),
        (736541084301358743055, "Некорректный номер счета!"),
        (7365410843013587430, "Некорректный номер счета!"),
        ("", "Некорректный номер счета!"),
        (" ", "Некорректный номер счета!"),
        ("jhgfdsaeyudhfydtdfgh", "Некорректный номер счета!"),
    ],
)
def test_get_mask_account_parametrize(enter_value, expected_result):
    """Проверяем работу функции на различных входных форматах номеров счета"""
    assert get_mask_account(enter_value) == expected_result
