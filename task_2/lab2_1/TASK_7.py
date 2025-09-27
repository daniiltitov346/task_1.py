s = input("Введите строку: ")

if not s:
    print("")
else:
    result = ""
    current_char = s[0]
    count = 1

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            result += current_char + str(count)
            current_char = s[i]
            count = 1

    result += current_char + str(count)

    print("Сжатая строка:", result)