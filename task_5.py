number = int(input("Введите число: "))
if number % 7 == 0 :
    print("Магическое число!")
else :
    digit_sum = 0
    n = number
    while n > 0:
        digit_sum += n % 10
        n = n // 10
    print(digit_sum)