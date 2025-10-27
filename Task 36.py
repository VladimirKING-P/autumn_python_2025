# Инкапсуляция и property
#todo: Класс "Пользователь" (Валидация email)
# Создайте класс User. У него должны быть свойства email и password.
# При установке email проверяйте, что строка содержит символ @ (простая валидация).
# При установке пароля, храните не сам пароль, а его хеш (для простоты можно использовать hash()).
# Сделайте метод check_password(password), который проверяет, соответствует ли хеш переданного
# пароля сохраненному хешу.

import hashlib

class User:
    def __init__(self, email, password):
        self._email = None
        self._password_hash = None

        self._email = email
        self._password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if '@' not in value:
            raise ValueError('Email должен содержать символ @')
        self._email = value

    @property
    def password(self):
        raise AttributeError('Пароль нельзя получить на прямую')

    @password.setter
    def password(self, value):
        self._password_hash = hashlib.sha256(value.encode()).hexdigest()

    def check_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest() == self._password_hash

try:
    user = User("test@example.com", "secret")
    print(f"Email: {user.email}")

    print("Пароль верный", user.check_password("secret_password123"))
    print("Пароль верный", user.check_password("wrong_password"))

    user.email = "valentin_email"

except ValueError as e:
    print(f"Ошибка {e}")
