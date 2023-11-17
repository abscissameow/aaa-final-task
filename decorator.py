from functools import wraps
from random import randint


def min_count(p: int) -> str:
    """
    минутки
    """
    if p % 10 == 1 and p % 100 != 11:
        return 'минутка'
    elif p % 10 in [2, 3, 4] and p % 100 not in [12, 13, 14]:
        return 'минутки'
    else:
        return 'минуток'


def log(message_template: str):
    """
    возвращает функцию декоратор
    """
    def decorator(func):
        """
        декоратор
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            обёрточка
            """
            p = randint(10, 30)
            print(f' {message_template} {p} {min_count(p)} 🕐')
        return wrapper

    return decorator
