from random import choice, randint
from string import ascii_letters


class AccountData:
    NAME = "Dzhaka"
    EMAIL = "dzhalatabaev10_911@mail.com"
    PASSWORD = "12345qwerty"
    INCORRECT_PASSWORD = "1123"


class UserDataGenerator:
    @staticmethod
    def user_data_generator():
        user_data = {'name': str(choice(ascii_letters) * 5).title(),
                     'email': "dzhal" + str(randint(100, 999)) + '@gmail.com',
                     'password': str(randint(100000, 999999))}
        return user_data

