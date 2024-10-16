# Bogushev V.V.

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(tup[0])-len(tup[1]) for tup in zip(first, second) if len(tup[0]) != len(tup[1]))
second_result = (len(tup[0]) == len(tup[1]) for tup in zip(first, second))

print(list(first_result))
print(list(second_result))
