# Bogushev V.V.
class Figure:
    side_count = 0

    def __init__(self):
        __sides = []
        __colors = []
        field = False

    def get_color(self):
        pass

    def __is_valid_color(self, r, g, b):
        pass

    def set_color(self, r, g, b):
        pass

    def __is_valid_side(self, sides:list):
        pass

    def get_sides(self):
        pass

    def __len__(self):
        pass

    def set_sides(self, *new_sides):
        pass


class Circle(Figure):
    side_count = 1
    __radius = 0

    def get_square(self):
        pass


class Triangle(Figure):
    side_count = 3

    def get_square(self):
        pass


class Cube(Figure):
    side_count = 12

    def get_volume(self):
        pass


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77) # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15) # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15) # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())
