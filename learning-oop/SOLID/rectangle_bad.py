class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


r = Rectangle(1, 2)
print(r.__dict__)

sq = Square(2)
print(sq.__dict__)

print(r['width'])




