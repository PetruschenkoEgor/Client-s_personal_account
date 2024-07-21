from functools import wraps
from inspect import getcallargs


def log(filename=""):
    """Логгирует данные о функции"""

    def wrapper(function):
        @wraps(function)
        def inner(*args, **kwargs):
            try:
                function(*args, **kwargs)
                # Выдает результат в консоль, если имя файла не задано
                if filename == "":
                    print(f"{function.__name__} ok")
                # Записывает результат в файл, если имя файла задано
                else:
                    with open(filename, "w") as f:
                        f.write(f"{function.__name__} ok")

            except ValueError as e:
                if filename == "":
                    print(f"{function.__name__} error: {e}. Inputs: {getcallargs(function, *args, **kwargs)}")
                else:
                    with open(filename, "w") as f:
                        f.write(f"{function.__name__} error: {e}. Inputs: {getcallargs(function, *args, **kwargs)}")

            except ZeroDivisionError as e:
                if filename == "":
                    print(f"{function.__name__} error: {e}. Inputs: {getcallargs(function, *args, **kwargs)}")
                else:
                    with open(filename, "w") as f:
                        f.write(f"{function.__name__} error: {e}. Inputs: {getcallargs(function, *args, **kwargs)}")

            except Exception as e:
                if filename == "":
                    print(f"{function.__name__} error: {e}. Inputs: {getcallargs(function, *args, **kwargs)}")
                else:
                    with open(filename, "w") as f:
                        f.write(f"{function.__name__} error: {e}. Inputs: {getcallargs(function, *args, **kwargs)}")

        return inner

    return wrapper


@log()
def my_function(x, y):
    return x + y


my_function(1, 2)


@log()
def my_function_division(x, y):
    return x / y


my_function_division(1, 0)
