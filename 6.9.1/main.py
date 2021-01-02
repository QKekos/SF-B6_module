
from math import pi


class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_rec_area(self):
        return self.width * self.height

class Square :
    def __init__(self, side: int):
        self.side = side

    def get_square_area(self):
        return self.side ** 2

class Circle:
    def __init__(self, radius: int):
        self.radius = radius

    def get_circle_area(self):
        return round(pi*self.radius**2, 2)


if __name__ == '__main__':

    rect_1 = Rectangle(3, 4)
    rect_2 = Rectangle(12, 5)

    square_1 = Square(5)
    square_2 = Square(10)

    circle_1 = Circle(3)
    circle_2 = Circle(7)

    figure_array = [
        rect_1, rect_2,
        square_1, square_2,
        circle_1, circle_2
    ]

    for figure in figure_array:

        if isinstance(figure, Rectangle):
            print(figure.get_rec_area())

        elif isinstance(figure, Square):
            print(figure.get_square_area())

        elif isinstance(figure, Circle):
            print(figure.get_circle_area())
