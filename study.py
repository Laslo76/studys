matrix = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]


matrix_T = [list(i) for i in zip(*matrix)]
print(matrix_T)

dict_test = {19: 114, 112: 100, 34: 121}

print(dict_test.items())

dict_test = dict(sorted(dict_test.items(), key=lambda x: x[1], reverse=False))
print(dict_test)

files = [
    "file.txt",
    "file2.doc",
    "file3.xxx.pdf"
]

for file in files:
    file_split = file.split(".")
    file_name = ".".join(file_split[:-1])

    print(file_name)


def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number[0])


print(get_multiplied_digits(40203))
print(get_multiplied_digits(203))
print(get_multiplied_digits(240))

a = [x for x in map(int, input().split())]
print(max(a))

print(dict(enumerate(files)))
print(help(str))

