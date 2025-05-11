import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:
    students_marks[student] = {}
    # цикл по предметам
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
    {students_marks[student]}''')

print('''
Список команд:
1. Добавить оценки ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Выход из программы
5. Удалить оценку ученика по предмету
6. Редактировать оценку ученика по предмету
7. Вывести все оценки для определенного ученика
8. Вывести средний балл по каждому предмету для определенного ученика
9. Добавить ученика
10. Удалить ученика
11. Добавить предмет
12. Удалить предмет
13. Вывести список учеников
14. Вывести список предметов
''')

while True:
    try:
        command = int(input('Введите команду: '))
    except ValueError:
        print("Ошибка: Введите число от 1 до 14.")
        continue

    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        try:
            mark = int(input('Введите оценку: '))
        except ValueError:
            print("Ошибка: Оценка должна быть числом.")
            continue
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            if 1 <= mark <= 5:
                students_marks[student][class_].append(mark)
                print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
            else:
                print("Ошибка: Оценка должна быть от 1 до 5.")

        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                if class_ in students_marks[student]:
                  marks = students_marks[student][class_]
                  marks_sum = sum(marks)
                  # находим количество оценок по предмету
                  marks_count = len(marks)
                  # выводим средний балл по предмету
                  if marks_count > 0:
                      print(f'{class_} - {marks_sum // marks_count}')
                  else:
                      print(f'{class_} - Нет оценок')
                else:
                  print(f'{class_} - Нет оценок')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        try:
            mark_index = int(input('Введите номер оценки для удаления (начиная с 0): '))
        except ValueError:
            print("Ошибка: Номер оценки должен быть числом.")
            continue

        if student in students_marks.keys() and class_ in students_marks[student].keys() and 0 <= mark_index < len(students_marks[student][class_]):
            del students_marks[student][class_][mark_index]
            print(f'Оценка удалена для {student} по предмету {class_}')
        else:
            print('ОШИБКА: неверное имя ученика, название предмета или номер оценки.')
    elif command == 5:
        print('5. Редактировать оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        try:
            mark_index = int(input('Введите номер оценки для редактирования (начиная с 0): '))
            new_mark = int(input('Введите новую оценку: '))
        except ValueError:
            print("Ошибка: Номер оценки и оценка должны быть числами.")
            continue

        if student in students_marks.keys() and class_ in students_marks[student].keys() and 0 <= mark_index < len(students_marks[student][class_]):
            if 1 <= new_mark <= 5:
                students_marks[student][class_][mark_index] = new_mark
                print(f'Оценка отредактирована для {student} по предмету {class_}')
            else:
                print("Ошибка: Оценка должна быть от 1 до 5.")
        else:
            print('ОШИБКА: неверное имя ученика, название предмета или номер оценки.')
    elif command == 6:
        print('6. Вывести все оценки для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(student)
            for class_ in classes:
                if class_ in students_marks[student]:
                    print(f'\t{class_} - {students_marks[student][class_]}')
                else:
                    print(f'\t{class_} - Нет оценок')
            print()
        else:
            print('ОШИБКА: неверное имя ученика')
    elif command == 7:
        print('7. Вывести средний балл по каждому предмету для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(student)
            for class_ in classes:
                if class_ in students_marks[student]:
                    marks = students_marks[student][class_]
                    if marks:
                        average_mark = sum(marks) / len(marks)
                        print(f'{class_} - {average_mark:.2f}')
                    else:
                        print(f'{class_} - Нет оценок')
                else:
                    print(f'{class_} - Нет оценок')
            print()
        else:
            print('ОШИБКА: неверное имя ученика')

    elif command == 8:
        print('8. Добавить ученика')
        new_student = input('Введите имя нового ученика: ')
        if new_student not in students:
            students.append(new_student)
            students.sort() # Сортируем список учеников после добавления
            students_marks[new_student] = {} # Инициализируем оценки для нового ученика
            for class_ in classes:
                students_marks[new_student][class_] = []  # Инициализируем оценки по предметам
            print(f'Ученик {new_student} добавлен.')
        else:
            print('ОШИБКА: Ученик с таким именем уже существует.')
    elif command == 9:
        print('9. Удалить ученика')
        student_to_remove = input('Введите имя ученика для удаления: ')
        if student_to_remove in students:
            students.remove(student_to_remove)
            del students_marks[student_to_remove]
            print(f'Ученик {student_to_remove} удален.')
        else:
            print('ОШИБКА: Ученик с таким именем не найден.')
    elif command == 10:
        print('10. Добавить предмет')
        new_class = input('Введите название нового предмета: ')
        if new_class not in classes:
            classes.append(new_class)
            # Обновляем оценки для всех учеников, добавляя новый предмет
            for student in students:
                students_marks[student][new_class] = []
            print(f'Предмет {new_class} добавлен.')
        else:
            print('ОШИБКА: Предмет с таким названием уже существует.')
    elif command == 11:
        print('11. Удалить предмет')
        class_to_remove = input('Введите название предмета для удаления: ')
        if class_to_remove in classes:
            classes.remove(class_to_remove)
            # Удаляем оценки по предмету у всех учеников
            for student in students_marks:
                if class_to_remove in students_marks[student]:
                    del students_marks[student][class_to_remove]
            print(f'Предмет {class_to_remove} удален.')
        else:
            print('ОШИБКА: Предмет с таким названием не найден.')
    elif command == 12:
        print('12. Вывести список учеников')
        print(students)
    elif command == 13:
        print('13. Вывести список предметов')
        print(classes)
    elif command == 14:
        print('14. Выход из программы')
        break
    else:
        print("Неверная команда. Пожалуйста, введите число от 1 до 14.")