# Bogushev V.V.

def is_prime(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if result in [0, 1]:
            prime = True
        elif result < 0:
            prime = True
            for i in range(result+1, -2):
                prime = result % i != 0
                if not prime:
                    break
        else:
            prime = True
            for i in range(2, result):
                prime = result % i != 0
                if not prime:
                    break
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
    result = sum_three(-97, -2, 2)
    print(result)
