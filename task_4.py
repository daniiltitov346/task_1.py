money = int(input("Введите сумму в рублях: "))

# Купюры
k100 = money // 100
money = money % 100

k50 = money // 50
money = money % 50

k10 = money // 10
money = money % 10

# Монеты
k5 = money // 5
money = money % 5

k2 = money // 2
k1 = money % 2

print("Купюр 100 руб.:", k100)
print("Купюр 50 руб.:", k50)
print("Купюр 10 руб.:", k10)
print("Монет 5 руб.:", k5)
print("Монет 2 руб.:", k2)
print("Монет 1 руб.:", k1)