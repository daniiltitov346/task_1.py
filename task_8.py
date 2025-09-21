text = input("Введите строку: ")

# Удаляем пробелы и приводим к нижнему регистру для проверки
reversed_text = text.replace(" ", "").lower()

# Проверяем, равна ли строка своей перевернутой версии
if reversed_text == reversed_text[::-1]:
    print("Это палиндром!")
else:
    print("Это не палиндром")