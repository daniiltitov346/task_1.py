"""
Часть 3. Генерация синтетических данных о вступительной кампании
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from faker import Faker
import random
from datetime import datetime

# Инициализация Faker для генерации реалистичных данных
fake = Faker('ru_RU')


def generate_student_data(num_students=800):
    """Генерация синтетических данных о студентах"""

    data = {
        'fio': [],
        'admission_year': [],
        'study_form': [],
        'ct_score_russian': [],
        'ct_score_math': [],
        'ct_score_physics': [],
        'ct_score_foreign_lang': [],
        'ct_score_history': [],
        'certificate_score': [],
        'total_score': [],
        'specialty': [],
        'address': [],
        'phone': []
    }

    # Специальности и соответствующие предметы ЦТ
    specialties = {
        'Информатика и вычислительная техника': ['math', 'physics', 'russian'],
        'Экономика': ['math', 'foreign_lang', 'russian'],
        'Юриспруденция': ['history', 'foreign_lang', 'russian'],
        'Менеджмент': ['math', 'history', 'russian'],
        'Психология': ['biology', 'history', 'russian'],
        'Лингвистика': ['foreign_lang', 'history', 'russian'],
        'Медицина': ['biology', 'chemistry', 'russian'],
        'Строительство': ['math', 'physics', 'russian'],
        'Дизайн': ['creative', 'history', 'russian'],
        'Журналистика': ['creative', 'history', 'russian']
    }

    study_forms = ['Бюджет', 'Платная', 'Целевая']
    current_year = datetime.now().year
    admission_years = list(range(current_year - 4, current_year + 1))

    for _ in range(num_students):
        data['fio'].append(fake.name())

        year = random.choice(admission_years)
        data['admission_year'].append(year)

        study_form = random.choice(study_forms)
        data['study_form'].append(study_form)

        # Выбор специальности
        specialty = random.choice(list(specialties.keys()))
        data['specialty'].append(specialty)

        # Генерация баллов ЦТ по предметам
        required_subjects = specialties[specialty]

        # Обнуляем все предметы
        for subject in ['russian', 'math', 'physics', 'foreign_lang', 'history']:
            data[f'ct_score_{subject}'].append(0)

        # Заполняем баллы только по требуемым предметам
        total_ct_score = 0
        for subject in required_subjects:
            if subject in ['russian', 'math', 'physics', 'foreign_lang', 'history']:
                base_score = 50 + (year - admission_years[0]) * 3
                score = max(0, min(100, int(np.random.normal(base_score, 12))))
                data[f'ct_score_{subject}'][-1] = score
                total_ct_score += score
            elif subject == 'biology':
                base_score = 55 + (year - admission_years[0]) * 2
                score = max(0, min(100, int(np.random.normal(base_score, 10))))
                total_ct_score += score
            elif subject == 'chemistry':
                base_score = 52 + (year - admission_years[0]) * 2
                score = max(0, min(100, int(np.random.normal(base_score, 11))))
                total_ct_score += score
            elif subject == 'creative':
                base_score = 65 + (year - admission_years[0]) * 1
                score = max(0, min(100, int(np.random.normal(base_score, 8))))
                total_ct_score += score

        # Средний балл аттестата
        cert_score = round(np.random.normal(7.8, 0.8), 1)
        cert_score = max(6.0, min(10.0, cert_score))
        data['certificate_score'].append(cert_score)

        # Общий балл (сумма ЦТ + аттестат с коэффициентом)
        total_score = total_ct_score + cert_score * 10
        data['total_score'].append(total_score)

        # Адрес и телефон
        data['address'].append(fake.address())
        data['phone'].append(fake.phone_number())

    return pd.DataFrame(data)


def visualize_admission_data(df):
    """Визуализация данных вступительной кампании"""

    plt.figure(figsize=(20, 15))

    # 1. Динамика среднего балла за ЦТ по предметам
    plt.subplot(2, 3, 1)
    subjects = ['russian', 'math', 'physics', 'foreign_lang', 'history']
    subject_names = ['Русский', 'Математика', 'Физика', 'Иностранный', 'История']

    for i, subject in enumerate(subjects):
        subject_data = df.groupby('admission_year')[f'ct_score_{subject}'].mean()
        plt.plot(subject_data.index, subject_data.values, marker='o', label=subject_names[i], linewidth=2)

    plt.title('Динамика среднего балла за ЦТ по предметам', fontsize=12, fontweight='bold')
    plt.xlabel('Год')
    plt.ylabel('Средний балл')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(df['admission_year'].unique())  # Только целые годы на оси X

    # 2. Динамика среднего балла аттестата
    plt.subplot(2, 3, 2)
    cert_by_year = df.groupby('admission_year')['certificate_score'].mean()
    plt.plot(cert_by_year.index, cert_by_year.values, marker='s', color='green', linewidth=2, markersize=6)
    plt.title('Динамика среднего балла аттестата', fontsize=12, fontweight='bold')
    plt.xlabel('Год')
    plt.ylabel('Средний балл аттестата')
    plt.grid(True, alpha=0.3)
    plt.xticks(df['admission_year'].unique())  # Только целые годы на оси X

    # 3. Динамика проходного балла
    plt.subplot(2, 3, 3)
    passing_by_year = df.groupby('admission_year')['total_score'].mean()
    plt.plot(passing_by_year.index, passing_by_year.values, marker='^', color='red', linewidth=2, markersize=6)
    plt.title('Динамика среднего общего балла', fontsize=12, fontweight='bold')
    plt.xlabel('Год')
    plt.ylabel('Средний общий балл')
    plt.grid(True, alpha=0.3)
    plt.xticks(df['admission_year'].unique())  # Только целые годы на оси X

    # 4. Количество поступивших по специальностям
    plt.subplot(2, 3, 4)
    specialty_counts = df['specialty'].value_counts()
    plt.barh(range(len(specialty_counts)), specialty_counts.values, color='lightblue')
    plt.yticks(range(len(specialty_counts)), specialty_counts.index, fontsize=9)
    plt.title('Количество поступивших по специальностям', fontsize=12, fontweight='bold')
    plt.xlabel('Количество студентов')

    # 5. Статистика по формам обучения
    plt.subplot(2, 3, 5)
    study_form_counts = df['study_form'].value_counts()
    colors = ['lightgreen', 'lightcoral', 'gold']
    plt.pie(study_form_counts.values, labels=study_form_counts.index, autopct='%1.1f%%', colors=colors)
    plt.title('Распределение по формам обучения', fontsize=12, fontweight='bold')

    # 6. Распределение общего балла по годам
    plt.subplot(2, 3, 6)
    for year in sorted(df['admission_year'].unique()):
        year_data = df[df['admission_year'] == year]['total_score']
        plt.hist(year_data, alpha=0.6, label=str(year), bins=15)
    plt.title('Распределение общего балла по годам', fontsize=12, fontweight='bold')
    plt.xlabel('Общий балл')
    plt.ylabel('Количество студентов')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def print_statistics(df):
    """Вывод статистической информации"""
    print("СТАТИСТИКА ВСТУПИТЕЛЬНОЙ КАМПАНИИ")
    print("=" * 50)
    print(f"Общее количество студентов: {len(df)}")
    print(f"Период данных: {df['admission_year'].min()} - {df['admission_year'].max()} годы")

    print(f"\nКоличество студентов по годам:")
    year_counts = df['admission_year'].value_counts().sort_index()
    for year, count in year_counts.items():
        print(f"  {year} год: {count} студентов")

    print(f"\nСредние показатели по годам:")
    stats_by_year = df.groupby('admission_year').agg({
        'ct_score_russian': 'mean',
        'ct_score_math': 'mean',
        'certificate_score': 'mean',
        'total_score': 'mean'
    }).round(1)
    print(stats_by_year)


def main():
    # Генерация данных
    print("Генерация данных о вступительной кампании...")
    df = generate_student_data(800)

    # Вывод статистики
    print_statistics(df)

    # Визуализация
    print("\nСоздание визуализаций...")
    visualize_admission_data(df)

    # Сохранение данных
    df.to_csv('admission_campaign_data.csv', index=False, encoding='utf-8-sig')
    print(f"\nДанные сохранены в файл: admission_campaign_data.csv")


if __name__ == "__main__":
    main()