"""
Задача 2: Расчет пути, времени и средней скорости автомобиля
"""


def calculate_journey():
    lengths_input = input("Введите длины участков через пробел: ")
    speeds_input = input("Введите скорости на участках через пробел: ")
    k = int(input("Введите номер участка въезда (k): "))
    p = int(input("Введите номер участка выезда (p): "))

    lengths = list(map(float, lengths_input.split()))
    speeds = list(map(float, speeds_input.split()))

    if len(lengths) != len(speeds):
        print("Ошибка: количество участков длин и скоростей не совпадает!")
        return

    if k < 1 or p > len(lengths) or k > p:
        print("Ошибка: некорректные номера участков!")
        return

    start_idx = k - 1
    end_idx = p - 1

    total_distance = sum(lengths[start_idx:end_idx + 1])

    times = []
    for i in range(start_idx, end_idx + 1):
        time = lengths[i] / speeds[i]
        times.append(time)

    total_time = sum(times)

    average_speed = total_distance / total_time if total_time > 0 else 0

    print(f"\nРезультаты расчета:")
    print(f"Длина пути с {k} по {p} участок: {total_distance:.2f} км")
    print(f"Время в пути: {total_time:.2f} час")
    print(f"Средняя скорость: {average_speed:.2f} км/ч")

    print(f"\nДетали по участкам (с {k} по {p}):")
    for i in range(start_idx, end_idx + 1):
        segment_time = lengths[i] / speeds[i]
        print(f"Участок {i + 1}: длина {lengths[i]} км, "
              f"скорость {speeds[i]} км/ч, время {segment_time:.2f} ч")


def test_example():
    """Тестовый пример из задания"""
    print("=== ТЕСТОВЫЙ ПРИМЕР ===")

    # Данные из теста
    lengths = [20, 8, 9, 18, 5, 12, 16, 16, 6, 7]
    speeds = [44, 70, 44, 66, 46, 38, 38, 37, 66, 67]
    k = 4
    p = 7

    print(f"Длины: {' '.join(map(str, lengths))}")
    print(f"Скорости: {' '.join(map(str, speeds))}")
    print(f"k = {k}, p = {p}")

    start_idx = k - 1
    end_idx = p - 1

    total_distance = sum(lengths[start_idx:end_idx + 1])

    times = []
    for i in range(start_idx, end_idx + 1):
        time = lengths[i] / speeds[i]
        times.append(time)

    total_time = sum(times)
    average_speed = total_distance / total_time

    print(f"\nРезультаты:")
    print(f"S = {total_distance:.0f} км")
    print(f"T = {total_time:.2f} час")
    print(f"V = {average_speed:.2f} км/ч")


if __name__ == "__main__":
    print("Расчет пути, времени и средней скорости автомобиля")
    print("=" * 50)

    test_example()

    print("\n" + "=" * 50)
    print("Теперь введите свои данные:")

    calculate_journey()