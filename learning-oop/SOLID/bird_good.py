class Bird:
    def __init__(self, name):
        self.name=name

    def fly(self):
        print('We fly!')

class FlyingBird(Bird):
    def __init__(self, name):
        super(FlyingBird, self).__init__(name)

    def fly(self):
        print('We fly!')

class Eagle(FlyingBird):
    def __init__(self, name):
        super(Eagle, self).__init__(name)

class Penguin(Bird):
    def __init__(self, name):
        super(Penguin, self).__init__(name)

    def fly(self):
        raise Exception('I cannot fly!')

b=Bird('cucurigu')

e=Eagle('some_eagle_name')
e.fly()

p=Penguin('Linux')
