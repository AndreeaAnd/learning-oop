class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Square (Rectangle):
    def __init__(self, side):
        super().__init__ (side, side)
    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ('width', 'height'):
            self.__dict__['width']=value
            self.__dict__['height'] = value

r = Rectangle(1, 2)
print(r.__dict__)

sq = Square(2)
print(sq.__dict__['width'])
