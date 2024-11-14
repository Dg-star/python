import math

# Умножение
def multiply(a, b):
    return a * b

# Деление
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

# Вычисление расстояния между двумя точками (x1, y1) и (x2, y2)
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Решение квадратного уравнения ax^2 + bx + c = 0
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # Нет реальных корней
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2

# Сумма геометрической прогрессии
def geometric_sum(a, r, n):
    if r == 1:
        return a * n  # Специальный случай для r=1
    if r == 0:
        return a  # В случае r=0 сумма равна только первому элементу
    return a * (1 - r**n) / (1 - r)

