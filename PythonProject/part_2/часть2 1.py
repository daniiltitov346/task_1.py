"""
Часть 2. NumPy, SciPy
Задача 1: Анализ расходов на проезд
"""

import numpy as np
from scipy import stats


def analyze_transport_expenses(expenses):

    expenses = np.array(expenses)

    winter_months = [11, 0, 1]
    summer_months = [5, 6, 7]

    winter_total = np.sum(expenses[winter_months])
    summer_total = np.sum(expenses[summer_months])

    if winter_total > summer_total:
        season_comparison = "Зимой тратится больше"
    elif summer_total > winter_total:
        season_comparison = "Летом тратится больше"
    else:
        season_comparison = "Расходы равны"

    max_expense = np.max(expenses)
    max_months = np.where(expenses == max_expense)[0] + 1  # +1 для номеров месяцев с 1

    return {
        'winter_total': winter_total,
        'summer_total': summer_total,
        'season_comparison': season_comparison,
        'max_months': list(max_months),
        'max_expense': max_expense
    }


def main():
    # Пример данных:  (январь - декабрь)
    monthly_expenses = [2500, 2400, 2300, 2200, 2100, 2000,
                        1900, 1800, 2200, 2300, 2400, 2600]

    print("=== Анализ расходов на проезд ===")
    print(f"Расходы по месяцам: {monthly_expenses}")
    print()

    result = analyze_transport_expenses(monthly_expenses)

    # Выводим результаты
    print("Результаты анализа:")
    print(f"Сумма зимних расходов: {result['winter_total']} руб.")
    print(f"Сумма летних расходов: {result['summer_total']} руб.")
    print(f"Сравнение: {result['season_comparison']}")
    print(f"Максимальный расход: {result['max_expense']} руб.")

    # Визуализация (простая текстовая)
    print("\nВизуализация расходов:")
    months = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн',
              'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']

    for i, (month, expense) in enumerate(zip(months, monthly_expenses)):
        marker = "  MAX" if (i + 1) in result['max_months'] else ""
        season = " (зима)" if i in [0, 1, 11] else " (лето)" if i in [5, 6, 7] else ""
        print(f"{month}: {expense:4d} руб.{marker}{season}")


if __name__ == "__main__":
    main()