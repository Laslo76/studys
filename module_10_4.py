from threading import Thread
from time import sleep
from queue import Queue
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *args):
        self.tables = args
        self.queue = Queue()

    def guest_arrival(self, *args):
        free_tables = list(filter(lambda x: x.guest is None, self.tables))
        for _ in args:
            if len(free_tables) > 0:
                current_table = free_tables.pop()
                current_table.guest = _
                print(f"{_.name} сел(-а) за стол номер {current_table.number}")
                _.start()
            else:
                self.queue.put(_)
                print(f"{_.name} в очереди")

    def discuss_guests(self):
        used_tables = list(filter(lambda x: x.guest is not None, self.tables))
        while not self.queue.empty() or len(used_tables) > 0:
            for table in used_tables:
                if table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла). Стол номер {table.number} свободен")
                    table.guest = None

                    if not self.queue.empty():
                        guest = self.queue.get()
                        table.guest = guest
                        print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        guest.start()
            used_tables = list(filter(lambda x: x.guest is not None, self.tables))


if __name__ == '__main__':
    # Создание столов
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Mariya', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Victoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # Приём гостей
    cafe.guest_arrival(*guests)
    # Обслуживание гостей
    cafe.discuss_guests()
