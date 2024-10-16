# Bogushev V.V.
from random import choice


class MysticBall:
    def __init__(self, *args):
        self.words = args

    def __call__(self):
        return choice(self.words)


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf8') as file:
            for elem in data_set:
                print(elem, file=file)

    return write_everything


if __name__ == '__main__':
    first = 'Мама мыла раму'
    second = 'Рамена мало было'

    print(list(map(lambda fs, ss: fs == ss, first, second)))

    write = get_advanced_writer('example.txt')
    write('Это строчка',  ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())
