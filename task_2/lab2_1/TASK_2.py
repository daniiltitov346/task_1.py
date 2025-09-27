numbers_input = input("Введите числа через пробел: ")

numbers = numbers_input.split()
num_list = []

for num in numbers:
    if '.' in num:
        num_list.append(float(num))
    else:
        num_list.append(int(num))

unique = []  # для чисел, которые встречаются один раз
repeating = []  # для чисел, которые повторяются
even = []  # для четных чисел
odd = []  # для нечетных чисел
negative = []  # для отрицательных чисел
float_nums = []  # для чисел с плавающей точкой
multiple_5 = []  # для чисел, которые делятся на 5

for num in num_list:

    if num_list.count(num) == 1:
        unique.append(num)
    else:
        if num not in repeating:
            repeating.append(num)

    if type(num) == int:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    if num < 0:
        negative.append(num)

    if type(num) == float:
        float_nums.append(num)

    if num % 5 == 0:
        multiple_5.append(num)


print("\n1. Уникальные числа (встречаются один раз):")
print("   ", unique)

print("\n2. Повторяющиеся числа (встречаются больше одного раза):")
print("   ", repeating)

print("\n3. Четные числа (делятся на 2 без остатка):")
print("   ", even)

print("\n4. Нечетные числа (не делятся на 2 без остатка):")
print("   ", odd)

print("\n5. Отрицательные числа (меньше нуля):")
print("   ", negative)

print("\n6. Числа с плавающей точкой:")
print("   ", float_nums)

print("\n7. Сумма чисел, кратных 5 (делятся на 5):")
print("   ", sum(multiple_5))

print("\n8. Самое большое число в списке:")
print("   ", max(num_list))

print("\n9. Самое маленькое число в списке:")
print("   ", min(num_list))