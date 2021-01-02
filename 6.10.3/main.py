
class Client:
    def __init__(self, name: str, surname:str, balance: int):

        self.name = name
        self.surname = surname
        self.balance = balance 

    @property
    def info(self):
        return f'Клиент: «{self.name} {self.surname}». Баланс: {self.balance} руб'


if __name__ == '__main__':

    client = Client('Иван', 'Петров', 50)
    print(client.info)