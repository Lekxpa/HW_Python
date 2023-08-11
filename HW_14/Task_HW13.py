# Доработать класс Project
# Доработайте классы исключения так,
# чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.


# Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта.
# Класс имеет следующие методы:
# Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
# Метод входа в систему – требует указать имя и id пользователя. Далее метод создает пользователя и проверяет
# есть ли он в списке пользователей проекта. Если в списке его нет, то вызывается исключение доступа.
# Если пользователь присутствует в списке пользователей проекта, то пользователь, который входит получает
# его уровень доступа и становится администратором.
# Метод добавление пользователя в список пользователей. Если уровень пользователя меньше,
# чем уровень админа, вызывайте исключение уровня доступа.
# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера
import json

from Users import User
from Excepts import NotAllowedError, LevelError, AdminError


class Project:
    def __init__(self, project_users_lst=None):
        if project_users_lst is None:
            project_users_lst = []
        self.project_users_lst = project_users_lst
        self.admin = None

    @classmethod
    def fill_project_users_lst(cls):
        with open('task2.json', 'r', encoding='utf-8') as f:
            file = json.load(f)
            temp = []
            for key in file:
                for user in file[key].items():
                    temp.append(User(user[1], int(user[0]), int(key)))
            return cls(temp)

    def enter(self, name, user_id, level):
        """вход в систему"""
        user = User(name, user_id, level)
        for proj_user in self.project_users_lst:
            if user == proj_user:
                self.admin = proj_user
                break
        else:
            raise NotAllowedError(name, user_id)

    def add_user(self, name, user_id, level):
        """добавление пользователя в Project"""
        if self.admin is None:
            raise AdminError(name, user_id)
        if level < self.admin.level:
            raise LevelError(level, self.admin.level)
        self.project_users_lst.append(User(name, user_id, level))

    def del_user(self, name, user_id, level):
        """удаление пользователя из Project"""
        if self.admin is None:
            raise AdminError(name, user_id)
        if level < self.admin.level:
            raise LevelError(level, self.admin.level)
        try:
            self.project_users_lst.remove(User(name, user_id, level))
        except ValueError:
            # raise ValueError('ПОльзователя нет в списке') так нельзя делать, тк обрабатываем исключение и тут же бросаем ислючение
            print('ПОльзователя нет в списке')

    def __enter__(self):
        return self

    def __repr__(self):
        return f'Project({self.project_users_lst},\n\nadmin = {self.admin})'

    def __exit__(self, exc_type, exc_value, traceback):
        with open('task2.json', 'w', encoding='utf-8') as f:
            json.dump(self.project_users_lst, f)


p = Project.fill_project_users_lst()
print(f'\n{p}\n')
p.enter("Hip", 12354, 2)
print(f'\n{p}\n')
p.add_user('Helga', 789, 4)
print(f'\n{p}\n')
# p.add_user('Vlad', 675, 1)
# print(f'\n{p}\n')
# p.del_user('Helga', 789, 4)
# print(f'{p}\n')