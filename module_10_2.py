# Bogushev V.V.
from time import sleep
from datetime import datetime
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.day_combat = 0
        self.name = name
        self.power = power
        self.warriors = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.warriors > 0:
            self.day_combat += 1
            self.warriors -= self.power
            print(f'{self.name} сражался {self.day_combat} день(дня)..., осталось {self.warriors} воинов')
            sleep(1.0)
        print(f'{self.name} одержал победу спустя {self.day_combat} дней(дня)!"')


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print("Все битвы закончились!")
