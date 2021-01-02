
class Rectangle:
    def __init__(self, width: int, height: int):

        self.width = width
        self.height = height

    @property
    def info(self):
        return f'width = {self.width}, height = {self.height}, area = {self.width*self.height}'


if __name__ == '__main__':

    rectangle = Rectangle(5, 12)
    print(rectangle.info)