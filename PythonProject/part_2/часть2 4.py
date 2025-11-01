"""
Задача 4: Вычисление определенного и двойного интегралов
"""

import numpy as np
from scipy import integrate


def main():
    print("ВЫЧИСЛЕНИЕ ИНТЕГРАЛОВ")
    print("=" * 40)

    # Определенный интеграл: ∫(x² + 2x + 1) dx от 0 до 2
    def f1(x):
        return x ** 2 + 2 * x + 1

    a, b = 0, 2
    result1, error1 = integrate.quad(f1, a, b)

    print("ОПРЕДЕЛЕННЫЙ ИНТЕГРАЛ:")
    print(f"∫(x² + 2x + 1) dx от {a} до {b}")
    print(f"Результат: {result1:.3f}")

    # Двойной интеграл: ∫∫(x + y) dxdy, где x от 0 до 1, y от 0 до 2
    def f2(x, y):
        return x + y

    x_bounds = [0, 1]
    y_bounds = [0, 2]
    result2, error2 = integrate.dblquad(f2, x_bounds[0], x_bounds[1],
                                        lambda x: y_bounds[0], lambda x: y_bounds[1])

    print("\nДВОЙНОЙ ИНТЕГРАЛ:")
    print(f"∫∫(x + y) dxdy, x∈[{x_bounds[0]},{x_bounds[1]}], y∈[{y_bounds[0]},{y_bounds[1]}]")
    print(f"Результат: {result2:.3f}")


if __name__ == "__main__":
    main()