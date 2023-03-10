
class Registration:

    def __init__(self, login, password):
        self.login = login
        self.__password = password

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if '@' not in value:
            raise ValueError("Логин должен содержать один символ '@'")
        if '.' not in value[value.find('@'):]:
            raise ValueError("Логин должен содержать символ '.'")
        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Пароль должен быть строкой")
        if len(value) < 5 or len(value) > 11:
            raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        if not any(_.isdigit() for _ in value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')
        if not any(_.isupper() for _ in value) or not any(_.islower() for _ in value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
        if not all(_.isalpha() for _ in value):
            raise ValueError('Пароль должен содержать только латинский алфавит')
        self.check_password_dictionary(value)
        self.__password = value

    @staticmethod
    def is_include_digit(value):
        if not any(_.isdigit() for _ in value):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')

    @staticmethod
    def is_include_all_register(value):
        if not any(_.isupper() for _ in value) and any(_.islower() for _ in value):
            raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')

    @staticmethod
    def is_include_only_latin(value):
        if any(_.isalpha() for _ in value) and any(_.isupper() for _ in value) \
                and any(_.islower() for _ in value):
            raise ValueError('Пароль должен содержать только латинский алфавит')

    @staticmethod
    def check_password_dictionary(value):
        with open('easy_passwords.txt', 'r') as file:
            for i in file.read().strip():
                if value == i:
                    ValueError('Ваш пароль содержится в списке самых легких')


r1 = Registration('qwerty@rambler.ru', 'QwrRt124')  # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
r1.password = 43  # raise TypeError("Пароль должен быть строкой")
