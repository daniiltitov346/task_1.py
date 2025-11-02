def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            # Проверяем, что количество аргументов совпадает
            if len(args) != len(types):
                raise TypeError(f"Ожидается {len(types)} аргументов, получено {len(args)}")

            # Проверяем типы каждого аргумента
            for i, (arg, expected_type) in enumerate(zip(args, types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Аргумент {i} должен быть {expected_type.__name__}, "
                                    f"получен {type(arg).__name__}")

            # Вызываем оригинальную функцию
            return func(*args)

        return wrapper

    return decorator

# Пример 1: Сложение двух целых чисел
@type_check(int, int)
def add(a, b):
    return a + b

print(add(2, 3))     # 5
# add(2, "3")       # TypeError: Аргумент 1 должен быть int, получен str

# Пример 2: Приветствие
@type_check(str)
def greet(name):
    return f"Привет, {name}!"

print(greet("Анна"))  # Привет, Анна!
# greet(123)         # TypeError: Аргумент 0 должен быть str, получен int

# Пример 3: Расчет площади
@type_check(float, float)
def rectangle_area(width, height):
    return width * height

print(rectangle_area(5.5, 3.2))  # 17.6

