# Bogushev V.V.
def get_multiplied_digits(number: int = 0) -> int:
    str_number = str(number)
    if len(str_number) < 2:
        return int(str_number[0])
    else:
        return int(str_number[0]) * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(44))
