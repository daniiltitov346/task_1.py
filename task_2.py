text = input("Введите строку: ")

text = text.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
text = text.replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')

print(text)
