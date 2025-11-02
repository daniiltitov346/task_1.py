def flatten_list(lst):
    """Делает список плоским с помощью рекурсии"""
    i = 0
    while i < len(lst):
        if type(lst[i]) is list:
            flatten_list(lst[i])
            lst[i:i+1] = lst[i] #убираем вложенные функции
        else:
            i += 1

print("Исходный список:")
list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
print(list_a)

flatten_list(list_a)

print("\nПосле flatten_list:")
print(list_a)