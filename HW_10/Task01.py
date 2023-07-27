# Доработаем задачи 5-6. Создайте класс-фабрику. 
# Класс принимает тип животного (название одного из созданных классов) 
# и параметры для этого типа. Внутри класса создайте экземпляр 
# на основе переданного типа и верните его из класса-фабрики.


class Animals:
    def __init__(self, name):
        self.name = name


class Fish(Animals):

    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth

    def get_special_info(self):
        return f'Для {self.name} Глубина обитания: {self.depth}'


class Bird(Animals):

    def __init__(self, name, wings):
        super().__init__(name)
        self.wings = wings

    def get_special_info(self):
        return f'Для {self.name} Размах крыльев: {self.wings}'


class Mammal(Animals):

    def __init__(self, name, coat):
        super().__init__(name)
        self.coat = coat

    def get_special_info(self):
        return f'Для {self.name} длина шерсти: {self.coat}'


class Factory:
    
    @staticmethod
    def anim_factory(cls, typeofanimal, *args):
        return cls(typeofanimal, args)
    
    # без @staticmethod
    # def anim_factory(cls, typeofanimal, *args):
    #     self.typeofanimal = typeofanimal
    #     self.quality = args
    
    # def get_typeofanimal(self):
        # return self.typeofanimal(*self.quality)

if __name__ == "__main__":

    new_anim = Factory.anim_factory(Mammal, 'Alphe', 30)
    print(new_anim.__dict__, type(new_anim))

    new_anim_1 = Factory.anim_factory(Fish, 'Ani', 10)
    print(new_anim_1.__dict__, type(new_anim_1))

# ошибка - name Elephan is not defined (и программа подчеркивает само название)
    # new_anim_2 = Factory.anim_factory(Elephan, 'An', 100)
    # print(new_anim_2.__dict__, type(new_anim_2))



    # для предыдущей задачи вывод:
    # fish = Fish('Neo', 15)
    # bird = Bird('Woody', 25)
    # mammal = Mammal('Bunny', 6)

    # print(fish.get_special_info())
    # print(bird.get_special_info())
    # print(mammal.get_special_info())