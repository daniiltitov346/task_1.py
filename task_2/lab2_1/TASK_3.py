numbers = list(map(int, input("Введите числа через пробел: ").split()))
numbers.sort()

if len(numbers) < 2:
    print("Недостаточно чисел")
else:
    print("Второе по величине число:", numbers[-2])