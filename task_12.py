BASE_PRICE = 24.99
INCLUDED_MINUTES = 60
INCLUDED_SMS = 30
INCLUDED_MB = 1024  # 1 ГБ = 1024 МБ

EXTRA_MINUTE = 0.89
EXTRA_SMS = 0.59
EXTRA_MB = 0.79

TAX_RATE = 0.02

used_minutes = int(input("Введите количество израсходованных минут: "))
used_sms = int(input("Введите количество израсходованных SMS: "))
used_mb = int(input("Введите количество израсходованных МБ: "))

extra_minutes = max(0, used_minutes - INCLUDED_MINUTES)
extra_sms = max(0, used_sms - INCLUDED_SMS)
extra_mb = max(0, used_mb - INCLUDED_MB)

extra_minutes_cost = extra_minutes * EXTRA_MINUTE
extra_sms_cost = extra_sms * EXTRA_SMS
extra_mb_cost = extra_mb * EXTRA_MB

subtotal = BASE_PRICE + extra_minutes_cost + extra_sms_cost + extra_mb_cost

tax = subtotal * TAX_RATE

total = subtotal + tax


print("СЧЕТ ЗА ТЕЛЕФОН")
print("Базовая стоимость тарифа:", round(BASE_PRICE, 2), "руб.")

if extra_minutes > 0:
    print("Дополнительные минуты (", extra_minutes, "мин.):", round(extra_minutes_cost, 2), "руб.")

if extra_sms > 0:
    print("Дополнительные SMS (", extra_sms, "шт.):", round(extra_sms_cost, 2), "руб.")

if extra_mb > 0:
    print("Дополнительный трафик (", extra_mb, "МБ):", round(extra_mb_cost, 2), "руб.")

print("Налог (2%):", round(tax, 2), "руб.")

print("ИТОГО К ОПЛАТЕ:", round(total, 2), "руб.")
