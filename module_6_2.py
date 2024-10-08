# Bogushev V.V.

class Vehicle:
    _COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    owner = ''
    __model = ''
    __engine_power = 0
    __color = ''

    def __init__(self, owner, model, color, power):
        self.owner = owner
        self.__model = model
        self.set_color(color)
        self.__engine_power = power

    def get_model(self) -> str:
        return f'Модель: {self.__model}.'

    def get_horsepower(self) -> str:
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self) -> str:
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in self._COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}.')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


if __name__ == '__main__':
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Изначальные свойства
    vehicle1.print_info()

    # Меняем свойства (в т.ч. вызывая методы)
    vehicle1.set_color('Pink')
    vehicle1.set_color('BLACK')
    vehicle1.owner = 'Vasyok'

    # Проверяем что поменялось
    vehicle1.print_info()
