
class GuestList:
    def __init__(self, *args):

        self.guest_list = []

        for i in args:
            self.append(i)

    def append(self, guest):

        if isinstance(guest, Guest):
            self.guest_list.append(guest)

        else:
            raise TypeError('Non guest type')

    def __repr__(self):
        
        output_string = ''

        for i in range(len(self.guest_list)-1):
            output_string += str(self.guest_list[i])+'\n'

        output_string += str(self.guest_list[-1])

        return output_string

class Guest:
    def __init__(self, name: str, surname: str, city: str, status: str=None):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status

    @property
    def info(self):
        if self.status is None:
            return f'«{self.name} {self.surname}, г. {self.city}»'

        return f'«{self.name} {self.surname}, г. {self.city}, статус "{self.status}"»'

    def __repr__(self):
        return self.info

class Veterinarian(Guest):
    pass

class Volunteer(Guest):
    def __init__(self, name, surname, city, status='Новичек'):
        super().__init__(name, surname, city, status)


if __name__ == '__main__':

    guest_1 = Veterinarian('Игорь', 'Шашков', 'Александров')
    guest_2 = Volunteer('Марина', 'Кудрявцева', 'Фокино', 'Наставник')
    guest_3 = Veterinarian('Ирина', 'Симоненко', 'Калининск')
    guest_4 = Guest('Сергей', 'Савин', 'Сорочинск')
    guest_5 = Volunteer('Егор', 'Соболев', 'Москва', 'Наставник')
    guest_6 = Volunteer('Кирилл', 'Рябов', 'Азов')
    guest_7 = Guest('Лариса', 'Сафонова', 'Самара')

    guest_list = GuestList(
        guest_1, guest_2, guest_3,
        guest_4, guest_5, guest_6,
        guest_7,
    )

    print(guest_list)
