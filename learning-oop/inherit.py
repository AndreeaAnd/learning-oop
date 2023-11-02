class QuadrupedAnimal:
    legs_no=4

    def __init__(self, name):
        self.__name=name

    def __str__(self):
        # return f'({type(self)}, {self.name})'
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name=name

    @name.deleter
    def name(self):
        del self.__name

    def change_name(self, name):
        self.__name=name

    @staticmethod
    def speak():
        pass


class Dog(QuadrupedAnimal):
    @staticmethod
    def speak():
        print('Bark, bark!')


class Cat(QuadrupedAnimal):
    @staticmethod
    def speak():
        print('Meow, meow!')


class Cow(QuadrupedAnimal):
    @staticmethod
    def speak():
        print('Muu, muu!')


my_dog=Dog(name='Rex')
my_cat=Dog(name='Kitty')
my_cow=Dog(name='Joiana')

print(my_dog)
print(my_cat)
print(my_cow)