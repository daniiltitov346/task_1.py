seconds = int(input("Введите количество секунд: "))

minutes = seconds // 60
remaining_seconds = seconds % 60

print(minutes, "минут", remaining_seconds, "секунд")