def cache(func):
    cached_results = {}

    def wrapper(*args):
        if args in cached_results:
            print(f"Из кэша: {func.__name__}{args} = {cached_results[args]}")
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        print(f"Вычислено: {func.__name__}{args} = {result}")
        return result

    return wrapper
@cache
def slow_function(x):
    print("Выполняется медленная операция...")
    return x * x

# Первый вызов — вычисляется
slow_function(4)

# Второй вызов — результат берётся из кэша
slow_function(4)

# Новый аргумент — снова вычисляется
slow_function(5)
