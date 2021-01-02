
class Rectangle:
    def __init__(self, x: int, y: int, width: int, height: int):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f'{__class__.__name__} ({self.x}, {self.y}, {self.width}, {self.height})'


if __name__ == '__main__':

    rectange = Rectangle(5, 10, 50, 100)
    print(str(rectange))
