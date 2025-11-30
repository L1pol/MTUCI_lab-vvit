class UserAccount:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password: str):
        self.__password = new_password

    def check_password(self, password: str) -> bool:
        return self.__password == password


user = UserAccount("салфетка5", "mellstroy@money.com", "bembembem")

pwd = input("Введите пароль: ")
print(user.check_password(pwd))

new_pwd = input("Введите новый пароль: ")
user.set_password(new_pwd)
print(f'Пароль изменен: {new_pwd}')