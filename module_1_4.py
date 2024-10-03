# Богушев В.В.
my_string = input("Введите произвольный текст: ")
print(f'Длинна строки: {len(my_string)}')
print(f'Строки в верхнем регистре: {my_string.upper()}')
print(f'Строки в нижнем регистре: {my_string.lower()}')
print(f'Строка с удаленным пробелом: {my_string.replace(" ", "")}')
print(f'Первый символ строки: {my_string[0:1]}')
print(f'Последний символ строки: {my_string[-1::]}')