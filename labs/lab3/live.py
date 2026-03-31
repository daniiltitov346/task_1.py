#написать класс учебные дисциплины со свойствами: название дисциплины,семестр в котором она изучается, количество часов, от него создаем классы наследники шде должно происходить переопределение количества часов(разбиение на количество лабораторных и лекционных часов, и преподаватель). обьекты классы мы должны добавлять через пользовательский ввод
class EducationalDiscipline:
    def __init__(self, name, semester, hours):
        self.name = name
        self.semester = semester
        self.hours = hours

    def show(self):
        print(f"Название: {self.name}")
        print(f"Семестр: {self.semester}")
        print(f"Часы: {self.hours}")


class LectureDiscipline(EducationalDiscipline):
    def __init__(self, name, semester, hours, lecture_hours, lab_hours, teacher):
        super().__init__(name, semester, hours)
        self.lecture_hours = lecture_hours
        self.lab_hours = lab_hours
        self.teacher = teacher
        self.hours = lecture_hours + lab_hours

    def show(self):
        super().show()
        print(f"Лекционные часы: {self.lecture_hours}")
        print(f"Лабораторные часы: {self.lab_hours}")
        print(f"Преподаватель: {self.teacher}")


disciplines = []

while True:
    print("\n1. Добавить дисциплину")
    print("2. Показать все дисциплины")
    print("3. Выйти")
    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Введите название дисциплины: ")
        semester = input("Введите семестр: ")
        hours = int(input("Введите общее количество часов: "))

        print("\nТип дисциплины:")
        print("1. Базовая")
        print("2. С разделением часов")
        discipline_choice = input("Ваш выбор: ")

        if discipline_choice == "1":
            try:
                discipline = EducationalDiscipline(name, semester, hours)
                disciplines.append(discipline)
                print("Дисциплина добавлена!")
            except ValueError as e:
                print("Ошибка ввода данных")
                print(e)

        elif discipline_choice == "2":
            lecture = int(input("Введите лекционные часы: "))
            lab = int(input("Введите лабораторные часы: "))
            teacher = input("Введите преподавателя: ")

            try:
                discipline = LectureDiscipline(name, semester, hours, lecture, lab, teacher)
                disciplines.append(discipline)
                print("Дисциплина добавлена!")
            except ValueError as e:
                print("Ошибка ввода данных")
                print(e)
    elif choice == "2":
        if not disciplines:
            print("Список дисциплин пуст")
        else:
            print(f"\nВсего дисциплин: {len(disciplines)}")
            for i, disc in enumerate(disciplines, 1):
                print(f"\n*** Дисциплина {i} ***")
                disc.show()

    elif choice == "3":
        print("Выход из программы")
        break

    else:
        print("Неверный выбор")