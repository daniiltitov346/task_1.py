text = input("Введите строку: ")
result = ""

for char in text:
    if char.lower() not in 'aeiou':
        result += char

print("Результат:", result)