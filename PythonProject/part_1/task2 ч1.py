import numpy as np
import matplotlib.pyplot as plt

# Создаем массив значений x
x = np.linspace(-10, 10, 1000)

# Вычисляем значения функции
f_x = 5 / (x**2 - 9)

# Создаем график
plt.figure(figsize=(10, 6))
plt.plot(x, f_x, 'b-', linewidth=2, label='$f(x) = \\frac{5}{x^2 - 9}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции $f(x) = \\frac{5}{x^2 - 9}$')
plt.grid(True, alpha=0.3)
plt.legend()

# Устанавливаем пределы по оси y для лучшего отображения
plt.ylim(-10, 10)

# Добавляем вертикальные асимптоты
plt.axvline(x=-3, color='red', linestyle='--', alpha=0.5, label='Вертикальные асимптоты')
plt.axvline(x=3, color='red', linestyle='--', alpha=0.5)

# Добавляем горизонтальную асимптоту
plt.axhline(y=0, color='green', linestyle='--', alpha=0.5, label='Горизонтальная асимптота y=0')

plt.legend()
plt.show()