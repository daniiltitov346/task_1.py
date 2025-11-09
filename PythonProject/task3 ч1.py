import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle, Polygon, PathPatch
from matplotlib.path import Path

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_aspect('equal')
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

# Цвета для тропической рыбки
body_color = '#FF6B35'
fin_color = '#FF8E53'
tail_color = '#FF5252'
accent_color = '#FFD700'
eye_color = '#2C3E50'

# ОСНОВНОЕ ТЕЛО (гладкий эллипс)
body = Ellipse((6, 4), 5, 2.5, angle=0, color=body_color, alpha=0.95, linewidth=2, edgecolor='#E55A2D')
ax.add_patch(body)

# ХВОСТ - изящная форма
tail_points = np.array([[3.5, 4], [2, 2.8], [1.8, 4], [2, 5.2]])
tail = Polygon(tail_points, color=tail_color, alpha=0.9, linewidth=1.5, edgecolor='#D84343')
ax.add_patch(tail)

# СПИННОЙ ПЛАВНИК
dorsal_fin = Polygon([[5, 5.2], [4.5, 6], [6.5, 6], [6, 5.2]], color=fin_color, alpha=0.9, linewidth=1.5,
                     edgecolor='#E57D53')
ax.add_patch(dorsal_fin)


# ГОЛОВА
head = Ellipse((7.5, 4), 1.8, 1.8, angle=0, color=body_color, alpha=0.95, linewidth=2, edgecolor='#E55A2D')
ax.add_patch(head)

# ГЛАЗ - детализированный
eye_outer = Circle((8, 4.3), 0.5, color='white', alpha=0.95, linewidth=2, edgecolor='#CCCCCC')
eye_inner = Circle((8.1, 4.3), 0.25, color=eye_color, alpha=0.95)
eye_highlight = Circle((8.15, 4.35), 0.08, color='white', alpha=0.8)
ax.add_patch(eye_outer)
ax.add_patch(eye_inner)
ax.add_patch(eye_highlight)

# РОТ
mouth = Polygon([[7, 3.8], [6.8, 4], [7, 4.2]], color='#333333', alpha=0.8)
ax.add_patch(mouth)

# ЖАБРЫ
gill = Ellipse((6.8, 4), 0.3, 0.8, angle=90, color='#E55A2D', alpha=0.6, fill=False, linewidth=1.5)
ax.add_patch(gill)

# УЗОР НА ТЕЛЕ - аккуратные чешуйки
scales = [
    Circle((5.5, 4.2), 0.15, color=accent_color, alpha=0.7, fill=False, linewidth=1),
    Circle((5, 3.8), 0.12, color=accent_color, alpha=0.7, fill=False, linewidth=1),
    Circle((5, 4.4), 0.12, color=accent_color, alpha=0.7, fill=False, linewidth=1),
    Circle((4.5, 4), 0.1, color=accent_color, alpha=0.7, fill=False, linewidth=1),
    Circle((6, 3.7), 0.13, color=accent_color, alpha=0.7, fill=False, linewidth=1),
    Circle((6, 4.5), 0.13, color=accent_color, alpha=0.7, fill=False, linewidth=1)
]

for scale in scales:
    ax.add_patch(scale)


# ПОЛОСКИ НА ПЛАВНИКАХ
def add_fin_stripes(fin_patch, num_stripes=3):
    bounds = fin_patch.get_path().vertices
    x_vals = bounds[:, 0]
    y_vals = bounds[:, 1]

    for i in range(1, num_stripes + 1):
        t = i / (num_stripes + 1)
        stripe_y = np.min(y_vals) + t * (np.max(y_vals) - np.min(y_vals))
        ax.plot([np.min(x_vals), np.max(x_vals)], [stripe_y, stripe_y],
                color='#FFFFFF', alpha=0.4, linewidth=1)


# Добавляем полоски на плавники
add_fin_stripes(dorsal_fin)

# ПУЗЫРЬКИ
bubbles = [
    Circle((8.5, 5.5), 0.12, color='lightblue', alpha=0.6, fill=False, linewidth=1.5),
    Circle((8.8, 5.8), 0.08, color='lightblue', alpha=0.6, fill=False, linewidth=1.5),
    Circle((9, 6), 0.15, color='lightblue', alpha=0.6, fill=False, linewidth=1.5)
]

for bubble in bubbles:
    ax.add_patch(bubble)

plt.title('Аккуратная тропическая рыбка 🐠', fontsize=16, pad=20, color='#2C3E50')
plt.tight_layout()
plt.show()