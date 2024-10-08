# Bogushev V.V.

class Horse:
    x_distance = 0

    def __init__(self):
        self.sound = 'Frrr'
        super().__init__()

        """ Если вызов метода super().__init__() поставить
        первой строкой то Pegasus.sound() будет возвращать
                            Frrr  
        """
    def run(self, dx):
        self.x_distance += dx


class Eagle:
    y_distance = 0

    def __init__(self):
        self.sound = 'I train, eat, sleep, and repeat'
        super().__init__()

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


if __name__ == '__main__':
    p1 = Pegasus()

    print(p1.get_pos())
    p1.move(10, 15)
    print(p1.get_pos())
    p1.move(-5, 20)
    print(p1.get_pos())

    p1.voice()
