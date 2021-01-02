
class Animal:
    def __init__(self, name: str, gender: str, age: int=0):
        self.__name = name
        self.__gender = gender
        self.__age = age

    # Name

    @property
    def name(self):
        return self.__name

    @name.getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name

        else:
            raise TypeError('name can be only string')

    # Gender

    @property
    def gender(self):
        return self.__gender

    @gender.getter
    def gender(self):
        return self.__gender

    # Age

    @property
    def age(self):
        return self.__age

    @age.getter
    def age(self):

        age_output = str(self.__age)
        last_num = int(age_output[-1])

        if last_num == 0 or last_num in range(5, 10):
            age_output += ' лет'

        elif last_num == 1:
            age_output += ' год'

        else:
            age_output += ' года'

        return age_output

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            if new_age > 0:
                self.__age = new_age

            else:
                raise ValueError('age cant be less than zero')
        else:
            raise TypeError('age can be only int')

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Parrot(Animal):
    pass
