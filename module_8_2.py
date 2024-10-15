# Bogushev V.V.

def personal_summ(numbers) -> tuple:
    incorrect_data = 0
    result = 0
    try:
        for number in numbers:
            try:
                result += number
            except TypeError:
                print(f'Некорректный тип данных для подсчёта суммы - {number}')
                incorrect_data += 1
    except TypeError:
        raise TypeError
    return result, incorrect_data


def calculate_average(numbers):
    try:
        summator = personal_summ(numbers)
        count_obj = len(numbers)
        result = summator[0] / (count_obj - summator[1])
    except ZeroDivisionError:
        result = 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных!')
        result = None
    return result


if __name__ == '__main__':
    print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
    print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
    print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
    print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
