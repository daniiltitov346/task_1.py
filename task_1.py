fio = input("Введите ФИО: ")
space1 = fio.find(" ")
space2 = fio.find(" ", space1 + 1)
surname = fio[:space1]
name_letter = fio[space1 + 1]
patronymic_letter = fio[space2 + 1]

print(surname, name_letter + "." + patronymic_letter + ".")