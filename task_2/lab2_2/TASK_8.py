import time
from functools import wraps


def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Засекаем начальное время
        result = func(*args, **kwargs)  # Выполняем функцию
        end_time = time.time()  # Засекаем конечное время

        # Вычисляем время выполнения в миллисекундах
        execution_time = (end_time - start_time) * 1000
        print(f"Функция {func.__name__} выполнилась за {execution_time:.2f} мс")

        return result

    return wrapper

@timing
def calculate_sum(n):
    """Вычисляет сумму чисел от 1 до n"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Вызов функции
result = calculate_sum(1000000)