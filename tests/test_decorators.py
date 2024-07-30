from src.decorators import log, my_function


def test_log_ok(capsys):
    """ Тест, если функция работает без ошибок """
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_log_division_by_zero(capsys):
    """ Тест, если в функции выпадает исключение ZeroDivisionError """
    @log()
    def test_func_error(x, y):
        return x / y

    result = test_func_error(1, 0)
    captured = capsys.readouterr()
    assert "test_func_error error: division by zero. Inputs: {'x': 1, 'y': 0}\n" in captured.out
