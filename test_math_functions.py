import pytest
from math_functions import multiply, divide, distance, solve_quadratic, geometric_sum
#Лях Никита 107б2
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(5, 0)

def test_distance():
    assert distance(0, 0, 3, 4) == 5
    assert distance(1, 1, 1, 1) == 0

def test_solve_quadratic():
    assert solve_quadratic(1, -3, 2) == (2, 1)
    assert solve_quadratic(1, 2, 1) == (-1, -1)
    assert solve_quadratic(1, 1, 1) == None

def test_geometric_sum():
    assert geometric_sum(1, 2, 3) == 7
    assert geometric_sum(1, 1, 3) == 3
    assert geometric_sum(1, 0, 5) == 1  # Для r=0, сумма равна первому элементу

