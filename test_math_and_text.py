import pytest
#Иванов Артём 107б2
from math_and_text import multiply, divide, distance, solve_quadratic, geometric_sum, count_words, contains_substring, to_upper_case

# Фикстура для работы с текстовым файлом
@pytest.fixture
def sample_text():
    with open("sample_text.txt", "r") as file:
        return file.read()

# Класс для тестирования математических функций
class TestMathFunctions:

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 6),
        (-2, 3, -6),
        (0, 5, 0),
        (3, 0, 0)
    ])
    def test_multiply(self, a, b, expected):
        assert multiply(a, b) == expected

    @pytest.mark.parametrize("a, b, expected", [
        (6, 3, 2),
        (-6, 3, -2),
        (1, 1, 1)
    ])
    def test_divide(self, a, b, expected):
        assert divide(a, b) == expected

    @pytest.mark.parametrize("x1, y1, x2, y2, expected", [
        (0, 0, 3, 4, 5),
        (1, 1, 1, 1, 0),
        (-1, -1, 1, 1, 2.828)
    ])
    def test_distance(self, x1, y1, x2, y2, expected):
        assert round(distance(x1, y1, x2, y2), 3) == expected

    @pytest.mark.parametrize("a, b, c, expected", [
        (1, -3, 2, (2, 1)),
        (1, -2, 1, (1.0,)),  # исправлено
        (1, 1, 1, ValueError)
    ])
    def test_solve_quadratic(self, a, b, c, expected):
        if expected == ValueError:
            with pytest.raises(ValueError):
                solve_quadratic(a, b, c)
        else:
            result = solve_quadratic(a, b, c)
            # Если результат — одиночное число, просто сравниваем его с ожидаемым значением.
            if isinstance(result, tuple):
                assert len(result) == len(expected)  # Проверяем совпадение длины кортежа
                assert all(round(r, 3) == round(e, 3) for r, e in zip(result, expected))  # Сравниваем значения с точностью
            else:
                assert round(result, 3) == round(expected[0], 3)  # Сравниваем одиночные числа

    @pytest.mark.parametrize("a, r, n, expected", [
        (1, 2, 5, 31),
        (1, 0.5, 5, 1.9375),  # Ожидаем точное значение
        (1, 1, 5, 5)
    ])
    def test_geometric_sum(self, a, r, n, expected):
        assert round(geometric_sum(a, r, n), 4) == expected  # Округляем до 4 знаков после запятой


# Класс для тестирования строковых функций
class TestTextFunctions:

    @pytest.mark.parametrize("text, expected", [
        ("Hello world", 2),
        ("This is a test", 4),
        ("", 0)
    ])
    def test_count_words(self, text, expected):
        assert count_words(text) == expected

    @pytest.mark.parametrize("text, substring, expected", [
        ("Hello world", "world", True),
        ("This is a test", "test", True),
        ("This is a test", "hello", False)
    ])
    def test_contains_substring(self, text, substring, expected):
        assert contains_substring(text, substring) == expected

    @pytest.mark.parametrize("text, expected", [
        ("hello", "HELLO"),
        ("hello world", "HELLO WORLD"),
        ("Test", "TEST")
    ])
    def test_to_upper_case(self, text, expected):
        assert to_upper_case(text) == expected

    @pytest.mark.parametrize("word, expected", [
        ("test", True),
        ("hello", False),
        ("sample", True)
    ])
    def test_contains_substring_from_file(self, sample_text, word, expected):
        assert contains_substring(sample_text, word) == expected
