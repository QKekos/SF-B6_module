from animals import Cat, Dog, Parrot


if __name__ == '__main__':

    animals_array = [
        Dog(name='Феликс', gender='Мальчик', age=2),
        Cat(name='Барон', gender='Мальчик', age=2),
        Dog(name='Линда', gender='Девочка', age=2),
        Parrot(name='Гоша', gender='Мальчик', age=1),
        Dog(name='Мухтар', gender='Мальчик', age=0),
        Cat(name='Сэм', gender='Мальчик', age=2)
    ]

    for animal in animals_array:
        print(animal.name, animal.gender, animal.age, sep=', ')