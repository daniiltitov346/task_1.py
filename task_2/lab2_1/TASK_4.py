print("Введите первый набор чисел через пробел:")
numbers1 = list(map(int, input().split()))

print("Введите второй набор чисел через пробел:")
numbers2 = list(map(int, input().split()))

common_numbers = []
for num in numbers1:
    if num in numbers2 and num not in common_numbers:
        common_numbers.append(num)

print("\n1. Числа в обоих наборах:", common_numbers)

only_in_first = []
for num in numbers1:
    if num not in numbers2 and num not in only_in_first:
        only_in_first.append(num)

only_in_second = []
for num in numbers2:
    if num not in numbers1 and num not in only_in_second:
        only_in_second.append(num)

print("2. Числа только в первом наборе:", only_in_first)
print("   Числа только во втором наборе:", only_in_second)

all_except_common = []
for num in numbers1 + numbers2:
    if num not in common_numbers and num not in all_except_common:
        all_except_common.append(num)

print("3. Все числа кроме общих:", all_except_common)