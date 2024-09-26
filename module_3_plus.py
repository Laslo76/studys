# Bogushev V.V.
def calculate_structure_sum(data_, res=0):
    if type(data_) in (int, float, bool):
        return data_
    elif type(data_) is str:
        return len(data_)
    elif type(data_) is dict:
        return calculate_structure_sum(list(data_.items()))
    elif type(data_) in (tuple, list, set):
        for i in data_:
            res += calculate_structure_sum(i)
        return res
    else:
        raise Exception(f'Ошибка Типов! Нельзя обработать {type(data_)}.')


data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6, {'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(calculate_structure_sum(data_structure))
