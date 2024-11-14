# test_calculations.py

import pytest
from calculations import multiply, divide, distance, quadratic_equation, geometric_sum

# 1. Тесты для умножения
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0
    assert multiply(-2, -3) == 6
    assert multiply(1, 1) == 1

# 2. Тесты для деления
def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(0, 5) == 0
    with pytest.raises(ValueError):
        divide(5, 0)
#Лях Никита 107б2
# 3. Тесты для расстояния между точками
def test_distance():
    assert distance(0, 0, 3, 4) == 5
    assert distance(1, 1, 1, 1) == 0
    assert distance(-1, -1, 2, 2) == 4.242640687119285
    assert distance(0, 0, 0, 0) == 0
    assert distance(0, 0, -3, -4) == 5

# 4. Тесты для квадратного уравнения
def test_quadratic_equation():
    assert quadratic_equation(1, -3, 2) == (2, 1)
    assert quadratic_equation(1, 2, 1) == -1
    assert quadratic_equation(1, 0, -1) == (1, -1)
    assert quadratic_equation(1, 0, 1) == "Нет действительных корней"
    assert quadratic_equation(2, -8, 6) == (3, 1)

# 5. Тесты для суммы геометрической прогрессии
def test_geometric_sum():
    assert geometric_sum(1, 2, 3) == 7
    assert geometric_sum(1, 1, 5) == 5
    assert geometric_sum(1, 0.5, 4) == 1.875
    assert geometric_sum(2, 2, 3) == 14
    assert geometric_sum(1, -1, 3) == 1.0  # Исправлено на 1.0

