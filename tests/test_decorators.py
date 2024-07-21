from src.decorators import my_function


def test_log_ok(capsys):
    """ Тест, если функция работает без ошибок """
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
