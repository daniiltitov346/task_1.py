import numpy as np
import matplotlib.pyplot as plt
import math

# Переводим градусы в радианы
def deg_to_rad(degrees):
    return degrees * math.pi / 180

# Создаем массив значений x в градусах
x_degrees = np.linspace(-360, 360, 1000)
x_radians = np.array([deg_to_rad(x) for x in x_degrees])

# Вычисляем значения функций
f_x = (np.exp(np.cos(x_radians)) +
       np.log(np.cos(0.6 * x_radians)**2 + 1) * np.sin(x_radians))

h_x = (-np.log((np.cos(x_radians) + np.sin(x_radians))**2 + 2.5) + 10)

# Создаем график
plt.figure(figsize=(12, 8))

# График функции f(x)
plt.subplot(2, 1, 1)
plt.plot(x_degrees, f_x, 'b-', linewidth=2, label='$f(x) = e^{cosx} + \ln(cos^2(0.6x) + 1) \cdot sinx$')
plt.xlabel('Градусы')
plt.ylabel('f(x)')
plt.title('График функции f(x)')
plt.grid(True, alpha=0.3)
plt.legend()

# График функции h(x)
plt.subplot(2, 1, 2)
plt.plot(x_degrees, h_x, 'r-', linewidth=2, label='$h(x) = -\ln((cosx + sinx)^2 + 2.5) + 10$')
plt.xlabel('Градусы')
plt.ylabel('h(x)')
plt.title('График функции h(x)')
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()

# Дополнительно: оба графика на одном рисунке для сравнения
plt.figure(figsize=(10, 6))
plt.plot(x_degrees, f_x, 'b-', linewidth=2, label='f(x)')
plt.plot(x_degrees, h_x, 'r-', linewidth=2, label='h(x)')
plt.xlabel('Градусы')
plt.ylabel('y')
plt.title('Графики функций f(x) и h(x)')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()