# Bogushev V.V.
def custom_write(file_name: str, strings: list) -> dict:
    result_dict = {}
    if file_name == '':
        raise Exception('Не задано имя файла!')
    writings_file = open(file_name, "a", encoding='utf8')
    current_num = 1
    for current_str in strings:
        key_str = (current_num, writings_file.tell())
        writings_file.write(f'{current_str}\n')
        result_dict[key_str] = current_str
        current_num += 1
    writings_file.close()
    return result_dict


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)
