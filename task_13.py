import random

number = random.randint(1, 100)
tries = 0

print("Угадай число от 1 до 100")

while True:
    guess = int(input("Введи число: "))
    tries += 1

    if guess < number:
        print("Больше")
    elif guess > number:
        print("Меньше")
    else:
        print("Победа! Число", number, "угадано за", tries, "попыток")
        break