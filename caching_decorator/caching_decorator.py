"""Кэширующий декоратор.

Пара полезных ссылок:
1. Зачем нужен wraps?
https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
2. Декораторы с параметрам
https://stackoverflow.com/questions/5929107/decorators-with-parameters
"""

__all__ = ["cache"]

from functools import wraps


def cache(depth=10):
    def decorator(func):
        # cache = ...

        @wraps(func)
        def wrapper(*args, **kwargs):
            # magic happens here...
            pass

        return wrapper

    return decorator
