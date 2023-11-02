class Bird:
    def __init__(self, name):
        self.name=name


class FlyingBird(Bird):
    def fly(self):
        print('Fly')

class Eagle(FlyingBird):

class Penguin(Bird)