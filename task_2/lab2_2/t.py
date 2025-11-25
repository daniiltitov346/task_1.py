#сгенерирровать словарь на 100 жлементов с помощью генератора из чисел от 1 до 1000000, прописать через пользовательский ввод возможность вывести все элементы кратные 5, найти сумму каждого 3 элемента,вывод всех простых чисел в новый список
import random
dictionary =[
     random.randint(1, 1000000)

    for _ in range(100)]
print(dictionary)

while True:
    print("/nВыберите"
          "1 - вывод всех элементов кратных 5"
          "2 - найти сумму каждого 3го элемента"
          "3 - вывод всех простых чисел")
    choice = input("введите ваш выбор")
    if choice == "1":
        for number in dictionary:
            if number % 5 == 0:
                with open("numbers.txt", "a", encoding="utf-8") as f:
                    f.write(f"СПИСОК ЧИСЕЛ КРАТНЫХ 5 {number }\n" )
                    print(number)


    if choice == "2":
         list = []
         sum = 0
         for number in dictionary:
             if number % 2 == 0:
                 sum += number
         print(sum)

    with open("numbers.txt", "a", encoding= "utf-8") as f:
         f.write(f"СУММА ЧЕТНЫХ ЧИСЕЛ::{sum} \n")

    if choice == "3":
        prostye = []
        for number in dictionary:
            if number < 2:
                continue
            if number == 2:
                prostye.append(number)
                continue
            if number % 2 == 0:
                continue  # Четные числа больше 2 не простые

            # Проверяем делители от 3 до корня из числа
            is_prosty = True
            for i in range(3, int(number ** 0.5) + 1, 2):
                if number % i == 0:
                    is_prosty = False
                    break

            if is_prosty:
                prostye.append(number)

        print(prostye)
        with open("numbers.txt", "a", encoding="utf-8") as f:
            f.write(f"СПИСОК ПРОСТЫХ ЧИСЕЛ::{prostye}\n")

