def count_words(sentence):
    """
    Функция для подсчета слов в предложении.

    Args:
        sentence (str): Входная строка с предложением

    Returns:
        int: Количество слов в предложении
    """
    if not sentence or not sentence.strip():
        return 0

    words = [word for word in sentence.split() if word]
    return len(words)


def count_chars_per_word(sentence):
    if not sentence or not sentence.strip():
        return []

    words = [word for word in sentence.split() if word]
    return [len(word) for word in words]


# Тесты для count_words
def test_count_words_basic():
    """Тест обычного предложения"""
    assert count_words("Привет мир") == 2
    assert count_words("Hello world") == 2
    assert count_words("Это тестовое предложение") == 3


def test_count_words_empty():
    """Тест пустой строки"""
    assert count_words("") == 0
    assert count_words("   ") == 0


def test_count_words_multiple_spaces():
    """Тест множественных пробелов"""
    assert count_words("Слово1   Слово2    Слово3") == 3
    assert count_words("  Начальные  и  конечные  пробелы  ") == 4


def test_count_words_single_word():
    """Тест одного слова"""
    assert count_words("Слово") == 1
    assert count_words("  Слово  ") == 1


def test_count_words_punctuation():
    """Тест знаков препинания"""
    assert count_words("Привет, мир!") == 2
    assert count_words("Что? Где? Когда?") == 3


def test_count_words_numbers():
    """Тест чисел и смешанного содержания"""
    assert count_words("123 456 789") == 3
    assert count_words("Цена 100 рублей") == 3
    assert count_words("Python3 лучше чем Python2") == 4


def test_count_words_special_chars():
    """Тест специальных символов"""
    assert count_words("@username #hashtag $price") == 3
    assert count_words("word1 & word2 | word3") == 5


def test_count_words_tabs_newlines():
    """Тест табуляции и переносов строк"""
    assert count_words("Слов1\tСлов2\tСлов3") == 3
    assert count_words("Line1\nLine2\nLine3") == 3
    assert count_words("Смешанные\tпробелы\nи переносы") == 4


# Тесты для count_chars_per_word
def test_count_chars_per_word_basic():
    """Тест основной функциональности"""
    assert count_chars_per_word("привет мир") == [6, 3]
    assert count_chars_per_word("а б в") == [1, 1, 1]


def test_count_chars_per_word_empty():
    """Тест пустых случаев"""
    assert count_chars_per_word("") == []
    assert count_chars_per_word("   ") == []


def test_count_chars_per_word_punctuation():
    """Тест со знаками препинания"""
    assert count_chars_per_word("Привет, мир!") == [7, 4]


# Тесты граничных случаев
def test_edge_cases():
    """Тест граничных случаев"""
    # Очень длинное слово
    long_word = "a" * 100
    assert count_words(long_word) == 1
    assert count_chars_per_word(long_word) == [100]

    # Чередование пробелов и слов
    assert count_words("а  б   в    г") == 4


# Параметризованные тесты
import pytest


@pytest.mark.parametrize("sentence,expected_count", [
    ("", 0),
    (" ", 0),
    ("слово", 1),
    ("два слова", 2),
    ("три разных слова", 3),
    ("  начальные  пробелы  ", 2),
    ("конечные  пробелы  ", 2),
    ("  и  те  и  другие  ", 4),
    ("раз\tдва\nтри", 3),
    ("123 456", 2),
    ("test,with,commas", 1),  # запятые без пробелов - одно слово
])
def test_count_words_parametrized(sentence, expected_count):
    """Параметризованные тесты для count_words"""
    assert count_words(sentence) == expected_count


@pytest.mark.parametrize("sentence,expected_lengths", [
    ("", []),
    ("   ", []),
    ("а", [1]),
    ("а б", [1, 1]),
    ("hello world", [5, 5]),
    ("test  spaces", [4, 6]),
])
def test_count_chars_per_word_parametrized(sentence, expected_lengths):
    """Параметризованные тесты для count_chars_per_word"""
    assert count_chars_per_word(sentence) == expected_lengths