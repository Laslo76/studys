# Bogushev V.V.

def apply_all_func(int_list, *functions):
    return {fun.__name__: fun(int_list) for fun in functions}


if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
