# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Настройки
plt.rcParams['figure.figsize'] = (12, 6)
sns.set_style("whitegrid")

print("АНАЛИЗ ДАННЫХ ПРОДАЖ АВИАБИЛЕТОВ S7")
print("=" * 50)

# Загрузка данных
try:
    df = pd.read_excel('s7_data_sample_rev4_50k.xlsx', sheet_name='DATA', engine='openpyxl')
    print(f" Загружено {len(df)} записей")
except Exception as e:
    print(f" Ошибка загрузки: {e}")
    exit()

# Преобразование дат
df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'])
df['FLIGHT_DATE_LOC'] = pd.to_datetime(df['FLIGHT_DATE_LOC'])

# 1. ОБЩИЕ СТАТИСТИКИ
print("\n1. ОБЩИЕ СТАТИСТИКИ")
print("-" * 40)
print(f"Записи: {len(df):,}")
print(f"Выручка: {df['REVENUE_AMOUNT'].sum():,.0f} у.е.")
print(f"Средний чек: {df['REVENUE_AMOUNT'].mean():.0f} у.е.")
print(f"Период: {df['ISSUE_DATE'].min().date()} - {df['ISSUE_DATE'].max().date()}")

# 2. АЭРОПОРТЫ
print("\n2. АНАЛИЗ АЭРОПОРТОВ")
print("-" * 40)
top_orig = df['ORIG_CITY_CODE'].value_counts().head(5)
top_dest = df['DEST_CITY_CODE'].value_counts().head(5)
print("Топ-5 аэропортов вылета:")
print(top_orig)
print("\nТоп-5 аэропортов прилета:")
print(top_dest)

# 3. СЕЗОННОСТЬ
print("\n3. СЕЗОННОСТЬ")
print("-" * 40)
monthly_flights = df.groupby(df['FLIGHT_DATE_LOC'].dt.to_period('M')).size()
monthly_revenue = df.groupby(df['FLIGHT_DATE_LOC'].dt.to_period('M'))['REVENUE_AMOUNT'].sum()
print("Перелеты по месяцам:")
print(monthly_flights)

# 4. ПАССАЖИРЫ
print("\n4. АНАЛИЗ ПАССАЖИРОВ")
print("-" * 40)
pax_stats = df.groupby('PAX_TYPE').agg({
    'REVENUE_AMOUNT': ['count', 'mean', 'sum']
})
print("Статистика по типам пассажиров:")
print(pax_stats.round(0))

# 5. СПОСОБЫ ОПЛАТЫ
print("\n5. СПОСОБЫ ОПЛАТЫ")
print("-" * 40)
fop_counts = df['FOP_TYPE_CODE'].value_counts().head(5)
sale_counts = df['SALE_TYPE'].value_counts()
print("Топ-5 способов оплаты:")
print(fop_counts)
print(f"\nКаналы продаж:")
print(sale_counts)

# 6. ПРОГНОЗ
print("\n6. ПРОГНОЗ ПРОДАЖ")
print("-" * 40)

def simple_linear_regression(x, y):
    x_mean, y_mean = np.mean(x), np.mean(y)
    b1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
    b0 = y_mean - b1 * x_mean
    return b0, b1

monthly_data = df.groupby(df['FLIGHT_DATE_LOC'].dt.to_period('M')).agg({
    'REVENUE_AMOUNT': 'sum',
    'FLIGHT_DATE_LOC': 'count'
}).rename(columns={'FLIGHT_DATE_LOC': 'FLIGHT_COUNT'})

monthly_data = monthly_data.reset_index()
monthly_data['MONTH_NUM'] = range(len(monthly_data))

X = monthly_data['MONTH_NUM'].values
y_revenue = monthly_data['REVENUE_AMOUNT'].values
y_flights = monthly_data['FLIGHT_COUNT'].values

b0_rev, b1_rev = simple_linear_regression(X, y_revenue)
b0_fl, b1_fl = simple_linear_regression(X, y_flights)

next_month = len(monthly_data)
pred_revenue = b0_rev + b1_rev * next_month
pred_flights = b0_fl + b1_fl * next_month

print(f"Прогноз на следующий месяц:")
print(f"• Выручка: {pred_revenue:,.0f} у.е.")
print(f"• Перелеты: {pred_flights:.0f}")

# ВИЗУАЛИЗАЦИИ
fig, axes = plt.subplots(2, 3, figsize=(16, 10))

# 1. Распределение стоимости
axes[0,0].hist(df['REVENUE_AMOUNT'], bins=50, alpha=0.7, color='skyblue', edgecolor='black')
axes[0,0].set_title('Распределение стоимости билетов', fontsize=14, fontweight='bold')
axes[0,0].set_xlabel('Стоимость (у.е.)')
axes[0,0].set_ylabel('Количество')
axes[0,0].grid(True, alpha=0.3)

# 2. Топ аэропорты вылета
sns.barplot(x=top_orig.values, y=top_orig.index, ax=axes[0,1], color='lightblue', hue=top_orig.index, legend=False)
axes[0,1].set_title('Топ-5 аэропортов вылета', fontsize=14, fontweight='bold')
axes[0,1].set_xlabel('Количество вылетов')

# 3. Топ аэропорты прилета
sns.barplot(x=top_dest.values, y=top_dest.index, ax=axes[0,2], color='lightcoral', hue=top_dest.index, legend=False)
axes[0,2].set_title('Топ-5 аэропортов прилета', fontsize=14, fontweight='bold')
axes[0,2].set_xlabel('Количество прилетов')

