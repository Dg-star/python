#Иванов Артём 107б2
import math

# 1. Умножение
def multiply(a, b):
    return a * b

# 2. Деление
def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль невозможно!")
    return a / b

# 3. Расстояние между двумя точками (по формуле Пифагора)
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 4. Квадратное уравнение (решение по формуле дискриминанта)
def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Нет действительных корней"
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)

# 5. Сумма геометрической прогрессии
def geometric_sum(a, r, n):
    if r == 1:
        return a * n  # Если r = 1, прогрессия не меняется
    return a * (1 - r**n) / (1 - r)
