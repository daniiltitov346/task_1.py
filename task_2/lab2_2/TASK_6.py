def unique_elements(nested_list):
    result = []

    def flatten(lst):
        for item in lst:
            if type(item) == list:
                flatten(item)
            else:
                if item not in result:  # Проверяем уникальность
                    result.append(item)

    flatten(nested_list)
    return result

list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print(unique_elements(list_a))
