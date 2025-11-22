def are_anagrams(str1, str2):
    # Приводим к нижнему регистру и убираем пробелы
    str1_clean = str1.lower().replace(" ", "")
    str2_clean = str2.lower().replace(" ", "")

    # Сортируем буквы и сравниваем
    return sorted(str1_clean) == sorted(str2_clean)


import pytest


def test_anagrams_basic():
    """Тест базовых анаграмм"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True
    assert are_anagrams("cat", "act") == True


def test_not_anagrams():
    """Тест не анаграмм"""
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False
    assert are_anagrams("test", "best") == False


def test_different_length():
    """Тест строк разной длины"""
    assert are_anagrams("abc", "abcd") == False
    assert are_anagrams("a", "ab") == False


def test_case_insensitive():
    """Тест регистронезависимости"""
    assert are_anagrams("Listen", "Silent") == True
    assert are_anagrams("CAT", "act") == True


def test_with_spaces():
    """Тест с пробелами"""
    assert are_anagrams("school master", "the classroom") == True
    assert are_anagrams("debit card", "bad credit") == True


def test_same_string():
    """Тест одинаковых строк"""
    assert are_anagrams("test", "test") == True
    assert are_anagrams("a", "a") == True


def test_empty_strings():
    """Тест пустых строк"""
    assert are_anagrams("", "") == True
    assert are_anagrams(" ", " ") == True


def test_numbers_in_strings():
    """Тест строк с числами"""
    assert are_anagrams("123", "321") == True
    assert are_anagrams("a1b2", "2b1a") == True


if __name__ == "__main__":
    # Примеры использования
    test_cases = [
        ("listen", "silent"),
        ("hello", "world"),
        ("cat", "act"),
        ("Listen", "Silent"),
        ("school master", "the classroom"),
        ("test", "best")
    ]

    print("Проверка анаграмм:")
    for str1, str2 in test_cases:
        result = are_anagrams(str1, str2)
        print(f"'{str1}' и '{str2}' -> {result}")