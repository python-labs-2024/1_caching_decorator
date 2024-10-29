from caching_decorator import cache


def test_caching():
    """Проверяет, что результат кэшируется и функция не выполняется повторно."""

    @cache(depth=3)
    def slow_function(x):
        slow_function.call_count += 1
        return x * x

    # Инициализируем счетчик вызовов
    slow_function.call_count = 0

    result1 = slow_function(2)
    result2 = slow_function(2)

    assert result1 == result2  # Ожидаем одинаковый результат
    assert slow_function.call_count == 1  # Функция должна быть вызвана только один раз
