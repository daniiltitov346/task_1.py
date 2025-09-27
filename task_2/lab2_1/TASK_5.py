word1 = input("Введите первое слово: ").lower()
word2 = input("Введите второе слово: ").lower()

if sorted(word1) == sorted(word2):
    print(True)
else:
    print(False)