# 4. Сезонность перелетов
axes[1,0].plot(monthly_flights.index.astype(str), monthly_flights.values, marker='o', linewidth=2, markersize=6)
axes[1,0].set_title('Количество перелетов по месяцам', fontsize=14, fontweight='bold')
axes[1,0].set_xlabel('Месяц')
axes[1,0].set_ylabel('Количество перелетов')
axes[1,0].tick_params(axis='x', rotation=45)
axes[1,0].grid(True, alpha=0.3)

# 5. Типы пассажиров
pax_counts = df['PAX_TYPE'].value_counts()
axes[1,1].pie(pax_counts.values, labels=pax_counts.index, autopct='%1.1f%%', startangle=90,
              colors=['lightblue', 'lightcoral', 'lightgreen'])
axes[1,1].set_title('Распределение типов пассажиров', fontsize=14, fontweight='bold')

# 6. Каналы продаж
sale_data = df['SALE_TYPE'].value_counts()
axes[1,2].bar(sale_data.index, sale_data.values, color=['blue', 'red'], alpha=0.7)
axes[1,2].set_title('Онлайн vs Офлайн продажи', fontsize=14, fontweight='bold')
axes[1,2].set_ylabel('Количество продаж')
for i, v in enumerate(sale_data.values):
    axes[1,2].text(i, v + 100, f'{v}\n({v/len(df)*100:.1f}%)',
                   ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

# ДОПОЛНИТЕЛЬНЫЕ ГРАФИКИ
fig2, axes2 = plt.subplots(1, 2, figsize=(14, 5))

# Способы оплаты
sns.barplot(x=fop_counts.values, y=fop_counts.index, ax=axes2[0],
            hue=fop_counts.index, legend=False, palette='viridis')
axes2[0].set_title('Топ-5 способов оплаты', fontsize=14, fontweight='bold')
axes2[0].set_xlabel('Количество')

# Прогноз
months_display = [str(m) for m in monthly_data['FLIGHT_DATE_LOC']] + ['Прогноз']
flight_values = list(monthly_data['FLIGHT_COUNT']) + [pred_flights]

axes2[1].plot(range(len(monthly_data)), monthly_data['FLIGHT_COUNT'],
             'o-', linewidth=2, markersize=6, label='Факт')
axes2[1].plot(len(monthly_data), pred_flights, 'ro', markersize=10, label='Прогноз')
axes2[1].set_title('Прогноз количества перелетов', fontsize=14, fontweight='bold')
axes2[1].set_xlabel('Период')
axes2[1].set_ylabel('Количество перелетов')
axes2[1].legend()
axes2[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ИТОГИ
print("\n" + "=" * 60)
print("ИТОГОВЫЕ ВЫВОДЫ")
print("=" * 60)
print(f"1.  ОБЩАЯ СТАТИСТИКА:")
print(f"   • Всего записей: {len(df):,}")
print(f"   • Общая выручка: {df['REVENUE_AMOUNT'].sum():,.0f} у.е.")
print(f"   • Средний чек: {df['REVENUE_AMOUNT'].mean():.0f} у.е.")

print(f"\n2.  АЭРОПОРТЫ:")
print(f"   • Самый популярный аэропорт вылета: {top_orig.index[0]} ({top_orig.iloc[0]} вылетов)")
print(f"   • Самый популярный аэропорт прилета: {top_dest.index[0]} ({top_dest.iloc[0]} прилетов)")

print(f"\n3.  СЕЗОННОСТЬ:")
print(f"   • Пиковый месяц: {monthly_flights.idxmax()} ({monthly_flights.max()} перелетов)")
print(f"   • Наименьшая активность: {monthly_flights.idxmin()} ({monthly_flights.min()} перелетов)")

print(f"\n4.  ПАССАЖИРЫ:")
print(f"   • Основной тип: {pax_counts.index[0]} ({pax_counts.iloc[0]/len(df)*100:.1f}%)")
print(f"   • Средняя стоимость по типам: AD-{pax_stats.iloc[0,1]:.0f} у.е., CHD-{pax_stats.iloc[1,1]:.0f} у.е.")

print(f"\n5.  ОПЛАТА И ПРОДАЖИ:")
print(f"   • Доля онлайн-продаж: {sale_counts['ONLINE']/len(df)*100:.1f}%")
print(f"   • Основной способ оплаты: {fop_counts.index[0]} ({fop_counts.iloc[0]/len(df)*100:.1f}%)")

print(f"\n6.  ПРОГНОЗ:")
print(f"   • Перелеты на след. месяц: {pred_flights:.0f}")
print(f"   • Выручка на след. месяц: {pred_revenue:,.0f} у.е.")

# Анализ программы лояльности
if 'FFP_FLAG' in df.columns:
    ffp_participation = df['FFP_FLAG'].value_counts().get('FFP', 0) / len(df) * 100
    print(f"   • Участие в программе лояльности: {ffp_participation:.1f}%")

print(f"\n7.  РЕКОМЕНДАЦИИ:")
print(f"   • Усилить маркетинг в месяцы с низкой активностью")
print(f"   • Развивать программу лояльности (текущее участие: {ffp_participation:.1f}%)")
print(f"   • Оптимизировать работу с аэропортом {top_orig.index[0]}")
print(f"   • Улучшить онлайн-каналы продаж")

print("\n" + "=" * 60)