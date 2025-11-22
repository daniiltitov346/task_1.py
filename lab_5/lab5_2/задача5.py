def combine_dicts(dict1, dict2):

    result = dict1.copy()  # Создаем копию первого словаря

    for key, value in dict2.items():
        result[key] = value

    return result


import pytest


def test_basic_combine():
    """Тест базового объединения"""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert combine_dicts(dict1, dict2) == expected


def test_overlapping_keys():
    """Тест с пересекающимися ключами"""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    expected = {'a': 1, 'b': 3, 'c': 4}
    assert combine_dicts(dict1, dict2) == expected


def test_empty_dicts():
    """Тест с пустыми словарями"""
    assert combine_dicts({}, {}) == {}
    assert combine_dicts({'a': 1}, {}) == {'a': 1}
    assert combine_dicts({}, {'b': 2}) == {'b': 2}


def test_same_dicts():
    """Тест с одинаковыми словарями"""
    dict1 = {'a': 1, 'b': 2}
    expected = {'a': 1, 'b': 2}
    assert combine_dicts(dict1, dict1) == expected


def test_different_value_types():
    """Тест с разными типами значений"""
    dict1 = {'a': 1, 'b': 'hello'}
    dict2 = {'c': [1, 2, 3], 'd': {'x': 10}}
    expected = {'a': 1, 'b': 'hello', 'c': [1, 2, 3], 'd': {'x': 10}}
    assert combine_dicts(dict1, dict2) == expected


def test_none_values():
    """Тест с None значениями"""
    dict1 = {'a': None, 'b': 2}
    dict2 = {'b': None, 'c': 3}
    expected = {'a': None, 'b': None, 'c': 3}
    assert combine_dicts(dict1, dict2) == expected


def test_original_unchanged():
    """Тест что оригинальные словари не изменяются"""
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3}
    original_dict1 = dict1.copy()
    original_dict2 = dict2.copy()

    combine_dicts(dict1, dict2)

    assert dict1 == original_dict1
    assert dict2 == original_dict2


if __name__ == "__main__":
    # Примеры использования
    test_cases = [
        ({'a': 1, 'b': 2}, {'c': 3, 'd': 4}),
        ({'a': 1, 'b': 2}, {'b': 3, 'c': 4}),
        ({}, {'x': 10}),
        ({'name': 'John'}, {'age': 25})
    ]

    print("Объединение словарей:")
    for dict1, dict2 in test_cases:
        result = combine_dicts(dict1, dict2)
        print(f"{dict1} + {dict2} = {result}")