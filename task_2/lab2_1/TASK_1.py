text = input("Введите текст: ")

words = text.lower().split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nСколько раз встречается каждое слово:")
for word in word_count:
    count = word_count[word]
    print(word, "-", count, "раз")

unique_words = 0
for word in word_count:
    if word_count[word] == 1:
        unique_words += 1

print("\nКоличество уникальных слов (встречаются 1 раз):", unique_words)