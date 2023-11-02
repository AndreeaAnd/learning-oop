class Dog:
    legs_no=4

    # def __init__(self, name):
    #     self.name=name

    # __ => private

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

    # def change_name(self, name):
    #     self.name=name

    @staticmethod
    def speak():
        return('Bark, bark!')


# print(Dog)
# my_first_dog = Dog('Rex')
# my_second_dog = Dog('Azorel')
# print(my_first_dog)
# print(my_second_dog)
#
# print(my_first_dog.legs_no)
# print(Dog.legs_no)
# my_first_dog.change_name('Azorel')
# print(my_first_dog)
# my_second_dog.change_name('Rex')
# print(my_second_dog)
#
# print(Dog.speak())
# print(my_second_dog.speak())

my_dog=Dog(name='Rex')
my_dog.name='Ben'
print(my_dog)

# del my_dog.name
print(my_dog.name)
my_dog.name='Linda'
print(my_dog.name)









