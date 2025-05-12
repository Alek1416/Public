# Создаем пустой словарь для телефонной книги
phonebook = {}

# Заполняем телефонную книгу
try:
    n = int(input("Введите количество контактов, которые хотите добавить: "))
except ValueError:
    print("Ошибка: Введите целое число.")
    exit()

for i in range(n):
    name = input(f"Введите имя контакта {i + 1}: ")
    phone = input(f"Введите номер телефона для {name}: ")
    phonebook[name] = phone

# Выводим только имена
print("\nИмена:")
for name in phonebook.keys():
    print(name)

# Выводим только номера телефонов
print("\nНомера телефонов:")
for phone in phonebook.values():
    print(phone)

# Выводим записи в формате "Контакт: {Имя} Телефон: {Номер телефона}"
print("\nЗаписи в телефонной книге:")
for name, phone in phonebook.items():
    print(f"Контакт: {name}, Телефон: {phone}")

# Добавляем номера телефонов для двух новых друзей
print("\nДобавление новых контактов:")
for i in range(2):
    new_name = input(f"Введите имя нового контакта {i + 1}: ")
    new_phone = input(f"Введите номер телефона для {new_name}: ")
    phonebook[new_name] = new_phone

# Меняем номер телефона одного из друзей
print("\nИзменение номера телефона:")
name_to_update = input("Введите имя контакта, чей номер хотите изменить: ")
if name_to_update in phonebook:
    new_phone = input(f"Введите новый номер телефона для {name_to_update}: ")
    phonebook[name_to_update] = new_phone
    print("Номер телефона обновлен.")
else:
    print("Ошибка: Контакт не найден.")

# Добавляем или удаляем контакт
print("\nДобавление или удаление контакта:")
name_to_check = input("Введите имя контакта для проверки: ")
if name_to_check in phonebook:
    del phonebook[name_to_check]
    print(f"Контакт {name_to_check} удален.")
else:
    phone_to_add = input(f"Введите номер телефона для {name_to_check}: ")
    phonebook[name_to_check] = phone_to_add
    print(f"Контакт {name_to_check} добавлен.")

# Выводим обновленную телефонную книгу
print("\nОбновленная телефонная книга:")
for name, phone in phonebook.items():
    print(f"Контакт: {name}, Телефон: {phone}")