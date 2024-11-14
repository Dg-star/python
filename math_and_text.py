import math
#Иванов Артём 107б2
# Умножение
def multiply(a, b):
    return a * b

# Деление
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
# Вычисление расстояния между двумя точками
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# Решение квадратного уравнения
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        raise ValueError("No real solutions")
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
# Сумма геометрической прогрессии
def geometric_sum(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)
# Определение количества слов
def count_words(text):
    return len(text.split())
# Нахождение подстроки
def contains_substring(text, substring):
    return substring in text
# Преобразование всех букв в верхний регистр
def to_upper_case(text):
    return text.upper()
