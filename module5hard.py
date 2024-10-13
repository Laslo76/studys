import time


class User:
    """
    User - класс пользователей системы.
    Обладает тремя атрибутами:
    nick_name - имя пользователя,
    password - хэш пароля,
    age - возраст.
    """
    nick_name = None
    age = 0
    password = ''

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return self.nick_name

    def __eq__(self, other):
        if not isinstance(other, User):
            raise Exception(f'Нельзя сравнивать объекты различных типов!')
        return self.nick_name == other.nick_name


class Video:
    """
    Video - класс видео объектов в системе.
    Обладает атрибутами:
    title - заголовок,
    duration - продолжительность,
    time_now - текущее время просмотра,
    adult_mode - ограничения по возрасту.
    """
    title = ''
    duration = 0
    time_now = 0
    adult_mode = False

    def __init__(self, *args, **kwargs):
        self.title = args[0]
        self.duration = args[1]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f'{self.title} ({self.duration})'


class UrTube:
    """
    Главный объект системы UrTube.

    """
    users = []
    videos = []
    current_user = None

    def log_in(self, nick_name, passwd):
        for user_item in self.users:
            if user_item.nickname == nick_name and user_item.password == passwd:
                self.current_user = user_item
        if self.current_user is None:
            print("Пользователь {nick_name} не идентифицирован.")

    def register(self, nickname, password, age):
        for user_item in self.users:
            if user_item.nick_name == nickname:
                print(f"Пользователь {nickname} уже существует")
                if user_item.password == password:
                    self.current_user = user_item
                return
        new_user = User(nick_name=nickname, password=password, age=age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        print(f'{self.current_user}, до свиданья!')
        self.current_user = None

    def add(self, *args):
        for args_item in args:
            self.videos.append(args_item)

    def get_videos(self, search_video, return_title=True):
        if return_title:
            return [video.title for video in self.videos if video.title.upper().find(search_video.upper()) > -1]
        else:
            return [video for video in self.videos if video.title.upper().find(search_video.upper()) > -1]

    def watch_video(self, name_video):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return
        for current_video in self.get_videos(name_video, return_title=False):
            if current_video.adult_mode:
                if self.current_user.age < 18:
                    print(f'Вам нет 18 лет, пожалуйста покиньте страницу!')
                    continue
            print(f'{current_video}:')
            while current_video.time_now <= current_video.duration:
                current_video.time_now += 1
                time.sleep(1)
                print(current_video.time_now, end=' ')
            print(f'Конец видео.')
            current_video.time_now = 0


if __name__ == '__main__':
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
