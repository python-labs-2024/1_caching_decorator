"""Кэширующий декоратор.

Пара полезных ссылок:
1. Зачем нужен wraps?
https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
2. Декораторы с параметрами
https://stackoverflow.com/questions/5929107/decorators-with-parameters
"""

__all__ = ["cache"]

from collections import deque
from functools import wraps


def cache(depth=10, policy="LRU"):
    def decorator(func):
        if policy not in ["LRU", "FIFO", "LIFO", "MRU"]:
            raise ValueError("Wrong substitution policy")

        cache = dict()
        access = deque()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (*args, *kwargs.items())

            try:
                if key in cache:
                    if policy in ["LRU", "MRU"]:
                        access.remove(key)
                        access.append(key)
                    return cache[key]
            except:
                raise TypeError("The type of this argument is not hashable")

            if depth is not None and depth > 0:
                if len(cache) + 1 > depth:
                    if policy in ["LRU", "FIFO"]:
                        oldest_key = access.popleft()
                    elif policy in ["LIFO", "MRU"]:
                        oldest_key = access.pop()
                    del cache[oldest_key]
            elif depth is not None and depth < 1:
                raise ValueError("Depth cannot be less than 1")

            result = func(*args, **kwargs)
            cache[key] = result
            access.append(key)

            return result

        return wrapper

    return decorator
