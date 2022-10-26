from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def Calculate_Square_Root(Number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number: float) -> float:
    if your_number <= 0:
        return sqrt(your_number)
    print(f'Мы вычислили квадратный корень '
          f'из введённого вами числа. Это будет: '
          f'{Calculate_Square_Root(your_number)}')


print(message)
calc(25.5)
