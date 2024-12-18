import time

class User:
    def __init__(self, nickname, password, age):
        if not isinstance(age, int):
            raise ValueError('возраст указыввется только числом')
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = str(title)
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode
    def __str__(self):
        return self.title
    def __eq__(self, other):
        return other.title == self.title


class UrTube:
    def __init__(self,):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
            print(f'пользователь {nickname} создан успешно')
        else:
            print(f'пользователь с логином {nickname} существует')

    def log_in(self, nickname, password):
        for user in self.users:
            if (nickname, hash(password)) == (user.nickname , user.password):# создаем и сравниваем два кортежа
            # if (nickname == user.nickname and hash(password) == user.password): тут сравниваем сначала логины потом пароли
                self.current_user = user
                print(f'пользователь {nickname} вошел в систему')
                return
        print('неверное имя пользователя или пароль')

    def log_out(self):
        self.current_user = None

    def add(self, *videos : Video):
        for video in videos:
            # # if video.title not in self.videos:  проверка производится по самому обьекту,
            # в таком исполнении лучше добавить __eq__ в видео что б сравнение шло по названию
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)
            else:
                print(f'видео с названием {video.title} уже добавлено')

    def get_videos(self, search):
        title = []
        for video in self.videos:
            if search.lower() in str(video).lower():
                title.append(video)
        return title

    def watch_video(self, title):
        if self.current_user is None:
            print('войдите в аккаунт')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age >= 18:
                    while video.time_now < video.duration:
                        video.time_now += 1
                        time.sleep(.1)
                        print(video.time_now, end=' ')
                    video.time_now = 0
                    print('конец видео')
                else:
                    print('вам нет 18 лет, покиньте страницу')



ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)



# Добавление видео

ur.add(v1, v2)



# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))



# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')



# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)



# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')


