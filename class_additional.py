class User:
    '''
    класс пользователя, запрашивающий логин. пароль,
    '''
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password
        else:
            None

    def valid_password(self):
        if len(self.password) < 8:
            return 'пароль не можеть быть меньше восьми элементов!'

        has_upper = False
        has_digit = False

        for elem in self.password:
            if elem.isupper():
                has_upper = True
            elif elem.isdigit():
                has_digit = True
        if not has_upper:
            print('пароль ддолжен содержать хотя бы одну букву в верхнем регистре')
        if not has_digit:
            print('пароль должен содержать минимум одну цифру')
        return None




class Database:
    def __init__(self):
        self.data = {}

    def Add_user(self, username, password):
        self.data[username] = password




if __name__ == '__main__':
    database = Database()
    while True:
        choise = input('приветствую! выберите действие: \n1 - Вход\n2 - регистрация\n ')
        if choise == '1':
            username = input('введите логин')
            password = input('введите пароль')
            if username in database.data and database.data[username] == password:
                print(f'добро пожаловать {username}')
                break
            else:
                print('неправильный логин или пароль')

        elif choise == '2':
            # username = input('введите ваш логин:')
            # password1 = input('введите пароль')
            # password2 = input('повторите пароль')
            user = User(input('Введите логин: '), password1 := input('введите пароль: '),
                        password2 := input('повторите пароль: '))
            if password1 != password2:
                print('пароли не совпадают')
                continue
            database.Add_user(user.username, user.password)
            print((f'пользователь {user.username} добавлен успешно.'))

        print(database.data)
