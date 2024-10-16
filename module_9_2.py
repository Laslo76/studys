# Bogushev V.V.

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(elem) for elem in first_strings if len(elem) > 5]
second_result = [(first_str, sec_str) for first_str in first_strings for sec_str in second_strings if len(first_str) == len(sec_str)]
third_result = {elem: len(elem) for elem in first_strings + second_strings if not len(elem) % 2}

print(first_result)
print(second_result)
print(third_result)
