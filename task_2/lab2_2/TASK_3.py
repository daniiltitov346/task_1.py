import datetime


def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Записываем все в одну строку
            line = f"{datetime.datetime.now()} - {func.__name__} - {args} - {kwargs}\n"

            with open(filename, 'a') as f:
                f.write(line)

            return func(*args, **kwargs)

        return wrapper

    return decorator


# Тест
@log_calls("log.txt")
def example(x):
    return x * 2


result1 = example(5)
print("example(5) =", result1)

result2 = example(10)
print("example(10) =", result2)