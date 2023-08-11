# Создайте класс с базовым исключением и дочерние классы-исключения:
# ошибка уровня,
# ошибка доступа.
# Вспомните задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7).
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Реализуйте магический метод проверки на равенство пользователей

class User:
    def __init__(self, name, user_id, level):
        self.name = name
        self.u_id = user_id
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.u_id == other.u_id

    def __repr__(self):
        return f'User {self.name = }, {self.u_id = }, {self.level = }'



    # def __str__(self):
    #     return f'User {self.__dict__}'


# import json
#
#
# def read_user():
#     while True:
#         try:
#             with open('task02.json', 'r', encoding='utf-8') as f:
#                 users = json.load(f)
#         except FileNotFoundError:
#             users = {}
#         u_id, level = None, None
#         name = input('Input user name: ')
#         is_valid_data = False
#         while not is_valid_data:
#             u_id, level = (i for i in input('Input spaced ID and LEVEL (1 to 7): ').split())
#             if int(level) in range(1, 8):
#                 if users:
#                     if all(u_id not in v.keys() for k, v in users.items()):
#                         is_valid_data = True
#                     else:
#                         print('ID already exists Try again')
#                 else:
#                     is_valid_data = True
#             else:
#                 print('Invalid level! Try again')
#         if level not in users:
#             users[level] = {}
#         users[level][u_id] = name
#         with open('task02.json', 'w') as f:
#             json.dump(users, f)
#             print("User added successfully!")
