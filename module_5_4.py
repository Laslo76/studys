class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, max_floors):
        self.name = name
        self.number_of_floors = max_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def go_to(self, new_floor):
        if not (new_floor in range(1, self.number_of_floors + 1)):
            print("Такого этажа не существует!")
            return
        for floor in range(1, new_floor + 1):
            print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if not isinstance(other, House):
            raise Exception(f'Нельзя сравнивать объекты различных типов!')
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, House):
            raise Exception(f'Нельзя сравнивать объекты различных типов!')
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House):
            raise Exception(f'Нельзя сравнивать объекты различных типов!')
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other, House):
            raise Exception(f'Нельзя сравнивать объекты различных типов!')
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance(other, House):
            raise Exception(f'Нельзя сравнивать объекты различных типов!')
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House):
            raise Exception(f'Нельзя сравнивать объекты различных типов!')
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            raise Exception(f'Количество этажей должно быть целым, положительным числом!')
        if value < 0:
            raise Exception(f'Количество этажей должно быть целым, положительным числом!')
        self.number_of_floors += value
        return self

    def __radd__(self, value):
        if not isinstance(value, int):
            raise Exception(f'Количество этажей должно быть целым, положительным числом!')
        if value < 0:
            raise Exception(f'Количество этажей должно быть целым, положительным числом!')
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if not isinstance(value, int):
            raise Exception(f'Количество этажей должно быть целым, положительным числом!')
        if value < 0:
            raise Exception(f'Количество этажей должно быть целым, положительным числом!')
        self.number_of_floors += value
        return self


if __name__ == "__main__":
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)

    del h2
    del h3

    print(House.houses_history)
