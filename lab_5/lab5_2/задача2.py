def find_unique(elements):
    if not elements:
        return []

    unique_elements = []

    for element in elements:
        if elements.count(element) == 1:
            unique_elements.append(element)

    return unique_elements


import pytest


def test_basic():
    """Базовый тест"""
    assert find_unique([1, 2, 2, 3]) == [1, 3]


def test_empty():
    """Тест пустого списка"""
    assert find_unique([]) == []


def test_all_unique():
    """Тест когда все элементы уникальны"""
    assert find_unique([1, 2, 3]) == [1, 2, 3]


def test_all_duplicates():
    """Тест когда все элементы дублируются"""
    assert find_unique([1, 1, 2, 2]) == []


def test_strings():
    """Тест со строками"""
    assert find_unique(['a', 'b', 'a']) == ['b']


def test_single_element():
    """Тест с одним элементом"""
    assert find_unique([5]) == [5]


if __name__ == "__main__":
    # Простые примеры
    print(find_unique([1, 2, 2, 3, 4, 4, 5]))  # [1, 3, 5]
    print(find_unique(['a', 'b', 'a', 'c']))  # ['b', 'c']
    print(find_unique([1, 1, 2, 2]))  # []