# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
import json
import pytest

from Task_HW13 import Project
from Users import User


@pytest.fixture
def project():
    return Project([User('Korry', 75, 2), User('Frenk', 56, 6)])

@pytest.fixture
def admin():
    return User('Korry', 75, 2)

@pytest.fixture
def user():
    return User('Amanda', 786, 5)

def test_fill_project_users_lst():
    file = 'task1_test.json'
    with open(file, 'w', encoding='utf-8') as f:
        data = {"3": {"126": "Helga", }, "4": {"789": "Max", }, "6": {"8549": "Alex", "7483": "Nik", }}
        json.dump(data, f, ensure_ascii=True)
    return file

def enter(project, admin):
    project.enter(admin.name, admin.u_id, admin.level)
    assert project.admin == admin

def test_add_user(project, user, admin):
    project.enter(admin.name, admin.u_id, admin.level)
    project.add_user(user.name, user.u_id, user.level)
    assert user in project.project_users_lst

def test_del_user(project, admin):
    project.enter(admin.name, admin.u_id, admin.level)
    project.del_user(project.project_users_lst[1].name, project.project_users_lst[1].u_id, project.project_users_lst[1].level)
    assert len(project.project_users_lst) == 1


if __name__ == "__main__":
    pytest.main(["-v"])