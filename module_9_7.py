# Bogushev V.V.

def is_prime(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        prime = True
        if not result in [-2, -1, 0, 1, 2]:
            point = min(result + 1, 2)
            fin = max(-2, result)
            while point < fin and prime:
                prime = result % point != 0
                point += 1
        if prime:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(first, second, third):
    return first + second + third


if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)
