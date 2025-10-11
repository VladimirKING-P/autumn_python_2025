#todo: База данных пользователя.
# Задан массив объектов пользователя
# users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
#         {'login': 'Ivan',  'age': 10, 'group': "guest"},
#         {'login': 'Dasha', 'age': 30, 'group': "master"},
#         {'login': 'Fedor', 'age': 13, 'group': "guest"}]
# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
# Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
# тип сортировки: 1
# Затем сообщение для ввода
# Введите критерии поиска: 16
# Результат:
# Пользователь: 'Piter' возраст 23 года , группа  "admin"
# Пользователь: 'Dasha' возраст 30 лет , группа  "master"

users = [
    {'login': 'Piter', 'age': 23, 'group': "admin"},
    {'login': 'Ivan', 'age': 10, 'group': "guest"},
    {'login': 'Dasha', 'age': 30, 'group': "master"},
    {'login': 'Fedor', 'age': 13, 'group': "guest"}
]

def filter_users():

    sort_type = input("Выберите тип сортировки:\n1. По возрасту\n2. По первой букве\n3. По группе\n Тип сортировки: ")
    
    criteria = input("Введите критерии поиска: ")

    if sort_type == '1':
        # Фильтрация по возрасту
        filtered = [user for user in users if user['age'] > int(criteria)]
        # Сортировка по возрасту
        filtered.sort(key=lambda x: x['age'])

    elif sort_type == "2":
        #Сортировка по первой букве
        filtered = [user for user in users if user['login']. startswith(criteria.upper())]
        
        filtered.sort(key=lambda x: x['login'])


    elif sort_type == "3":
        #Сортировка по группе
        filtered = [user for user in users if user['group'] == criteria]
        
        filtered.sort(key=lambda x: x['group'])

    else:
        print(" Неверный тип сортировки")

         #Вывод результата
    for user in filtered:
        print(f"Пользователь: '{user['login']}' возраст {user['age']}лет, группа: '{user['group']}' ")


filter_users()


