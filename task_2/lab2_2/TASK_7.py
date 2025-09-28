def merge_sorted_list(list1, list2):

    result = []
    i = j = 0

    # Сравниваем элементы из обоих списков и добавляем меньший в результат
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # Добавляем оставшиеся элементы из list1 (если есть)
    while i < len(list1):
        result.append(list1[i])
        i += 1

    # Добавляем оставшиеся элементы из list2 (если есть)
    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result

# Пример 1
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(merge_sorted_list(list1, list2))  # [1, 2, 3, 4, 5, 6, 7, 8]

# Пример 2 - списки разной длины
list3 = [1, 5, 9]
list4 = [2, 3, 6, 7, 10]
print(merge_sorted_list(list3, list4))  # [1, 2, 3, 5, 6, 7, 9, 10]

# Пример 3 - с повторяющимися элементами
list5 = [1, 3, 3, 5]
list6 = [2, 3, 4]
print(merge_sorted_list(list5, list6))  # [1, 2, 3, 3, 3, 4, 5]

# Пример 4 - один пустой список
list7 = []
list8 = [1, 2, 3]
print(merge_sorted_list(list7, list8))  # [1, 2, 3]