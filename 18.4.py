# Считываем количество дел
try:
    n = int(input("Введите количество дел на сегодня: "))
except ValueError:
    print("Ошибка: Введите целое число.")
    exit()

# Создаем пустой массив для дел
todo = []

# Запрашиваем дела у пользователя и записываем их в массив
for i in range(n):
    deal = input(f"Введите дело номер {i + 1}: ")
    todo.append(deal)


def print_todo():
    """Выводит текущий список дел."""
    print("Ваш список дел на сегодня:")
    for i, deal in enumerate(todo):
        print(f"{i + 1}. {deal}")


# Выводим полученный список
print_todo()


def get_valid_index(prompt):
    """Запрашивает у пользователя индекс и проверяет его валидность."""
    while True:
        try:
            index = int(input(prompt)) - 1
            if 0 <= index < len(todo):
                return index
            else:
                print("Ошибка: Неверный номер дела.")
        except ValueError:
            print("Ошибка: Введите целое число.")


# Редактирование дела
edit_index = get_valid_index("Введите номер дела, которое нужно отредактировать: ")
if edit_index is not None:
    new_deal = input("Введите новое описание дела: ")
    todo[edit_index] = new_deal
    print("Дело отредактировано.")
    print_todo()  # Выводим список после редактирования

# Удаление дела
delete_index = get_valid_index("Введите номер дела, которое нужно удалить: ")
if delete_index is not None:
    del todo[delete_index]
    print("Дело удалено.")
    print_todo()  # Выводим список после удаления