#проверяет наличие цифр, если есть заменить на дефис, вывести каждый третий элемент
#text = input("enter text: ")
#modif = text.replace("1","-").replace("2","-")
#print(modif)
#thirdmodif = modif[2::3]
#print(thirdmodif)

# s=input("enter s")
# if len(s)%5==0:
#     print(s[::-5])
# else:
#     print(s.replace("a","1"))


# s=input("enter")
# if s.isdigit() :
#   print(s[2::3])
# elif s.isalpha():
#   print(s.replace("a", " "))
# else:
#   position = s.find("a")
#   print(f"jfjgkgkkg{position + 1}jffkkg")


# text = input("Введите строку: ")
#
# if text.isdigit() and text.isalpha():
#     # Выводим первый и последний символ в верхнем регистре
#     first_char = text[0].upper()
#     last_char = text[-1].upper()
#     print(f"Первый: {first_char}, Последний: {last_char}")
# else:
#     print("Строка не содержит и цифры и буквы")

# s=input ("enter")
# if len(s)%3==0:
#     print(s[2::3])
# elif s.isdigit():
#     number=int(s)
#     print(number%11)
# elif s.isalpha():
#    print(s[0])
#    print(s[-1])


s=input()
if len(s)%3==0:
    print(s[0])
    print(s[-1])
elif s.isalpha():
    print(s.find("a")+1)
elif s.isdigit():
    print(s.find("1"))
else:
    print(s[::-1])
