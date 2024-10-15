# Bogushev V.V.

def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError as exp:
        if isinstance(a, str):
            result = a + str(b)
        elif isinstance(b, str):
            result = str(a) + b
        elif isinstance(a, float):
            result = a + float(b)
        else:
            result = float(a) + b
    return result


if __name__ == '__main__':
    print(add_everything_up(123.456, 'строка'))
    print(add_everything_up('яблоко', 4215))
    print(add_everything_up(123.456, 7))
