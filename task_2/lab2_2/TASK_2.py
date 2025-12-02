# task_2.py

def merge_dicts(dict_a, dict_b):
    """Простое рекурсивное слияние двух словарей"""
    for key, value in dict_b.items():
        if key in dict_a and type(dict_a[key]) is dict and type(value) is dict:
            # Если оба значения - словари, сливаем их рекурсивно
            merge_dicts(dict_a[key], value)
        else:
            # Во всех остальных случаях просто заменяем значение
            dict_a[key] = value

# Демонстрация работы
print("=== Простое слияние словарей ===")

# Пример из условия
dict_a = {"a": 1, "b": {"c": 1, "f": 4}}
dict_b = {"d": 1, "b": {"c": 2, "e": 3}}

print("До слияния:")
print(f"dict_a = {dict_a}")
print(f"dict_b = {dict_b}")

merge_dicts(dict_a, dict_b)

print("\nПосле слияния:")
print(f"dict_a = {dict_a}")

# Еще пример
print("\n" + "="*40)
print("Дополнительный пример:")

dict1 = {"x": 10, "y": {"z": 20}}
dict2 = {"y": {"z": 30, "w": 40}, "new": 50}

print("До слияния:")
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")

merge_dicts(dict1, dict2)

print("\nПосле слияния:")
print(f"dict1 = {dict1}")