# Bogushev V.V.
def calculate_structure_sum(data_structure) -> int:
    res = 0
    if type(data_structure) in (int, float):
        return data_structure
    elif type(data_structure) is str:
        return len(data_structure)
    elif type(data_structure) is bool:
        if data_structure:
            return 1
        else:
            return 0
    elif type(data_structure) in (tuple, list, set):
        for i in data_structure:
            res += calculate_structure_sum(i)
        return res
    elif type(data_structure) is dict:
        for i in data_structure.keys():
            res += calculate_structure_sum(i)
        for i in data_structure.values():
            res += calculate_structure_sum(i)
        return res
    else:
        raise Exception('Ошибка Типов!')


data_structure = [
                    [1, 2, 3],
                    {'a': 4, 'b': 5},
                    (6, {'cube': 7, 'drum': 8}),
                    "Hello",
                    ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)
