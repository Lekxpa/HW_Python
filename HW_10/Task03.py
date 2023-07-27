# Возьмите 1-3 любые задачи из прошлых семинаров, 
# которые вы уже решали. Превратите функции в методы класса. 
# Задачи должны решаться через вызов методов экземпляра.


# Функция генерирует N простых чисел,
# начиная с числа 2.
# Для проверки числа на простоту используйте правило:
# «число является простым, если делится нацело только на единицу и на себя».

class SimpleNumbs:

    def __init__(self, num):
        self.num = num
    
    def gen(self):
        start = 2
        yield start
        cnt = 1
        while cnt < self.num:
            start += 1
            for i in range(2, int((start ** 0.5) + 1)):
                if start % i == 0:
                    break
            else:
                cnt += 1
                yield start


dt = SimpleNumbs(10)
print(*dt.gen())