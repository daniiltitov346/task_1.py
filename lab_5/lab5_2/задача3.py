def is_palindrome(word):
    # Преобразуем в строку чтобы работать с числами и словами одинаково
    text = str(word).lower().replace(" ", "")
    return text == text[::-1]


import pytest


def test_palindrome_words():
    """Тест слов-палиндромов"""
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("madam") == True


def test_not_palindrome_words():
    """Тест слов не палиндромов"""
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("python") == False


def test_palindrome_numbers():
    """Тест чисел-палиндромов"""
    assert is_palindrome(121) == True
    assert is_palindrome(12321) == True
    assert is_palindrome(1) == True


def test_not_palindrome_numbers():
    """Тест чисел не палиндромов"""
    assert is_palindrome(123) == False
    assert is_palindrome(1234) == False


def test_case_insensitive():
    """Тест регистронезависимости"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Aba") == True


def test_with_spaces():
    """Тест с пробелами"""
    assert is_palindrome("a man a plan a canal panama") == True


def test_empty_string():
    """Тест пустой строки"""
    assert is_palindrome("") == True


def test_single_character():
    """Тест одного символа"""
    assert is_palindrome("a") == True
    assert is_palindrome("1") == True


if __name__ == "__main__":
    # Примеры использования
    test_words = ["radar", "hello", "level", "python", "Aba", ""]
    test_numbers = [121, 123, 12321, 1]

    print("Проверка слов:")
    for word in test_words:
        result = is_palindrome(word)
        print(f"'{word}' -> {result}")

    print("\nПроверка чисел:")
    for num in test_numbers:
        result = is_palindrome(num)
        print(f"{num} -> {result}")