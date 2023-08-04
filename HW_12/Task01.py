# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
from pathlib import Path

class Check_name:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not value.isalpha():
            raise ValueError('Имя должно состоять только из букв')
        if not value.istitle():
            raise ValueError('Имя должно начинаться с заглавной буквы')
        instance.__dict__[self.name] = value

class Student:
    MIN_GRADE = 2
    MAX_GRADE = 5
    MIN_TEST = 0
    MAX_TEST = 100

    last_name = Check_name()
    first_name = Check_name()
    middle_name = Check_name()

    def __init__(self, last_name, first_name, middle_name, file):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.fio = last_name + ' ' + first_name + ' ' + middle_name
        self.subjects = self.file_subjects(file)
        self.grade = {subject: [] for subject in self.subjects}
        self.result_of_tests = {subject: [] for subject in self.subjects}
    
    
    def file_subjects(self, file):
        """ работаем с файлом-перечнем предметов"""
        subject = []
        with open(file, 'r', encoding='utf-8') as f_csv:
            reader = csv.reader(f_csv)
            for line in reader:
                subject.extend(line)
        return subject

    def add_grade(self, subject, grade):
        """добавляем оценки по предметам"""
        if subject not in self.subjects:
            raise ValueError('Такого предмета нет')
        if grade < Student.MIN_GRADE or grade > Student.MAX_GRADE:
            raise ValueError('Оценка вне допустимого диапазона')
        self.grade[subject].append(grade)

    def add_result_of_tests(self, subject, result_of_tests):
        """добавляем результаты тестов"""
        if subject not in self.subjects:
            raise ValueError('Такого предмета нет')
        if result_of_tests < Student.MIN_TEST or result_of_tests > Student.MAX_TEST:
            raise ValueError('Результат теста вне допустимого диапазона')
        self.result_of_tests[subject].append(result_of_tests)

    def grade_average(self, subject):
        """средняя оценка"""
        if subject not in self.subjects:
            raise ValueError('Такого предмета нет')
        grade = self.grade[subject]
        if not grade:
            return None
        return f'Средняя оценка по {subject} - {sum(grade) / len(grade)}'
    
    def all_average_grades(self):
        """средний балл по всем предметам"""
        grade = [grade for subject_gr in self.grade.values() for grade in subject_gr]
        if not grade:
            return None
        return f'Средний балл по всем предметам - {sum(grade) / len(grade)}'

    def tests_average(self, subject):
        """средний балл по тестам по каждому предмету"""
        if subject not in self.subjects:
            raise ValueError('Такого предмета нет')
        average_test = self.result_of_tests[subject]
        if not average_test:
            return None
        return f'Средний балл по тестам по предмету {subject} - {sum(average_test) / len(average_test)}'
    

    def all_average_tests(self):
        """средний балл по тестам по всем предметам"""
        result_of_tests = [result for subject_res in self.result_of_tests.values() for result in subject_res]
        if not result_of_tests:
            return None
        return f'Средний балл по тестам по всем предметам - {sum(result_of_tests) / len(result_of_tests)}'
    
    def __str__(self):
        return f'ФИО: {self.fio}'

if __name__ == '__main__':
    new_data_1 = Student('Fran', 'Alex', 'Ivanovich', Path('subjects.csv'))
    print(new_data_1)
    new_data_1.add_grade('история', 5)
    new_data_1.add_grade('история', 4)
    new_data_1.add_grade('география', 5)
    new_data_1.add_grade('география', 3)
    print(new_data_1.grade_average('история'))
    new_data_1.add_result_of_tests('литература', 98)
    new_data_1.add_result_of_tests('литература', 58)
    new_data_1.add_result_of_tests('алгебра', 80)
    new_data_1.add_result_of_tests('геометрия', 95)
    print(new_data_1.tests_average('литература'))
    print(new_data_1.all_average_grades())
    print(new_data_1.all_average_tests())
    
